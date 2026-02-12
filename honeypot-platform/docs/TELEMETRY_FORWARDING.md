# Telemetry Forwarding

When `telemetry.forwarding.enabled: true`, compose adds `telemetry-forwarder`.

The forwarder:
- tails `run/artifacts/<honeypot_id>/index/events.jsonl`
- uploads missing blobs (`HEAD` then `PUT /api/v1/blobs/{sha}`)
- posts events to `POST /api/v1/events`
- persists cursor at `index/forwarder.cursor`

Environment:
- `HOHO_HUB_URL`
- `HOHO_HUB_TOKEN`
- `HOHO_FORWARD_FILTERS_JSON`
