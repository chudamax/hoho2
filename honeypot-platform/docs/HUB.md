# HOHO Hub

Hub lives under `honeypot-platform/hub/` and provides:
- ingest APIs for events/blobs
- lightweight HTML pages for browsing honeypots/sessions/events
- blob downloads by sha256

## Global .env
Use the shared env file at `honeypot-platform/.env` for hub + honeypot forwarding.

Required vars:
- `HOHO_HUB_URL`
- `HOHO_HUB_TOKEN`

Create it from template:
```bash
cp honeypot-platform/.env.example honeypot-platform/.env
```

Run hub from repo root:
```bash
docker compose --env-file honeypot-platform/.env \
  -f honeypot-platform/hub/docker-compose.yml up --build
```

`honeypot-platform/hub/docker-compose.yml` reads token from `HOHO_HUB_TOKEN` with fallback `changeme`.
