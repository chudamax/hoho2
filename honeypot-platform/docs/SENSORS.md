# Sensors

## Shared Contract
All sensors read common environment variables:
- `HOHO_PACK_ID`
- `HOHO_STORAGE_BACKEND=filesystem`
- `HOHO_STORAGE_ROOT=/artifacts`

`/artifacts` is a sensor/container mountpoint. The runtime maps it to a host path:
- Simple mode: `<storage.root>`
- Isolated run mode: `<storage.root>/runs/<run_id>`

Sensors append canonical events to `<root>/<pack_id>/index/events.jsonl` and write artifacts as content-addressed blobs.

## HTTP Proxy Sensor
- Built on mitmproxy reverse mode (`--mode reverse:<upstream>`).
- Captures request/response metadata and request body artifacts.
- Renderer joins proxy to attached service networks and applies fronting behavior:
  - Attached service published ports are removed.
  - Proxy publishes the same host ports to `listen_port` (default `8080`).

Runtime env used by renderer:
- `UPSTREAM` (required)
- `PROXY_LISTEN_PORT` (defaults to `8080`)
- `PROXY_LISTEN_HOST` (defaults to `0.0.0.0`)
- `PROXY_KEEP_HOST_HEADER` (`true`/`false`, defaults to `true`)

Troubleshooting redirects:
- Symptom: browser gets redirected to an internal compose DNS name (for example `http://web:8088/...`).
- Cause: reverse proxy rewrites `Host` by default unless `keep_host_header` is enabled.
- Fix: keep `PROXY_KEEP_HOST_HEADER=true` (default). Set it to `false` only when upstream behavior requires rewritten host headers.

## Filesystem Monitor Sensor
- Watches configured directories for create/modify events.
- Applies allow/deny glob filters.
- Stores changed file content up to a cap and records preview text.

Runtime env used by renderer:
- `FSMON_WATCH` (comma-separated absolute paths)
- `FSMON_ALLOW` (comma-separated globs, defaults to `*`)
- `FSMON_DENY` (comma-separated globs)
- `FSMON_MAX_BYTES` (optional)

Important: fsmon cannot inspect a target container root filesystem directly. Watch paths must be backed by mounts shared with the fsmon sidecar.

## PCAP Sensor
- Uses tcpdump with rotation controls.
- Sidecar mode (`attach.service`) uses `network_mode: service:<target>`.
- Network mode (`attach.network`) joins the named network.
- Renderer adds required capabilities:
  - `NET_ADMIN`
  - `NET_RAW`

Runtime env used by renderer:
- `PCAP_ROTATE_SECONDS`
- `PCAP_ROTATE_COUNT`
- `PCAP_INTERFACE` (currently emitted, may be ignored by entrypoint depending on image implementation)

## Operational Notes
Disk usage can grow quickly from uploads and pcap segments. Use external rotation, retention cleanup, and dedicated storage volumes.


## Egress Proxy Sensor
- Runs mitmproxy in explicit forward-proxy mode.
- Emits `sensor.egress_proxy.http` per flow with request/response metadata and redacted headers.
- Supports response-body capture with `capture.bodies: "*"` (default) or metadata-only with `"none"`.
- Persists mitmproxy confdir under artifacts and exports CA cert to `<artifacts>/<stack_id>/ca/egress-ca.crt`.
- Runtime can execute `/hoho/ca/install-ca.sh` in attached services after startup and emits `system.ca_install.succeeded` / `system.ca_install.failed` events.
- If trust install fails, HTTP capture still works; HTTPS may degrade to CONNECT-only visibility.
