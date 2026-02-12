# Telemetry Shipping

Honeypots always write telemetry locally under `run/artifacts/<honeypot_id>/`.

## Flow
1. Sensors/runtime append events to `index/events.jsonl`.
2. Artifacts are stored under `blobs/<sha_prefix>/<sha256>`.
3. `hoho ship` reads local artifacts and uploads blobs/events to HOHO Hub.

## Start Hub
```bash
cp honeypot-platform/.env.example honeypot-platform/.env
hoho hub up
```

## Ship events
Tail mode (default):
```bash
hoho ship --follow
```

One-shot mode:
```bash
hoho ship --once --honeypot <honeypot_id>
```

## Environment
- `HOHO_HUB_URL` (required unless passed as `--hub-url`)
- `HOHO_HUB_TOKEN` (optional if hub auth disabled)
- `HOHO_FORWARD_FILTERS_JSON` (optional global forward filter rules)

`hoho` loads `honeypot-platform/.env` automatically unless `--no-env` is used.

## Cursor behavior
- Per honeypot cursor: `run/artifacts/<honeypot_id>/index/shipper.cursor`
- Back-compat: if `forwarder.cursor` exists and `shipper.cursor` does not, shipper initializes from `forwarder.cursor`.
- Cursor advances only after a successful event POST.
