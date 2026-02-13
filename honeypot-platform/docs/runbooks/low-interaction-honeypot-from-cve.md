# Runbook: low-interaction honeypot from CVE

Low-interaction honeypots emulate vulnerable *request/response behavior* safely. They do **not** run the vulnerable software.

This runbook is written for coding agents and humans adding a new low-interaction honeypot under `honeypot-platform/honeypots/low/`.

---

## Required layout

- Honeypot folder: `honeypot-platform/honeypots/low/<honeypot_id>/`
- Definition: `honeypot-platform/honeypots/low/<honeypot_id>/honeypot.yaml`
- Docs: `honeypot-platform/honeypots/low/<honeypot_id>/README.md`
- Artifacts: `honeypot-platform/run/artifacts/<honeypot_id>/...` (overwritten)
- (Optional) Compose output: low interaction usually does *not* need compose, but the CLI may still render bundles into `deploy/compose/<honeypot_id>/` for consistency.

> The repo uses an overwrite-based storage layout. Re-running the same `<honeypot_id>` overwrites artifacts.

---

## Workflow

### 1) Research and scope
Collect stable, protocol-level signals (do not overfit):
- Target ports (80/443/8080/etc.)
- Paths/endpoints
- Encodings (double-encoding, dot-segments, traversal patterns)
- Typical response codes and headers
- Any request body patterns that are common (POST probes)

Decide **what you want to capture**:
- Always capture request metadata
- Capture request bodies only for high-signal requests (POST exploit probes)
- If the exploit uses file upload, capture multipart files (`store_multipart`) and enforce limits

### 2) Create folder + skeleton
Create:

- `honeypot-platform/honeypots/low/<honeypot_id>/honeypot.yaml`
- `honeypot-platform/honeypots/low/<honeypot_id>/README.md`

Minimal skeleton:

```yaml
apiVersion: hoho.dev/v1
kind: HoneypotPack
metadata:
  id: <honeypot_id>
  name: <Human readable name>
  interaction: low
  tags:
    - cve
    - cve:YYYY-NNNNN
    - product:<product>
    - technique:<technique>
  description: >
    <Short, operator-facing description>

storage:
  backend: filesystem
  root: ./run/artifacts

limits:
  max_body_bytes: 1048576
  max_upload_bytes: 10485760
  max_artifacts_per_request: 5

telemetry:
  emit_events: true
  redact_headers:
    - Authorization
    - Cookie

listen:
  - host: 0.0.0.0
    port: 8088
    protocol: http

responses:
  - name: landing_ok
    status: 200
    headers:
      Server: "nginx"
    body: "OK\n"

behaviors:
  - name: default_404
    match:
      pathGlob: "/**"
    then:
      - emit_event:
          verdict: unknown
          indicators: ["default"]
      - respond:
          response: landing_ok
```

### 3) Implement behaviors (matchers + actions)
Rules should be ordered: most specific first, then a safe default.

Recommended actions:
- `emit_event` with `verdict` + `indicators`
- `store_body` for selected POST probes (optionally gzip)
- `store_multipart` for file uploads
- `delay` with jitter for realism
- `respond` with plausible but minimal responses

Use stable matchers:
- `method`, `pathGlob`, `pathRegex`
- headers/query/body conditions only when they are stable across exploits
- do not rely only on User-Agent

### 4) Store attacker artifacts safely
If the CVE commonly involves:
- **POST command body** (e.g. CGI RCE probes): use `store_body` (gzip enabled) and cap sizes via `limits`.
- **File uploads**: use `store_multipart` and cap via `max_upload_bytes`.

Never “execute” anything. Treat all captured bytes as opaque.

### 5) Write README.md
README must include:
- What the honeypot emulates (and what it does not)
- Known request patterns matched
- What is captured (headers/body/files) and where it lands under `run/artifacts/<honeypot_id>/`
- “Harmless test requests” (benign curls)
- Limitations and safety statement

### 6) Validate + run

```bash
PYTHONPATH=honeypot-platform/packages/hoho_core:honeypot-platform/packages/hoho_runtime \
  python -m hoho_runtime.cli validate honeypot-platform/honeypots/low/<honeypot_id>/honeypot.yaml

PYTHONPATH=honeypot-platform/packages/hoho_core:honeypot-platform/packages/hoho_runtime \
  python -m hoho_runtime.cli run honeypot-platform/honeypots/low/<honeypot_id>
```

Then verify:
- `run/artifacts/<honeypot_id>/index/events.jsonl` exists
- Body/file blobs appear under `run/artifacts/<honeypot_id>/blobs/`

---

## Quality bar for low-interaction honeypots

- Match on *protocol traits*, not exploit PoC strings.
- Responses should be plausible but minimal (do not act like a full vulnerable service).
- Emit a clear verdict (`probe` vs `exploit` vs `unknown`) when possible.
- Capture only what you need; respect limits and redaction.
