<!--
File: docs/runbooks/high-interaction-honeypot-from-cve.md
Purpose: Codex/humans runbook to create a new HIGH-interaction honeypot from a CVE ID.
-->

# Runbook: Create a high-interaction honeypot from a CVE (real service in a sandbox)

This runbook describes a repeatable process to implement a **high-interaction** honeypot starting from only a **CVE name/ID** (e.g., `CVE-2020-25213`).

High-interaction here means: you run a **real (vulnerable) service** in a controlled sandbox and capture **full attacker workflow** (pre-exploit probes, exploitation, post-exploitation downloads, file drops, process activity) for later analysis.

> This is a **defensive** runbook. It focuses on safe deployment, isolation, and telemetry.  
> Do **not** embed weaponized payloads or “how-to exploit” instructions in the repo.

---

## Where to put this so Codex uses it

**Recommended:**
- Save this file as: `docs/runbooks/high-interaction-honeypot-from-cve.md`
- Add a pointer in your repo-root `AGENTS.md`:

```md
# AGENTS.md (repo root)

## Honeypots
- When asked to create a new high-interaction honeypot from a CVE, ALWAYS read:
  docs/runbooks/high-interaction-honeypot-from-cve.md
- Prioritize isolation + capture (pcap, proxy downloads, fsmon, process/audit logs).
```

If you often work in a specific folder (e.g., `honeypots/high/`), add a folder-local `AGENTS.md` there as well.

---

## What “high-interaction” means (scope)

A high-interaction honeypot includes:

- A **real service stack** (app + dependencies) at a vulnerable version
- A safe **sandbox boundary** (container, preferably microVM / gVisor / Kata)
- **Complete telemetry**:
  - network (PCAP)
  - application logs
  - file-system changes (new/modified files)
  - process execution / command lines (best-effort)
  - outbound downloads captured via proxy (HTTP/HTTPS)
- **Resetability**:
  - fast “wipe and redeploy” (immutable image + ephemeral volumes)
  - clear artifact directories for each session/time window

---

## Inputs

Minimum required:

- `CVE_ID`: `CVE-YYYY-NNNN`

Optional:

- `PRODUCT_HINT`: “WordPress”, “Apache httpd”, “MOVEit”, etc.
- `DEPLOYMENT_MODE`: `docker-compose` or `k8s`
- `ISOLATION_LEVEL`: `container` | `gvisor` | `kata` (prefer stronger isolation for risky CVEs)
- `INGRESS_PORTS`: e.g., 80/443/8080
- `EGRESS_POLICY`: `deny-all` (best) or `allow-with-proxy` (common for download capture)

---

## Output deliverables

You must produce:

1. A runnable **high-interaction environment** for the CVE:
   - `docker-compose.yml` or Kubernetes manifests
   - a pinned vulnerable image reference (or Dockerfile that builds it)
   - configuration files (app config, reverse proxy config, etc.)

2. A **capture stack**:
   - PCAP capture (e.g., tcpdump sidecar)
   - filesystem monitoring (inotify/auditd/agent)
   - outbound proxy capture (HTTP/HTTPS)
   - structured event log (JSONL) + blob storage for artifacts

3. Documentation:
   - `README.md` for the honeypot (how to run/reset, what is captured, safety notes)
   - “Telemetry contract” (event fields, tags, artifact paths)

Recommended paths (adjust to your repo conventions):

- `honeypots/high/<cve-id>_<slug>/docker-compose.yml`
- `honeypots/high/<cve-id>_<slug>/README.md`
- `honeypots/high/<cve-id>_<slug>/config/…`
- `run/artifacts/high/<cve-id>_<slug>/<session-id>/…`

---

## Safety & operational rules (non-negotiable)

- **Isolation first**: assume the service will be compromised.
  - Prefer **Kata Containers** or **gVisor** if available.
  - If plain Docker, run rootless where possible and harden aggressively.

- **No sensitive networks**:
  - Place in an isolated VLAN/DMZ or a dedicated cloud account/subnet.
  - Never attach to internal corp networks.

- **Egress policy** (choose one):
  1) **Deny-all egress** (safest) + fake DNS responses, or
  2) **Allow egress only via a controlled proxy** that captures downloads and can block risky destinations.

- **No credentials reuse**: decoy credentials only; never put real secrets in env vars or config.

- **Artifact hygiene**:
  - All captures go to a dedicated artifact root with per-session folders.
  - Redact or avoid logging Authorization/Cookies unless you explicitly want them.

- **Do not embed exploit payloads** in repo docs or comments. Keep matching/transcripts abstract.

---

## Reference architecture (recommended)

### Components

1. **Ingress reverse proxy** (front door)
   - Terminates TLS (optional), normalizes requests, logs requests
   - Can implement basic deception headers, rate limits, and route to target

2. **Target service stack** (the vulnerable workload)
   - App container(s) + DB/cache as required
   - Version-pinned image(s)

3. **Capture plane**
   - **PCAP**: tcpdump on the bridge/network namespace (sidecar or host-level)
   - **FS monitor**: watches web roots, temp dirs, upload dirs, and known persistence locations
   - **Process/audit**: command lines + exec events (best-effort via auditd/eBPF/agent)
   - **Outbound proxy**: transparent or explicit proxy to record downloads (HTTP/HTTPS)
   - **Artifact sink**: local filesystem or object store (MinIO/S3) with immutable session folders

4. **Reset plane**
   - rebuild/recreate containers
   - purge writable volumes (or use tmpfs/ephemeral volumes)
   - rotate artifacts

### Data flow

Ingress → Target (real service)  
Target egress → Proxy → Internet (optional)  
All traffic mirrored to PCAP capture  
FS/proc changes + proxy downloads saved as artifacts  
Structured events emitted to JSONL

---

## Phase 1 — Research the CVE (enough to deploy safely)

### 1.1 Identify deployment requirements
Determine:
- product + vulnerable version(s)
- required dependencies (DB, redis, Java, etc.)
- baseline “healthy” response when service is working
- typical attack surface (HTTP endpoints, admin panels, file upload locations)

### 1.2 Decide “what must be captured”
For this CVE family, decide whether you need:
- request bodies (uploads, serialized blobs)
- full response bodies (rare; usually avoid)
- filesystem diffs (often yes)
- outbound download capture (often yes for post-exploitation)

Deliverable: a short “capture plan” section in the honeypot README.

---

## Phase 2 — Choose/build the vulnerable workload

Preferred options (in order):

1) **Known vulnerable container image** (reproducible, pinned digest)  
2) Build from upstream release tarballs/packages at a pinned version  
3) Build from source at a tag/commit (last resort)

Rules:
- pin versions tightly (tags + digests)
- document how the vulnerable version was selected
- keep configuration minimal and realistic (default-ish)

Deliverable: `images.md` or README section listing:
- image references/digests
- exposed ports
- required env vars
- any initialization steps (DB migration, admin user creation with decoy creds)

---

## Phase 3 — Add isolation + hardening controls

### 3.1 Container hardening baseline (even for vulnerable services)
- drop Linux capabilities (keep minimal)
- run as non-root where possible (some apps require root; document)
- read-only filesystem for containers except explicit writable mounts
- separate networks for ingress vs egress
- resource limits (cpu/mem/pids)
- no Docker socket mounted (never)

### 3.2 Stronger isolation (recommended)
If your environment supports:
- **Kata**: microVM boundary
- **gVisor**: syscall interception sandbox

Deliverable: a short section in README indicating the chosen isolation level and how to enable it.

---

## Phase 4 — Build the capture stack

### 4.1 PCAP capture (must-have)
Capture at least:
- ingress traffic to target
- egress traffic from target (if allowed)

Implementation options:
- tcpdump on the Docker network interface (host-level)
- sidecar container sharing the network namespace (k8s: sidecar; docker: `network_mode: service:<name>`)

Output:
- `pcap/<timestamp>.pcap.gz`

### 4.2 HTTP/HTTPS outbound download capture (recommended)
Goal: capture files/tools pulled during post-exploitation.

Approaches:
- explicit proxy env vars (`HTTP_PROXY`, `HTTPS_PROXY`) in the target container
- transparent proxy via iptables redirect in the target namespace
- include a local CA and trust it in the target container (for HTTPS interception) **only if you accept that risk and document it**

Outputs:
- proxy access logs (structured)
- downloaded binaries/scripts saved as blobs
- optional: SHA256 manifest of all captured downloads

### 4.3 Filesystem monitoring (must-have)
Monitor typical drop locations:
- web roots
- upload dirs
- `/tmp`, `/var/tmp`
- app-specific plugin/theme/module dirs
- cron/systemd/autostart locations (if present in container)

Implementation options:
- lightweight inotify watcher writing JSON events
- periodic file tree snapshot + diff (slower but simple)
- auditd/eBPF (more complete, more complex)

Outputs:
- `fs/events.jsonl`
- `fs/snapshots/<t>/...` (optional)
- `blobs/files/<sha256>_<name>` for extracted new/modified files

### 4.4 Process / execution telemetry (best-effort, recommended)
Capture:
- process start/exit events
- command line, uid/gid
- network connections (optional)

Implementation options (pick what you can run safely):
- auditd inside container (sometimes heavy)
- host-level eBPF agent (preferred if you control host)
- app-layer logs (always)

Output:
- `proc/events.jsonl`

---

## Phase 5 — Define the artifact layout (consistent & analyzable)

Recommended artifact root:
- `run/artifacts/high/<cve-id>_<slug>/<session-id>/`

Within a session:
- `events/events.jsonl` (normalized events across subsystems)
- `pcap/traffic.pcap.gz`
- `proxy/` (logs + downloads + manifests)
- `fs/` (fs events + extracted files)
- `app/` (container logs, app logs)
- `meta/session.json` (timestamps, image digests, config hash)

Session ID suggestions:
- ISO timestamp + random suffix
- include honeypot id and port mapping

---

## Phase 6 — Run, reset, and rotate

### 6.1 Run
- bring up the stack
- verify health endpoints
- verify capture tools are writing artifacts
- verify egress policy is correct

### 6.2 Reset (must be fast)
Provide a `reset.sh` (or Make target) that:
- stops containers
- deletes writable volumes (or recreates them)
- starts fresh
- rotates artifacts into a new session folder

### 6.3 Rotation & retention
- rotate PCAP and logs by time and size
- keep a retention policy to avoid disk exhaustion

---

## Phase 7 — Smoke validation (no exploit payloads)

Validate that the honeypot “feels real” without executing exploitation:

- `curl /` and a few expected endpoints (login page, static assets)
- confirm reverse proxy logs are recorded
- confirm PCAP contains the test traffic
- upload a benign file (if the app supports uploads) and confirm:
  - request body capture (if enabled)
  - fs monitor recorded a new file
  - blob extraction stored it

---

## Minimal documentation for every high-interaction honeypot

Create `honeypots/high/<cve-id>_<slug>/README.md` with:

- Overview: CVE, product, vulnerable version(s)
- How to run / stop / reset
- Ports exposed
- Egress policy (deny-all vs proxy-only)
- What is captured:
  - PCAP
  - proxy downloads
  - fs changes
  - process telemetry
- Artifact directory structure
- Safety notes (isolation level, warnings)

---

## Acceptance checklist (definition of done)

- [ ] Stack is runnable via `docker compose up` (or `kubectl apply`)
- [ ] Target service is reachable and returns plausible responses
- [ ] PCAP is created and rotated
- [ ] Filesystem monitor records and extracts new/modified files
- [ ] Proxy capture is in place (if egress allowed) and stores downloads as blobs
- [ ] Structured events exist (JSONL) with consistent fields and tags, including `cve:<CVE_ID>`
- [ ] Reset is one command and produces a fresh session folder
- [ ] README exists with safety + capture details

---

## Templates (generic, safe)

### A) Suggested docker-compose layout (conceptual)

> This is a conceptual template showing component roles. Adapt to your repo conventions and target app.

```yaml
services:
  ingress:
    image: nginx:stable
    ports:
      - "8080:80"
    volumes:
      - ./config/nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on: [target]
    networks: [ingress_net]

  target:
    image: <pinned-vulnerable-image>
    networks:
      - ingress_net
      - egress_net
    environment:
      # if using explicit proxy:
      # HTTP_PROXY: http://proxy:8080
      # HTTPS_PROXY: http://proxy:8080
      # NO_PROXY: localhost,127.0.0.1
      - TZ=UTC
    volumes:
      - target_data:/var/lib/target   # keep minimal; prefer ephemeral
      - ./run/artifacts:/artifacts

  proxy:
    image: <proxy-image>
    networks: [egress_net]
    volumes:
      - ./run/artifacts:/artifacts

  pcap:
    image: <tcpdump-image>
    # docker: share netns with target
    network_mode: "service:target"
    volumes:
      - ./run/artifacts:/artifacts

  fsmon:
    image: <fsmon-image>
    volumes:
      - target_data:/watch:ro
      - ./run/artifacts:/artifacts
    depends_on: [target]
    networks: [ingress_net]

networks:
  ingress_net: {}
  egress_net: {}

volumes:
  target_data: {}
```

### B) Event schema (minimal)

Emit events with at least:

- `ts` (ISO8601)
- `source` (`ingress|app|proxy|pcap|fs|proc`)
- `cve` (`CVE-YYYY-NNNN`)
- `honeypot_id`
- `src_ip`, `src_port`, `dst_port` (when known)
- `summary`
- `tags` (list)
- `artifact_refs` (paths or blob hashes)

---

## Notes on “realism”

High-interaction realism comes from:
- correct base responses (headers, status codes, HTML)
- real assets (static files, admin panel structure)
- realistic latency and occasional errors
- consistent banners/version strings (but do not leak your host identity)

Avoid:
- too-perfect always-200 responses
- unrealistic giant debug banners (unless that product actually does)
- accidental exposure of your infra (hostname, cloud metadata, internal IPs)
