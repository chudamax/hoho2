# Honeypot Specification (v1)

> Historical name: "Pack Spec". Terminology now prefers **honeypot**.

## File + location
- Canonical file name: `honeypot.yaml`.
- Canonical path: `honeypots/{high,low}/<honeypot_id>/honeypot.yaml`.
- YAML is the standard format (`.yaml` / `.yml`). JSON input is still accepted by CLI when provided directly.

## Common top-level fields
- `apiVersion`: `hoho.dev/v1`
- `kind`: `HoneypotPack`
- `metadata`: includes `id`, `name`, `interaction`, `tags`, `description`
- `storage`: currently `backend: filesystem` + `root`
- `limits`: request/body/artifact limits
- `telemetry`: event emission + redaction controls
- `sensors`: optional for both low and high interaction honeypots

## Layout constraints
- `metadata.id` MUST match the folder name `<honeypot_id>`.
- Local relative paths in YAML must resolve inside the same honeypot folder.

## Low-interaction fields
- `listen`
- `responses` (optional)
- `behaviors`
- optional `sensors` that attach to the implicit runtime service named `honeypot`

## High-interaction fields
- `stack.runtime`
- `stack.services`
- optional `sensors`

## Validation rules
Schema validation runs first, then semantic checks:
- low interaction honeypots require `behaviors`
- high interaction honeypots require `stack`
- sensor attachment targets must exist:
  - high: targets must exist in `stack.services`
  - low: implicit service name `honeypot` is valid for sensor attachments

## Env compatibility note
Existing env naming is retained for compatibility:
- `HOHO_PACK_ID == honeypot_id`
