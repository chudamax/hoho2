# Pack Specification (v1)

## Common Top-Level Fields
- `apiVersion`: must be `hoho.dev/v1`.
- `kind`: must be `HoneypotPack`.
- `metadata`: includes `id`, `name`, `interaction`, `tags`, and `description`.
- `storage`: currently `backend: filesystem` and `root` path.
- `limits`: `max_body_bytes`, `max_upload_bytes`, and `max_artifacts_per_request`.
- `telemetry`: `emit_events`, `redact_headers`, and optional query redaction list.

## Low-Interaction Fields
- `listen`: list of `{host, port}` entries.
- `responses`: optional reusable response templates.
- `behaviors`: ordered rules with `name`, `match`, `actions`, and optional `respond`.

## High-Interaction Fields
- `stack.runtime`: `compose` for v1.
- `stack.services`: compose-like service map (`image/build`, environment, volumes, networks, ports).
- `sensors`: shared sensor descriptors with `name`, `type`, `config`, and `attach` mapping.
- `expose`: optional shortcut metadata for published ports.

## Validation Rules
Schema validation enforces required fields and interaction mode options. Semantic checks ensure low packs include behaviors and high packs include a stack section.
