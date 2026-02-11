# Runbook: high-interaction honeypot from CVE

## Required layout (Simple Layout v1)
Follow `honeypot-platform/docs/DIRECTORY_LAYOUT.md`.

- Pack YAML: `honeypot-platform/packs/high/<honeypot_id>.yaml`
- Pack assets (optional): `honeypot-platform/packs/high/<honeypot_id>/**`
- Operator doc: `honeypot-platform/honeypots/high/<honeypot_id>/README.md`
- Reset script: `honeypot-platform/honeypots/high/<honeypot_id>/reset.sh`
- Compose output: `honeypot-platform/deploy/compose/<honeypot_id>/docker-compose.yml`
- Artifacts: `honeypot-platform/run/artifacts/<honeypot_id>/...`

## Capture priorities
- PCAP capture.
- HTTP proxy capture for downloads and request metadata.
- Filesystem monitoring.
- Process/audit telemetry where available.

## Forbidden
- Do not create `run/artifacts/<runs-subtree>/**`.
- Do not use run-isolated filesystem paths.
- Do not put Markdown files in `honeypot-platform/packs/**`.

## Workflow
1. Research target CVE and deployable vulnerable stack.\
2. Sometimes specifically vulnerable images for testing are available at hub.docker.com. Search for it.
3. Build high-interaction YAML at `packs/high/<honeypot_id>.yaml`.
4. Add sensors for pcap/proxy/fs monitoring.
5. Create `honeypots/high/<honeypot_id>/README.md` and `reset.sh`.
6. Validate, render compose, and run.

## Working example (recommended to read first)
High-interaction reference pack:
- [`cve-2021-41773_42013_apache_rce.yaml`](../../packs/high/cve-2021-41773_42013_apache_rce.yaml)


## Validation and run
From repo root:

```bash
PYTHONPATH=honeypot-platform/packages/hoho_core:honeypot-platform/packages/hoho_runtime \
  python -m hoho_runtime.cli validate honeypot-platform/packs/high/<honeypot_id>.yaml

PYTHONPATH=honeypot-platform/packages/hoho_core:honeypot-platform/packages/hoho_runtime \
  python -m hoho_runtime.cli render-compose honeypot-platform/packs/high/<honeypot_id>.yaml


docker compose -p "hoho-<honeypot_id>" \
  -f honeypot-platform/deploy/compose/<honeypot_id>/docker-compose.yml up -d
```

## Why output overwrites
Simple Layout v1 intentionally overwrites compose/artifacts in fixed per-honeypot locations.

Operational guidance:
- Only one active run per `honeypot_id`.
- Stop/down the previous compose stack before restarting.
- Clear `run/artifacts/<honeypot_id>/` before a new run.
