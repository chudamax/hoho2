# Telemetry Forwarding

When `telemetry.forwarding.enabled: true`, compose adds `telemetry-forwarder`.

The forwarder:
- tails `run/artifacts/<honeypot_id>/index/events.jsonl`
- uploads missing blobs (`HEAD` then `PUT /api/v1/blobs/{sha}`)
- posts events to `POST /api/v1/events`
- persists cursor at `index/forwarder.cursor`

## Global .env
Use one shared env file at `honeypot-platform/.env`.

Variables:
- `HOHO_HUB_URL`
- `HOHO_HUB_TOKEN`
- `HOHO_FORWARD_FILTERS_JSON`

Template:
```bash
cp honeypot-platform/.env.example honeypot-platform/.env
```

`hoho` automatically loads `honeypot-platform/.env` and forwards it to docker compose with `--env-file` by default.

Override with:
```bash
hoho --env-file /path/to/custom.env run honeypots/high/<honeypot_id>/honeypot.yaml
```

## Pack contract example
```yaml
telemetry:
  forwarding:
    enabled: true
    hub_url: "${HOHO_HUB_URL}"
    token_env: "HOHO_HUB_TOKEN"
```
