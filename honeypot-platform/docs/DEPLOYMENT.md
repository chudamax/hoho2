# Deployment

## Quickstart: Low-Interaction Pack
1. Validate pack:
   - `hoho validate packs/low/example_web.yaml`
2. Run runtime:
   - `hoho run packs/low/example_web.yaml`
3. Send traffic to configured listen port.
4. Inspect `run/artifacts/<pack_id>/index/events.jsonl` and `blobs/`.

## Quickstart: High-Interaction Pack
1. Validate pack.
2. Render compose bundle:
   - `hoho render-compose packs/high/example_wp_stack.yaml`
3. Optionally start stack:
   - `docker compose -f deploy/compose/example-wp-stack/docker-compose.yml up`

## Recommended Isolation
- Use dedicated network segments for honeypot exposure.
- Restrict outbound egress from honeypot and sensor networks.
- Run with non-privileged users wherever possible.
- Mount artifact storage on isolated volumes with monitoring.
