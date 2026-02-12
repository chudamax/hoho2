# Sensors

## Shared Contract
All sensors read common environment variables:
- `HOHO_PACK_ID` (legacy name; value equals `honeypot_id`)
- `HOHO_STORAGE_BACKEND=filesystem`
- `HOHO_STORAGE_ROOT=/artifacts`

`/artifacts` is a sensor/container mountpoint mapped to host `<storage.root>`.

Sensors append canonical events to `<root>/<honeypot_id>/index/events.jsonl` and write artifacts as content-addressed blobs.

## Attach model for low and high
- High interaction: attach to named services in `stack.services`.
- Low interaction: attach to the implicit runtime service named `honeypot`.

Example (low + sensors):
```yaml
sensors:
  - name: proxy-sensor
    type: proxy
    attach:
      service: honeypot
    config:
      upstream: http://honeypot:8088
  - name: pcap-sensor
    type: pcap
    attach:
      service: honeypot
```

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
- Output is written under the honeypot artifacts tree (for example `run/artifacts/<honeypot_id>/...`).

Runtime env used by renderer:
- `PCAP_ROTATE_SECONDS`
- `PCAP_ROTATE_COUNT`
- `PCAP_INTERFACE`

## Egress Proxy Sensor
- Runs mitmproxy in explicit forward-proxy mode.
- Emits `sensor.egress_proxy.http` per flow with request/response metadata and redacted headers.
- Supports response-body capture with `capture.bodies: "*"` (default) or metadata-only with `"none"`.
- Persists mitmproxy confdir under artifacts (`run/artifacts/<id>/mitmproxy-conf/`).
- With `tls_mitm.enabled: true`, `hoho run` generates a runtime CA in compose runtime dir before startup.
- Runtime can execute `/hoho/ca/install-ca.sh` in attached services and emits `system.ca_install.succeeded` / `system.ca_install.failed` events.

## Operational Notes
Disk usage can grow quickly from uploads and pcap segments. Use external rotation, retention cleanup, and dedicated storage volumes.


## Falco Sensor
- High-interaction runtime behavior telemetry via Falco (process execution, shells, downloaders, network tools, interpreters).
- Renderer starts `falco-sensor` as privileged (MVP) with Modern eBPF engine by default.
- Default Hoho Falco rules are shipped in the image under `/app/rules/hoho_rules.yaml`.
- `any_exec: true` appends an additional noisy default rules file from `/app/rules/hoho_any_exec.yaml`.
- Falco writes one-line JSON alerts to a long-running forwarder via `program_output`.
- Forwarder emits `sensor.falco` canonical events to `<storage.root>/<honeypot_id>/index/events.jsonl`.
- Alerts are scoped to this compose stack by checking Docker labels (`com.docker.compose.project == hoho-<honeypot_id>`), with optional `attach.services` filtering.
- `sensors[].config.rules` adds extra rule files/overrides loaded after image defaults.
- Optional enforcement can stop offending container/service/stack and emit a corresponding enforcement event.
- Required mounts include `/sys/kernel/tracing`, `/proc`, `/etc`, and docker socket (`/var/run/docker.sock`) from host.

## Telemetry v2 additions
- All sensors emit `schema_version: 2` with `honeypot_id`, `session_id`, `agent_id`, and `event_name`.
- Runtime injects `HOHO_SESSION_ID`, `HOHO_AGENT_ID`, `HOHO_EMIT_FILTERS_JSON`, and `HOHO_FORWARD_FILTERS_JSON` into services/sensors.
- Optional forwarding uses telemetry-forwarder + hub token auth.
