# Runbook: high-interaction honeypot from CVE

## Required layout
- Honeypot folder: `honeypot-platform/honeypots/high/<honeypot_id>/`
- Definition: `honeypot-platform/honeypots/high/<honeypot_id>/honeypot.yaml`
- Docs: `honeypot-platform/honeypots/high/<honeypot_id>/README.md`
- Optional assets/scripts: under same honeypot folder
- Compose output: `honeypot-platform/deploy/compose/<honeypot_id>/docker-compose.yml`
- Artifacts: `honeypot-platform/run/artifacts/<honeypot_id>/...`

## Workflow
1. Research target CVE and vulnerable stack.
2. Build `honeypot.yaml` under `honeypots/high/<honeypot_id>/`.
3. Add sensors for proxy/fsmon/pcap (plus egress_proxy when needed). 
4. When configuring fsmon watch_paths, always include common world-writable temp locations (/tmp, /var/tmp) plus the app's most likely writable/content directories
5. Write `README.md` (+ `reset.sh` if useful).
6. Validate, render compose, and run.

## Validation and run
```bash
PYTHONPATH=honeypot-platform/packages/hoho_core:honeypot-platform/packages/hoho_runtime \
  python -m hoho_runtime.cli validate honeypot-platform/honeypots/high/<honeypot_id>/honeypot.yaml

PYTHONPATH=honeypot-platform/packages/hoho_core:honeypot-platform/packages/hoho_runtime \
  python -m hoho_runtime.cli render-compose honeypot-platform/honeypots/high/<honeypot_id>/honeypot.yaml

PYTHONPATH=honeypot-platform/packages/hoho_core:honeypot-platform/packages/hoho_runtime \
  python -m hoho_runtime.cli run honeypot-platform/honeypots/high/<honeypot_id>
```
