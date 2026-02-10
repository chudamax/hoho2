# Deployment

## Quickstart: Low-Interaction Pack
1. Validate pack:
   - `hoho validate packs/low/example_web.yaml`
2. Run runtime:
   - `hoho run packs/low/example_web.yaml`
3. Send traffic to configured listen port.
4. Inspect `run/artifacts/<pack_id>/index/events.jsonl` and `blobs/`.

## Quickstart: High-Interaction Pack (simple render mode)
1. Validate pack:
   - `hoho validate packs/high/example_wp_stack.yaml`
2. Render compose bundle:
   - `hoho render-compose packs/high/example_wp_stack.yaml`
3. Start stack:
   - `docker compose -f deploy/compose/example-wp-stack/docker-compose.yml up -d`
4. Artifacts land on host under:
   - `run/artifacts/example-wp-stack/...`

## Quickstart: High-Interaction Pack (`hoho run`, isolated)
1. Start run:
   - `hoho run packs/high/example_wp_stack.yaml`
2. `hoho run` prints JSON with `pack_id`, `run_id`, `artifacts_host_path`, `compose_file`, `project_name`.
3. Artifacts land on host under:
   - `run/artifacts/runs/<run_id>/example-wp-stack/...`

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

## Multi-instance verification helpers
After starting isolated runs with `hoho run`:

```bash
# find the newest run
ls -1dt run/artifacts/runs/* | head -n1

# tail events
tail -n 20 run/artifacts/runs/<run_id>/example-wp-stack/index/events.jsonl

# list blobs
find run/artifacts/runs/<run_id>/example-wp-stack/blobs -type f | head
```

## Generated Output Policy
- `deploy/compose/**` is generated output from `hoho render-compose` and should not be committed.
- Runtime artifacts under `run/artifacts/**` are also generated and ignored.
- Keep only `deploy/compose/README.md` tracked as documentation for this build-output directory.

## Recommended Isolation
- Use dedicated network segments for honeypot exposure.
- Restrict outbound egress from honeypot and sensor networks.
- Run with non-privileged users wherever possible.
- Mount artifact storage on isolated volumes with monitoring.
