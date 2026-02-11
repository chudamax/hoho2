# AGENTS.md (repo root)

## Honeypot layout (Unified Layout v2)
Authoritative spec: `honeypot-platform/docs/DIRECTORY_LAYOUT.md`.

MUST:
- Always use `honeypot_id == metadata.id`.
- Create honeypots only at:
  - `honeypot-platform/honeypots/low/<honeypot_id>/honeypot.yaml`
  - `honeypot-platform/honeypots/high/<honeypot_id>/honeypot.yaml`
- Create docs only at `honeypot-platform/honeypots/{low,high}/<honeypot_id>/README.md`.
- Keep YAML-referenced local paths relative and inside the same honeypot folder.
- Artifacts always go to `honeypot-platform/run/artifacts/<honeypot_id>/...`.
- Compose output always goes to `honeypot-platform/deploy/compose/<honeypot_id>/docker-compose.yml`.

MUST NOT:
- Do not create `honeypot-platform/run/artifacts/<runs-subtree>/**` (no run-id subtrees).
- Do not create non-canonical honeypot folders (example forbidden: `honeypots/high/2021-41773_42013/`).
- Do not add new honeypot YAML definitions under `honeypot-platform/packs/`.

## Deprecated compatibility
- `honeypot-platform/packs/{low,high}/*.yaml` may still be invoked by CLI for one compatibility window.
- CLI should emit deprecation warnings for `packs/` paths.

## Docs that must be consulted (before implementing or changing honeypots)
- Spec + schema rules: `honeypot-platform/docs/PACK_SPEC.md`
- Sensor behavior + env contracts: `honeypot-platform/docs/SENSORS.md`
- Storage layout + overwrite semantics: `honeypot-platform/docs/STORAGE_LAYOUT.md`
- Deployment notes: `honeypot-platform/docs/DEPLOYMENT.md`
- Compose output notes (incl. egress CA paths): `honeypot-platform/deploy/compose/README.md`

## Runbooks (follow exactly)
Low-interaction:
- Always read: `honeypot-platform/docs/runbooks/low-interaction-honeypot-from-cve.md`

High-interaction:
- Always read: `honeypot-platform/docs/runbooks/high-interaction-honeypot-from-cve.md`

## High-interaction capture baseline (recommended)
For “high” stacks, default to maximum visibility:
- `http_proxy` (reverse proxy) for inbound request/response metadata and request body capture.
- `egress_proxy` (forward proxy) to capture **outbound** downloads (post-exploitation stage).
- `fsmon` to capture file writes in shared mounted paths.
- `pcap` for ground-truth network capture.

## Egress proxy sensor guidance (important)
Use `egress_proxy` when you want to capture attacker tooling fetched by the compromised container(s):
- It emits `sensor.egress_proxy.http` events.
- It can store response bodies as artifacts (`egress.response_body`) and also materialize symlinks under:
  `run/artifacts/<honeypot_id>/objects/<event_id>/egress.response/<filename>`
- With TLS MITM enabled, `hoho run` pre-generates a runtime CA under:
  `deploy/compose/<honeypot_id>/runtime/ca/`
  and the egress proxy exports the CA cert to:
  `run/artifacts/<honeypot_id>/ca/egress-ca.crt`
- If `tls_mitm.install_trust.enabled: true`, runtime executes `/hoho/ca/install-ca.sh` in attached services and emits:
  `system.ca_install.succeeded` / `system.ca_install.failed` events.

## Working reference honeypots (golden examples)
High-interaction:
- `honeypot-platform/honeypots/high/cve-2021-41773_42013_apache_rce/honeypot.yaml`

Low-interaction:
- `honeypot-platform/honeypots/low/cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce/honeypot.yaml`

## Operational commands (stop/cleanup)
- Stop everything: `hoho down-all` (optionally `--volumes`)
- Per-honeypot manual stop:
  `docker compose -p "hoho-<honeypot_id>" -f deploy/compose/<honeypot_id>/docker-compose.yml down -v`
