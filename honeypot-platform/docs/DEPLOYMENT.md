# Deployment

## High-interaction quickstart
1. Validate pack:
   - `hoho validate packs/high/<honeypot_id>.yaml`
2. Render compose (fixed output path):
   - `hoho render-compose packs/high/<honeypot_id>.yaml`
3. Start stack:
   - `docker compose -p "hoho-<honeypot_id>" -f deploy/compose/<honeypot_id>/docker-compose.yml up -d`
4. Inspect artifacts:
   - `run/artifacts/<honeypot_id>/index/events.jsonl`
   - `run/artifacts/<honeypot_id>/blobs/`

## Notes
- `deploy/compose/**` is generated and should not be committed.
- `run/artifacts/<honeypot_id>/` is overwritten for each new run of the same honeypot.
- Run only one active stack per `honeypot_id`.
