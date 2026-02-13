# HOHO Hub

Hub lives under `honeypot-platform/hub/` and provides:
- ingest APIs for events/blobs
- SPA web GUI for browsing honeypots/sessions/events/files
- live events via SSE
- blob downloads by sha256
- blob file type detection metadata (libmagic-based)

## Global .env
Use the shared env file at `honeypot-platform/.env` for hub + shipper.

Common vars:
- `HOHO_HUB_URL`
- `HOHO_HUB_TOKEN` (optional; empty disables auth)

Create it from template:
```bash
cp honeypot-platform/.env.example honeypot-platform/.env
```

## Start/stop hub (recommended)
From repo root:
```bash
hoho hub up
hoho hub logs
hoho hub down
```

## UI and API
- UI: `http://localhost:8000/ui/`
- `/` redirects to `/ui/`
- Live stream endpoint: `/api/v1/stream/events`

### File type detection metadata
Blob metadata is stored in `blob_meta` (SQLite), keyed by blob SHA256 and reused across artifacts.

Metadata fields:
- `detected_desc` (human-readable file-style description)
- `detected_mime`
- `guessed_ext`

Artifacts API (`/api/v1/artifacts`) includes these fields, and supports `detected_mime_prefix=` filtering.

Optional blob metadata endpoint:
- `GET /api/v1/blobs/{sha}/meta`

Env flags:
- `HOHO_HUB_FILETYPE_DETECT` (default `1`)
- `HOHO_HUB_FILETYPE_DETECT_MAX_BYTES` (default `262144`)
- `HOHO_HUB_FILETYPE_LAZY` (default `0`; if `1`, detect on first read instead of upload)
- `HOHO_HUB_FILETYPE_BACKFILL` (default `0`; startup backfill)
- `HOHO_HUB_FILETYPE_BACKFILL_LIMIT` (default `100`; max blobs per startup)

Detection failures never fail blob upload; hub logs warning and continues.

## Local dev workflow
Run the API:
```bash
cd honeypot-platform/hub
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Run SPA dev server with proxy:
```bash
cd honeypot-platform/hub/webui
npm install
npm run dev
```

The Vite dev proxy forwards `/api` and `/blobs` to `http://localhost:8000`.

## Alternative raw compose command
```bash
docker compose --env-file honeypot-platform/.env \
  -f honeypot-platform/hub/docker-compose.yml up --build
```

`honeypot-platform/hub/docker-compose.yml` reads token from `HOHO_HUB_TOKEN` with empty fallback.
