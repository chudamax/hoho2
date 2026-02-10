# Security

## Core Safety Statement
Captured payloads are treated as opaque bytes. The platform never executes, imports, or opens uploaded content as code.

## Safe Malware Handling
- Keep artifacts in isolated storage.
- Do not double-click or run captured binaries/scripts.
- Use offline analysis environments with strict controls.
- Preserve hashes and metadata for chain-of-custody.

## Network and Host Isolation
- Place honeypots in dedicated VLAN/VPC segments.
- Enforce firewall egress controls.
- Limit sensor and runtime privileges.
- Keep host patching and logging up to date.

## Operational Hardening
- Enable strict size limits to reduce resource abuse.
- Redact sensitive headers by default.
- Avoid shelling out with untrusted input.


## Egress Proxy + TLS MITM Safety
- Captured response bodies (including binaries) are untrusted and must be handled as malware-grade content.
- The generated MITM CA is honeypot-only; never reuse it in production or on analyst workstations.
- CA private key material remains inside the egress proxy container/artifacts confdir and is never mounted into target services.
