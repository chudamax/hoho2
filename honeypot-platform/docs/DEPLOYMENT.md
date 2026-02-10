# Deployment

## Quickstart: Low-Interaction Pack
1. Validate pack:
   - `hoho validate packs/low/example_web.yaml`
2. Run runtime:
   - `hoho run packs/low/example_web.yaml`
3. Send traffic to configured listen port.
4. Inspect `run/artifacts/<pack_id>/index/events.jsonl` and `blobs/`.

## Quickstart: High-Interaction Pack
1. Validate pack:
   - `hoho validate packs/high/example_wp_stack.yaml`
2. Render compose bundle:
   - `hoho render-compose packs/high/example_wp_stack.yaml`
3. Start stack:
   - `docker compose -f deploy/compose/example-wp-stack/docker-compose.yml up`

## Smoke Commands (high interaction)
From `honeypot-platform/`:
1. Render:
   - `hoho render-compose packs/high/example_wp_stack.yaml`
2. Bring up:
   - `docker compose -f deploy/compose/example-wp-stack/docker-compose.yml up -d`
3. Generate traffic:
   - `curl -i http://127.0.0.1:8088/`
4. Trigger fsmon via watched volume-backed path:
   - `docker compose -f deploy/compose/example-wp-stack/docker-compose.yml exec web sh -lc 'echo test > /var/www/html/wp-content/uploads/probe.txt'`
5. Verify artifacts/events:
   - `tail -n 50 run/artifacts/example-wp-stack/index/events.jsonl`

## Generated Output Policy
- `deploy/compose/**` is generated output from `hoho render-compose` and should not be committed.
- Runtime artifacts under `run/artifacts/**` are also generated and ignored.
- Keep only `deploy/compose/README.md` tracked as documentation for this build-output directory.

## Recommended Isolation
- Use dedicated network segments for honeypot exposure.
- Restrict outbound egress from honeypot and sensor networks.
- Run with non-privileged users wherever possible.
- Mount artifact storage on isolated volumes with monitoring.
