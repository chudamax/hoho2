# Runbook: low-interaction honeypot from CVE

## Required layout (Simple Layout v1)
Follow `honeypot-platform/docs/DIRECTORY_LAYOUT.md`.

- Pack YAML: `honeypot-platform/packs/low/<honeypot_id>.yaml`
- Pack assets (optional): `honeypot-platform/packs/low/<honeypot_id>/**`
- Operator doc: `honeypot-platform/honeypots/low/<honeypot_id>/README.md`
- Compose output: `honeypot-platform/deploy/compose/<honeypot_id>/docker-compose.yml`
- Artifacts: `honeypot-platform/run/artifacts/<honeypot_id>/...`

## Forbidden
- Do not create `run/artifacts/<runs-subtree>/**`.
- Do not create Markdown files in `honeypot-platform/packs/**`.
- Do not use extra identifiers (`pack_id`, `run_id`) in filesystem paths.

## Workflow
1. Research CVE protocol surface and request patterns.
2. Derive safe request transcripts and matching logic.
3. Implement low-interaction YAML at `packs/low/<honeypot_id>.yaml`.
4. Document operator steps at `honeypots/low/<honeypot_id>/README.md`.
5. Validate and run.

## Working example (recommended to read first)
Low-interaction reference pack:
- [`cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce.yaml`](../../packs/low/cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce.yaml)



## Validation
From repo root:

```bash
PYTHONPATH=honeypot-platform/packages/hoho_core:honeypot-platform/packages/hoho_runtime \
  python -m hoho_runtime.cli validate honeypot-platform/packs/low/<honeypot_id>.yaml
```

## Why output overwrites
Simple Layout v1 keeps one active artifact location per honeypot. A new run overwrites `run/artifacts/<honeypot_id>/` and compose output for the same `honeypot_id`.

Operational guidance:
- Stop existing process before restart.
- Clear `run/artifacts/<honeypot_id>/` before the next run.
- Do not run two copies of the same honeypot concurrently.

