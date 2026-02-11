# DIRECTORY_LAYOUT.md

## Canonical Layout (one honeypot = one folder)

All honeypot source-of-truth files live together under:

- `honeypot-platform/honeypots/high/<honeypot_id>/`
- `honeypot-platform/honeypots/low/<honeypot_id>/`

Each honeypot folder must contain:
- `honeypot.yaml`
- `README.md`

Optional supporting assets referenced by `honeypot.yaml` must stay inside the same folder.

## Deprecated layout

`honeypot-platform/packs/` is deprecated. Existing files may be kept temporarily for compatibility, but new honeypot definitions must not be added there.

## Generated output (never committed)
- Compose: `honeypot-platform/deploy/compose/<honeypot_id>/docker-compose.yml` (overwritten)
- Artifacts: `honeypot-platform/run/artifacts/<honeypot_id>/**` (overwritten)

## MUST rules
- MUST use `honeypot_id` as the only filesystem identifier.
- MUST set `metadata.id == <honeypot_id>` in `honeypot.yaml`.
- MUST keep docs in `honeypots/{low,high}/<honeypot_id>/README.md`.
- MUST keep referenced local file paths relative and inside the same honeypot folder.
- MUST render compose to `deploy/compose/<honeypot_id>/docker-compose.yml`.
- MUST write artifacts to `run/artifacts/<honeypot_id>/...`.

## MUST NOT rules
- MUST NOT create `run/artifacts/<runs-subtree>/**`.
- MUST NOT create non-canonical honeypot folders (example forbidden: `honeypots/high/2021-41773_42013/`).
- MUST NOT commit generated compose files under `honeypots/**`.
- MUST NOT add new honeypot YAML files under `packs/`.

## Compatibility invocation styles
- `hoho run honeypot-platform/honeypots/high/<id>`
- `hoho run honeypot-platform/honeypots/high/<id>/honeypot.yaml`
- `hoho run honeypot-platform/packs/high/<old>.yaml` (supported with deprecation warning)

## Overwrite warning
Simple layout has no run isolation. Running the same `honeypot_id` again overwrites `deploy/compose/<honeypot_id>/` and `run/artifacts/<honeypot_id>/`.
