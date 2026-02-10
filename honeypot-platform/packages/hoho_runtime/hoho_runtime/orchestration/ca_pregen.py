from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path


class EgressCAError(RuntimeError):
    """Raised when host-side egress CA generation fails."""


def _write_bundle(cert_path: Path, key_path: Path, bundle_path: Path) -> None:
    cert = cert_path.read_text(encoding="utf-8")
    key = key_path.read_text(encoding="utf-8")
    bundle_path.write_text(f"{cert.rstrip()}\n{key.rstrip()}\n", encoding="utf-8")


def _set_private_key_mode(key_path: Path) -> None:
    try:
        os.chmod(key_path, 0o600)
    except OSError:
        # Best-effort on platforms/filesystems that do not support UNIX modes.
        return


def _run_openssl(args: list[str], *, cwd: Path) -> None:
    cmd = ["openssl", *args]
    try:
        proc = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True)
    except FileNotFoundError as exc:
        raise EgressCAError("openssl is required to pre-generate runtime egress CA but was not found") from exc

    if proc.returncode != 0:
        stderr = (proc.stderr or "").strip()
        raise EgressCAError(f"openssl command failed ({' '.join(cmd)}): {stderr[:500]}")


def ensure_egress_ca(
    ca_dir: Path,
    *,
    common_name: str,
    days_valid: int = 3650,
    overwrite: bool = False,
) -> dict:
    """
    Ensures CA exists in ca_dir.
    Returns metadata dict with paths and a "created" bool.
    """
    ca_dir.mkdir(parents=True, exist_ok=True)

    cert_path = ca_dir / "egress-ca.crt"
    key_path = ca_dir / "egress-ca.key"
    mitm_cert_path = ca_dir / "mitmproxy-ca-cert.pem"
    mitm_bundle_path = ca_dir / "mitmproxy-ca.pem"
    openssl_conf = ca_dir / "openssl.cnf"

    created = overwrite
    if not overwrite and cert_path.exists() and key_path.exists():
        created = False
    else:
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

        _run_openssl(["genrsa", "-out", str(key_path), "4096"], cwd=ca_dir)
        _set_private_key_mode(key_path)
        _run_openssl(
            [
                "req",
                "-x509",
                "-new",
                "-nodes",
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

    shutil.copyfile(cert_path, mitm_cert_path)
    _write_bundle(cert_path, key_path, mitm_bundle_path)
    _set_private_key_mode(key_path)

    return {
        "created": created,
        "common_name": common_name,
        "egress_ca_crt": str(cert_path),
        "egress_ca_key": str(key_path),
        "mitmproxy_ca_pem": str(mitm_bundle_path),
        "mitmproxy_ca_cert_pem": str(mitm_cert_path),
    }


def normalize_custom_ca(ca_dir: Path, *, cert_path: Path, key_path: Path) -> dict:
    """Copy user-provided cert/key into canonical runtime CA paths."""
    ca_dir.mkdir(parents=True, exist_ok=True)

    out_cert = ca_dir / "egress-ca.crt"
    out_key = ca_dir / "egress-ca.key"
    out_mitm_cert = ca_dir / "mitmproxy-ca-cert.pem"
    out_bundle = ca_dir / "mitmproxy-ca.pem"

    if not cert_path.exists():
        raise EgressCAError(f"custom CA certificate path does not exist: {cert_path}")
    if not key_path.exists():
        raise EgressCAError(f"custom CA key path does not exist: {key_path}")

    shutil.copyfile(cert_path, out_cert)
    shutil.copyfile(key_path, out_key)
    shutil.copyfile(out_cert, out_mitm_cert)
    _write_bundle(out_cert, out_key, out_bundle)
    _set_private_key_mode(out_key)

    return {
        "created": True,
        "common_name": "custom",
        "egress_ca_crt": str(out_cert),
        "egress_ca_key": str(out_key),
        "mitmproxy_ca_pem": str(out_bundle),
        "mitmproxy_ca_cert_pem": str(out_mitm_cert),
    }
