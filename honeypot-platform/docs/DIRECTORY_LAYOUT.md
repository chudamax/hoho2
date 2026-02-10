# DIRECTORY_LAYOUT.md

## Simple Layout v1 (authoritative)

### Source packs (YAML only)
- `honeypot-platform/packs/low/<honeypot_id>.yaml`
- `honeypot-platform/packs/high/<honeypot_id>.yaml`

Optional assets (only if required):
- `honeypot-platform/packs/low/<honeypot_id>/**`
- `honeypot-platform/packs/high/<honeypot_id>/**`

### Operator docs/scripts
- `honeypot-platform/honeypots/low/<honeypot_id>/README.md`
- `honeypot-platform/honeypots/high/<honeypot_id>/README.md`
- `honeypot-platform/honeypots/high/<honeypot_id>/reset.sh` (recommended)

### Generated output (never committed)
- Compose: `honeypot-platform/deploy/compose/<honeypot_id>/docker-compose.yml` (overwritten)
- Artifacts: `honeypot-platform/run/artifacts/<honeypot_id>/**` (overwritten)

## MUST rules
- MUST use `honeypot_id` as the only filesystem identifier.
- MUST set `metadata.id == <honeypot_id>` in the corresponding YAML.
- MUST keep packs as `.yaml` files under `packs/{low,high}`.
- MUST keep human docs under `honeypots/{low,high}/<honeypot_id>/README.md`.
- MUST render compose to `deploy/compose/<honeypot_id>/docker-compose.yml`.
- MUST write artifacts to `run/artifacts/<honeypot_id>/...`.
- MUST overwrite compose + artifacts in place for each run.

## MUST NOT rules
- MUST NOT create `run/artifacts/<runs-subtree>/**`.
- MUST NOT create Markdown beside pack YAML files (`packs/**/*.md`).
- MUST NOT commit generated compose files under `honeypots/**`.
- MUST NOT create folders that differ from `honeypot_id` (example forbidden: `honeypots/high/2021-41773_42013/`).

## Naming
- Recommended `honeypot_id` format: `cve-YYYY-NNNN` or `cve-YYYY-NNNN_YYYY-NNNN`.
- Examples:
  - `cve-2021-41773_42013`
  - `cve-2020-25213`

## Overwrite warning
Simple Layout v1 has **no run isolation**. Operators must not run two copies of the same honeypot concurrently. Starting a new run for a honeypot overwrites prior artifacts and compose output for that `honeypot_id`.

Operational guidance:
- Stop existing compose project first.
- Clear `run/artifacts/<honeypot_id>/` before new runs.
- Use per-honeypot reset scripts for consistent restart behavior.

## Examples

Low interaction:
- Pack: `honeypot-platform/packs/low/cve-2020-25213.yaml`
- README: `honeypot-platform/honeypots/low/cve-2020-25213/README.md`
- Artifacts: `honeypot-platform/run/artifacts/cve-2020-25213/`

High interaction:
- Pack: `honeypot-platform/packs/high/cve-2021-41773_42013.yaml`
- README: `honeypot-platform/honeypots/high/cve-2021-41773_42013/README.md`
- Compose: `honeypot-platform/deploy/compose/cve-2021-41773_42013/docker-compose.yml`
- Artifacts: `honeypot-platform/run/artifacts/cve-2021-41773_42013/`
