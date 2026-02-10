# Sensors

## Shared Contract
All sensors read common environment variables:
- `HOHO_PACK_ID`
- `HOHO_STORAGE_BACKEND=filesystem`
- `HOHO_STORAGE_ROOT=/artifacts`
- `HOHO_EMIT_EVENTS=1`
- `HOHO_REDACT_HEADERS=Authorization,Cookie`

All sensors append canonical events to `<root>/<pack_id>/index/events.jsonl` and write artifacts as content-addressed blobs.

## HTTP Proxy Sensor
- Built on mitmproxy reverse mode (`--mode reverse:<upstream>`).
- Captures request/response metadata and request body artifacts.
- Supports deployment as sidecar in front of a target web service.

Compose snippet:
```yaml
proxy-sensor:
  image: hoho/sensor-http-proxy:latest
  environment:
    HOHO_PACK_ID: example
  volumes: ["artifacts:/artifacts"]
```

## Filesystem Monitor Sensor
- Watches configured directories for create/modify events.
- Applies allow/deny glob filters.
- Stores changed file content up to a cap and records preview text.

## PCAP Sensor
- Uses tcpdump with rotation controls (`-G`, `-W`, optional `-C`).
- Stores rotated pcap files as blob artifacts and emits `pcap_segment` events.

## Operational Notes
Disk usage can grow quickly from uploads and pcap segments. Use external rotation, retention cleanup, and dedicated storage volumes.
