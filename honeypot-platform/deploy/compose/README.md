# Compose output directory

By default, `hoho` writes compose bundles under `<project_root>/deploy/compose/<honeypot_id>/`.

When `-o/--output` is not provided, the CLI discovers `project_root` by walking up from the honeypot definition path and selecting:
1. the first ancestor containing `deploy/compose` (or `deploy/compose/README.md`),
2. otherwise the first ancestor containing `honeypots/` or `packs/`,
3. otherwise the definition file's parent directory.

If `-o/--output` is provided, `hoho` keeps existing behavior and uses that path as given.


## Runtime egress MITM CA

For high-interaction stacks using the egress proxy with TLS MITM + CA install enabled, `hoho run` now pre-generates (or reuses) a host-side runtime CA before `docker compose up`:

- `deploy/compose/<honeypot_id>/runtime/ca/egress-ca.crt`
- `deploy/compose/<honeypot_id>/runtime/ca/egress-ca.key`
- `deploy/compose/<honeypot_id>/runtime/ca/mitmproxy-ca.pem` (combined cert + key)
- `deploy/compose/<honeypot_id>/runtime/ca/mitmproxy-ca-cert.pem` (cert only)

Attached services mount `runtime/ca/egress-ca.crt` at `/hoho/ca/egress-ca.crt`, and the egress proxy mounts `runtime/ca` and uses those files in custom CA mode so all services trust and interception use the same CA material.
