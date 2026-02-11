# Runbook: low-interaction honeypot from CVE

## Required layout
- Honeypot folder: `honeypot-platform/honeypots/low/<honeypot_id>/`
- Definition: `honeypot-platform/honeypots/low/<honeypot_id>/honeypot.yaml`
- Docs: `honeypot-platform/honeypots/low/<honeypot_id>/README.md`
- Compose output: `honeypot-platform/deploy/compose/<honeypot_id>/docker-compose.yml`
- Artifacts: `honeypot-platform/run/artifacts/<honeypot_id>/...`

## Workflow
1. Research CVE protocol surface and request patterns.
2. Implement `honeypot.yaml` at `honeypots/low/<honeypot_id>/`.
3. Document operation in `README.md`.
4. Validate and run.

## Validation and run
```bash
PYTHONPATH=honeypot-platform/packages/hoho_core:honeypot-platform/packages/hoho_runtime \
  python -m hoho_runtime.cli validate honeypot-platform/honeypots/low/<honeypot_id>/honeypot.yaml

PYTHONPATH=honeypot-platform/packages/hoho_core:honeypot-platform/packages/hoho_runtime \
  python -m hoho_runtime.cli run honeypot-platform/honeypots/low/<honeypot_id>
```

## Compatibility note
`packs/low/*.yaml` invocation is temporarily supported with a deprecation warning.
