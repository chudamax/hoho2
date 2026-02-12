# Deployment

## Quickstart (low + high)
1. Validate honeypot:
   - `hoho validate honeypots/{low,high}/<honeypot_id>/honeypot.yaml`
2. Render compose:
   - `hoho render-compose honeypots/{low,high}/<honeypot_id>/honeypot.yaml`
3. Start stack:
   - `hoho run honeypots/{low,high}/<honeypot_id>/honeypot.yaml`
4. Inspect artifacts:
   - `run/artifacts/<honeypot_id>/index/events.jsonl`
   - `run/artifacts/<honeypot_id>/blobs/`

## Global .env for telemetry forwarding
- Global environment file path: `honeypot-platform/.env`
- Recommended bootstrap:
  - `cp honeypot-platform/.env.example honeypot-platform/.env`
- Variables:
  - `HOHO_HUB_URL`
  - `HOHO_HUB_TOKEN`

`hoho` auto-loads `honeypot-platform/.env` by default and also passes it to Docker Compose with `--env-file` so `${HOHO_HUB_URL}` and `${HOHO_HUB_TOKEN}` interpolate consistently.

Override examples:
- `hoho --env-file /path/to/custom.env run honeypots/high/<honeypot_id>/honeypot.yaml`
- `hoho --no-env run honeypots/high/<honeypot_id>/honeypot.yaml`

## Low interaction runtime mode
- `hoho run` defaults to `--mode container` for both low and high interaction honeypots.
- For low-interaction debugging only, host mode is still available:
  - `hoho run honeypots/low/<honeypot_id>/honeypot.yaml --mode host`

## Multi-honeypot operation
- Each run uses compose project name `hoho-<honeypot_id>`.
- Multiple honeypots can run in parallel when `honeypot_id` differs.
- Keep only one active stack per `honeypot_id`.

## Notes
- `deploy/compose/**` is generated and should not be committed.
- `run/artifacts/<honeypot_id>/` is overwritten for each new run of the same honeypot.
- `HOHO_PACK_ID` remains the runtime env variable name and aliases `honeypot_id`.
