# Runbook: high-interaction honeypot from CVE

High-interaction honeypots run a real service (or realistic vulnerable stack) in containers and attach sensors to capture the full exploitation and post-exploitation workflow.

This runbook is written for coding agents and humans adding a new high-interaction honeypot under `honeypot-platform/honeypots/high/`.

---

## Required layout

- Honeypot folder: `honeypot-platform/honeypots/high/<honeypot_id>/`
- Definition: `honeypot-platform/honeypots/high/<honeypot_id>/honeypot.yaml`
- Docs: `honeypot-platform/honeypots/high/<honeypot_id>/README.md`
- Optional assets/scripts: under the same honeypot folder
- Compose output: `honeypot-platform/deploy/compose/<honeypot_id>/docker-compose.yml` (overwritten)
- Artifacts: `honeypot-platform/run/artifacts/<honeypot_id>/...` (overwritten)

> The repo uses an overwrite-based storage layout. Re-running the same `<honeypot_id>` overwrites compose output and artifacts.

---

## Workflow

### 1) Research and choose a realistic stack
Pick a container image and a minimal set of services to reproduce the vulnerable surface:
- web app + db + cache, etc.
- keep the stack small but functional enough to attract real exploit traffic

Document the choice in README:
- image names + tags
- which port(s) are exposed
- what “works” from an attacker’s view

### 2) Create folder + base YAML
Create:

- `honeypot-platform/honeypots/high/<honeypot_id>/honeypot.yaml`
- `honeypot-platform/honeypots/high/<honeypot_id>/README.md`

Minimal skeleton:

```yaml
apiVersion: hoho.dev/v1
kind: HoneypotPack
metadata:
  id: <honeypot_id>
  name: <Human readable name>
  interaction: high
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

telemetry:
  emit_events: true
  redact_headers:
    - Authorization
    - Cookie

stack:
  runtime:
    mode: container
  services:
    app:
      image: <image:tag>
      ports:
        - "8080:80"
      environment: {}
      volumes: []
      networks: [honeynet]

sensors: []
```

### 3) Add the sensor baseline (recommended)
For high stacks, default to maximum visibility:

1. **Inbound reverse proxy (`http_proxy`)**
   - Put the proxy in front of the vulnerable service.
   - Capture full request metadata; capture request bodies for POST where useful.

2. **Outbound forward proxy (`egress_proxy`)**
   - Route container egress via proxy to capture downloads during post-exploitation.
   - Enable TLS MITM when you want to capture HTTPS tooling fetches.
   - If CA trust install is enabled, ensure your service has a working CA install hook (typically `/hoho/ca/install-ca.sh`).

3. **Filesystem monitoring (`fsmon`)**
   - Only watches mounted paths. Choose realistic writable targets.
   - Always include `/tmp` or equivalent if it is relevant and writable.
   - Include app-specific writable/content directories.

4. **Packet capture (`pcap`)**
   - Capture ground-truth network traffic for later analysis.

5. (Optional) **Process telemetry (`falco`)**
   - Use when you need exec/process telemetry.
   - Consider “observe-only” mode by default; enforcement should be explicit and documented.

### 4) fsmon watch_paths guidance
When configuring fsmon watch paths, include:
- common temp dirs: `/tmp`, `/var/tmp` (if present and writable)
- the app’s most likely writable/content directories (e.g. WordPress: `/var/www/html/wp-content/uploads`)
- avoid watching huge read-only trees

### 5) Add README.md (+ optional reset.sh)
README must include:
- Stack description (services, ports, credentials if any)
- Sensors enabled and what they capture
- “Harmless test requests” (benign curls)
- Where to find artifacts (`run/artifacts/<honeypot_id>/...`)
- How to stop and cleanup
- Safety/limitations statement

If useful, add `reset.sh` to wipe only the honeypot’s compose bundle + volumes (no global cleanup).

### 6) Validate + render + run

```bash
PYTHONPATH=honeypot-platform/packages/hoho_core:honeypot-platform/packages/hoho_runtime \
  python -m hoho_runtime.cli validate honeypot-platform/honeypots/high/<honeypot_id>/honeypot.yaml

PYTHONPATH=honeypot-platform/packages/hoho_core:honeypot-platform/packages/hoho_runtime \
  python -m hoho_runtime.cli render-compose honeypot-platform/honeypots/high/<honeypot_id>/honeypot.yaml

PYTHONPATH=honeypot-platform/packages/hoho_core:honeypot-platform/packages/hoho_runtime \
  python -m hoho_runtime.cli run honeypot-platform/honeypots/high/<honeypot_id>
```

Then verify:
- `deploy/compose/<honeypot_id>/docker-compose.yml` exists
- `run/artifacts/<honeypot_id>/index/events.jsonl` exists
- sensor artifacts appear (pcaps, fsmon deltas, egress response bodies, etc.)

---

## Quality bar for high-interaction honeypots

- Stack should be minimal but credible to attackers.
- Default to maximum visibility (proxy + egress + fsmon + pcap).
- If TLS MITM is enabled, ensure CA paths and trust installation are correct and documented.
