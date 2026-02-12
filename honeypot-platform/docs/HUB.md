# HOHO Hub

Hub lives under `honeypot-platform/hub/` and provides:
- ingest APIs for events/blobs
- lightweight HTML pages for browsing honeypots/sessions/events
- blob downloads by sha256

Run with:
```bash
docker compose -f honeypot-platform/hub/docker-compose.yml up --build
```
