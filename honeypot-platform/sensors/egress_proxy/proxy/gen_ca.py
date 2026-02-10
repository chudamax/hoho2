#!/usr/bin/env python3
from __future__ import annotations

import sys
from datetime import UTC, datetime, timedelta
from pathlib import Path

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: gen_ca.py <conf_dir>", file=sys.stderr)
        return 2

    conf_dir = Path(sys.argv[1])
    conf_dir.mkdir(parents=True, exist_ok=True)

    now = datetime.now(UTC)
    subject = issuer = x509.Name(
        [
            x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, "hoho egress proxy"),
            x509.NameAttribute(NameOID.COMMON_NAME, "hoho mitm CA"),
        ]
    )

    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - timedelta(minutes=5))
        .not_valid_after(now + timedelta(days=3650))
        .add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
        .add_extension(
            x509.KeyUsage(
                digital_signature=True,
                key_encipherment=False,
                key_cert_sign=True,
                key_agreement=False,
                content_commitment=False,
                data_encipherment=False,
                encipher_only=False,
                decipher_only=False,
                crl_sign=True,
            ),
            critical=True,
        )
        .sign(private_key=key, algorithm=hashes.SHA256())
    )

    key_pem = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )
    cert_pem = cert.public_bytes(serialization.Encoding.PEM)

    (conf_dir / "mitmproxy-ca.pem").write_bytes(key_pem + cert_pem)
    (conf_dir / "mitmproxy-ca-cert.pem").write_bytes(cert_pem)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
