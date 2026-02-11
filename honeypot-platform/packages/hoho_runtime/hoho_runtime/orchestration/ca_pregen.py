from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path


class EgressCAError(RuntimeError):
    """Raised when host-side egress CA generation fails."""


def _set_private_key_mode(path: Path) -> None:
    # Best-effort (some FS / platforms ignore chmod).
    try:
        os.chmod(path, 0o600)
    except OSError:
        return


def _run_openssl(args: list[str], *, cwd: Path) -> subprocess.CompletedProcess[str]:
    cmd = ["openssl", *args]
    try:
        proc = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True)
    except FileNotFoundError as exc:
        raise EgressCAError("openssl is required to pre-generate runtime egress CA but was not found") from exc

    if proc.returncode != 0:
        stderr = (proc.stderr or "").strip()
        raise EgressCAError(f"openssl command failed ({' '.join(cmd)}): {stderr[:800]}")
    return proc


def _write_mitmproxy_bundle(*, cert_path: Path, key_path: Path, bundle_path: Path) -> None:
    """
    mitmproxy expects a PEM that includes the *private key* and the cert.
    Put key first to avoid tooling that stops parsing after the first block.
    """
    key = key_path.read_text(encoding="utf-8").rstrip()
    cert = cert_path.read_text(encoding="utf-8").rstrip()
    bundle_path.write_text(f"{key}\n{cert}\n", encoding="utf-8")
    _set_private_key_mode(bundle_path)


def _cert_has_ca_true(cert_path: Path) -> bool:
    # Keep it simple: parse openssl text output.
    try:
        out = _run_openssl(["x509", "-in", str(cert_path), "-noout", "-text"], cwd=cert_path.parent).stdout
    except EgressCAError:
        return False
    return "CA:TRUE" in out


def _key_matches_cert_rsa(cert_path: Path, key_path: Path) -> bool:
    """
    We generate RSA keys; use modulus check.
    If the key is not RSA for any reason, we treat it as mismatch.
    """
    try:
        cert_mod = _run_openssl(["x509", "-in", str(cert_path), "-noout", "-modulus"], cwd=cert_path.parent).stdout.strip()
        key_mod = _run_openssl(["rsa", "-in", str(key_path), "-noout", "-modulus"], cwd=key_path.parent).stdout.strip()
    except EgressCAError:
        return False
    return bool(cert_mod) and cert_mod == key_mod


def _existing_ca_is_valid(cert_path: Path, key_path: Path) -> bool:
    if not cert_path.is_file() or cert_path.stat().st_size == 0:
        return False
    if not key_path.is_file() or key_path.stat().st_size == 0:
        return False
    if not _cert_has_ca_true(cert_path):
        return False
    if not _key_matches_cert_rsa(cert_path, key_path):
        return False
    return True


def ensure_egress_ca(
    ca_dir: Path,
    *,
    common_name: str,
    days_valid: int = 3650,
    overwrite: bool = False,
    key_bits: int = 2048,
) -> dict:
    """
    Single-mode CA generation (automatic).
    - If valid CA already exists and overwrite=False: reuse.
    - Otherwise: generate a proper CA (CA:TRUE, keyCertSign) via openssl.
    Also creates mitmproxy-compatible files:
      - mitmproxy-ca-cert.pem  (cert only)
      - mitmproxy-ca.pem       (key+cert bundle)
    """
    ca_dir.mkdir(parents=True, exist_ok=True)

    cert_path = ca_dir / "egress-ca.crt"
    key_path = ca_dir / "egress-ca.key"
    mitm_cert_path = ca_dir / "mitmproxy-ca-cert.pem"
    mitm_bundle_path = ca_dir / "mitmproxy-ca.pem"
    openssl_conf = ca_dir / "openssl.cnf"

    created = False

    if overwrite or not _existing_ca_is_valid(cert_path, key_path):
        # Minimal config to guarantee proper CA extensions.
        openssl_conf.write_text(
            """[req]
distinguished_name=req_distinguished_name
x509_extensions=v3_ca
prompt=no

[req_distinguished_name]
CN=unused

[v3_ca]
basicConstraints=critical,CA:TRUE
keyUsage=critical,keyCertSign,cRLSign
subjectKeyIdentifier=hash
""",
            encoding="utf-8",
        )

        # Generate key + self-signed CA cert.
        _run_openssl(["genrsa", "-out", str(key_path), str(key_bits)], cwd=ca_dir)
        _set_private_key_mode(key_path)

        _run_openssl(
            [
                "req",
                "-x509",
                "-new",
                "-key",
                str(key_path),
                "-sha256",
                "-days",
                str(days_valid),
                "-out",
                str(cert_path),
                "-subj",
                f"/CN={common_name}",
                "-config",
                str(openssl_conf),
                "-extensions",
                "v3_ca",
            ],
            cwd=ca_dir,
        )
        created = True

        # Sanity: fail fast if we somehow produced a non-CA cert.
        if not _existing_ca_is_valid(cert_path, key_path):
            raise EgressCAError("generated CA is invalid (missing CA:TRUE and/or key mismatch)")

    # Derive mitmproxy files from the *same* CA.
    shutil.copyfile(cert_path, mitm_cert_path)
    _write_mitmproxy_bundle(cert_path=cert_path, key_path=key_path, bundle_path=mitm_bundle_path)

    return {
        "created": created,
        "common_name": common_name,
        "egress_ca_crt": str(cert_path),
        "egress_ca_key": str(key_path),
        "mitmproxy_ca_pem": str(mitm_bundle_path),
        "mitmproxy_ca_cert_pem": str(mitm_cert_path),
    }
