# Pack Specification (v1)

## File Format
- Pack files are real YAML (`.yaml`/`.yml`), parsed with YAML semantics.
- JSON packs (`.json`) are also accepted.

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
- `sensors`: sensor descriptors with `name`, `type`, `config`, and `attach`.

## Sensor Config + Attach Semantics
### `fsmon`
```yaml
- name: fsmon-sensor
  type: fsmon
  config:
    watch:
      - /var/www/html
      - /var/www/html/wp-content/uploads
    allow_globs: ["**"]
    deny_globs: ["**/cache/**"]
    max_bytes: 262144
  attach:
    service: web
```
- `attach.service` is required.
- **Important:** fsmon sidecars can only see files from shared volumes/binds. Each watched path must be covered by a mount in the attached service, or compose rendering fails.

### `proxy`
```yaml
- name: proxy-sensor
  type: proxy
  config:
    upstream: http://web:80
    listen_port: 8080
  attach:
    service: web
```
- `config.upstream` is required.
- `listen_port` defaults to `8080`.
- Port fronting rule: if attached service publishes host ports, renderer moves published ports from the app service to the proxy service, mapping to the proxy listen port.

### `pcap`
```yaml
- name: pcap-sensor
  type: pcap
  config:
    interface: any
    rotate_seconds: 60
    rotate_count: 10
  attach:
    service: proxy-sensor
```
- Prefer `attach.service` for true sidecar behavior (`network_mode: service:<name>`).
- Optional `attach.network` is supported for network joins when service sidecar mode is not used.

## Validation Rules
Schema validation is run first (shape/types). Semantic checks run after schema validation and enforce interaction-specific requirements:
- low interaction packs require `behaviors`
- high interaction packs require `stack`
