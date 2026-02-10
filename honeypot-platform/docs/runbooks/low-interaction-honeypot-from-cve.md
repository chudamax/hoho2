<!--
File: docs/runbooks/low-interaction-honeypot-from-cve.md
Purpose: Codex/humans runbook to create a new low-interaction honeypot pack from a CVE ID.
-->

# Runbook: Create a low-interaction honeypot from a CVE (YAML-first)

This runbook describes a repeatable process to implement a **low-interaction** honeypot **from only a CVE name/ID** (e.g., `CVE-2021-41773`).

Low-interaction here means: **behavioral emulation** (request/response), not a real vulnerable service.  
The goal is to **attract and record** probes/exploit attempts and produce high-quality telemetry + artifacts for analysis.

---

## Where to put this so Codex uses it

**Recommended:**
- Save this file as: `docs/runbooks/low-interaction-honeypot-from-cve.md`
- Add a pointer in your repo-root `AGENTS.md`:

```md
# AGENTS.md (repo root)

## Honeypots
- When asked to create a new low-interaction honeypot from a CVE, ALWAYS read:
  docs/runbooks/low-interaction-honeypot-from-cve.md
- Follow the runbook exactly: research -> derive request transcripts -> implement YAML pack -> validate/run -> document.
- Do not paste weaponized payloads into docs or code comments; use abstract patterns only.
```

If you often work in a specific folder (e.g., `packs/low/`), you can also add a **folder-local** `AGENTS.md` there with the same pointer.

---

## Inputs

Minimum required:

- `CVE_ID`: `CVE-YYYY-NNNN`

Optional:

- `PRODUCT_HINT`: if provided (e.g., "Apache httpd"), use it to speed up research.
- `SERVICE_PERSONA`: desired banner style (server header / HTML style), if you care.
- `LISTEN_PORTS`: default ports to bind (e.g., 80/443/8080).

---

## Output deliverables

You must produce:

1. A new **YAML pack** implementing the emulation behavior.
2. A short **pack README** describing what it catches, what it stores, and how to run it. Also oneline examples to test the honeypot instance.
3. A minimal **tagging/telemetry contract** (what events/tags/indicators are emitted).

Recommended paths (adjust to your repo conventions):

- Pack: `packs/low/<cve-id>_<slug>.yaml`
- Doc:  `packs/low/<cve-id>_<slug>.md`

---

## Safety & operational rules (non-negotiable)

- **Never run real vulnerable code** in low-interaction packs.
- **Never “attack back”** and never add outbound exploitation logic.
- Store untrusted request bodies as **opaque bytes** (optionally gzip), do not parse/execute.
- Default to logging with header redaction (`Authorization`/`Cookie`/etc.).

---

## Phase 1 — Research the CVE

### 1.1 Identify the exposed surface

Determine:

- Affected product and typical deployment context
- Protocol surface (HTTP? SOAP? JSON-RPC? multipart upload? etc.)
- Default ports/paths (if common)
- Vulnerability class (path traversal, SQLi, auth bypass, deserialization, etc.)
- Typical attacker objectives (file read, command exec, web shell dropper, etc.)

**Deliverable:** a short “CVE profile” note (can live in the pack README) with:
- product/version range (approx)
- vuln type
- primary endpoint(s)
- method(s)
- expected responses attackers look for

### 1.2 Extract “attack transcripts”

Find at least **one** public PoC/writeup that provides observable request structure:

- HTTP method
- path(s) / parameter names
- required headers (if any)
- content type and body shape (if POST/PUT)
- typical status codes and response markers

**Deliverable:** list of 2–5 request patterns:
- `PRIMARY_PROBES`: most distinctive requests
- `SECONDARY_FOLLOWUPS`: common follow-up probes (`/`, `/login`, `/robots.txt`, etc.)
- `NEGATIVE_CASES`: patterns you should *not* over-match
- `EXAMPLES_TO_TEST`: exploitations examples

---

## Phase 2 — Design the emulation behavior

### 2.1 Choose “service persona”

Pick:
- `Server` header value
- baseline landing page/body style (HTML/text/JSON)
- whether to emulate TLS (if your platform supports it)

### 2.2 Decide what to capture

At minimum, capture:
- method/path/query
- selected headers (with redaction)
- body bytes when relevant (uploads, serialized blobs, etc.)
- source IP / connection metadata (whatever your platform provides)

Tagging guidance:
- Always tag `cve:<CVE_ID>`
- Add `product:<name>` and `technique:<vuln-type>`
- Use a simple `verdict`: `probe | exploit | upload | unknown`

### 2.3 Decide response strategy

For each primary probe:
- choose a plausible status: `200/403/404/500`
- return plausible headers and small body marker
- optionally add:
  - `delay` + jitter
  - `drop` (timeout simulation) for some patterns

Goal: scanners/exploit scripts should think “something is there” and keep going,  
but you should not reveal “too perfect” behavior.

---

## Phase 3 — Implement the YAML pack

Create a new file:

`packs/low/<cve-id>_<short-slug>.yaml`

Example filename:
- `packs/low/cve-2021-41773_apache-traversal.yaml`

### 3.1 YAML template (copy/paste)

> Adjust keys to match your engine’s schema; the structure below is intentionally generic.

```yaml
apiVersion: honeypot.dev/v1
kind: HoneypotPack

metadata:
  id: cve-YYYY-NNNN-short-slug
  name: "CVE-YYYY-NNNN <Product> <VulnType> (low)"
  interaction: low
  tags:
    - cve
    - cve:YYYY-NNNN
    - product:<product>
    - technique:<vuln-type>
  description: >
    Low-interaction emulation for CVE-YYYY-NNNN. Captures probes/exploit attempts
    and returns plausible responses. Does not run real vulnerable software.

listen:
  - host: 0.0.0.0
    port: 8080

telemetry:
  emit_events: true
  redact_headers: [Authorization, Cookie]

limits:
  max_body_bytes: 1048576
  max_upload_bytes: 10485760

storage:
  backend: filesystem
  root: ./run/artifacts

behaviors:
  # --- Primary probe 1 ---
  - name: primary-probe-1
    match:
      method: GET
      pathRegex: "<stable pattern from transcript>"
    actions:
      - emit_event:
          verdict: exploit
          tags: ["cve:CVE-YYYY-NNNN", "product:<product>", "technique:<vuln-type>"]
          indicators: ["cve:CVE-YYYY-NNNN"]
      - delay:
          ms: 120
          jitterMs: 80
      - respond:
          status: 200
          headers:
            Content-Type: text/plain
            Server: "<persona>"
          body: "OK"

  # --- Primary probe 2 (POST example) ---
  - name: primary-probe-2
    match:
      method: POST
      path: "<path from transcript>"
      contentTypeContains: "application/x-www-form-urlencoded"
    actions:
      - emit_event:
          verdict: exploit
          tags: ["cve:CVE-YYYY-NNNN", "product:<product>", "technique:<vuln-type>"]
      - store_body:
          kind: request_body
          gzip: true
      - respond:
          status: 500
          headers:
            Content-Type: text/plain
            Server: "<persona>"
          body: "Internal Server Error"

  # --- Secondary: landing ---
  - name: landing
    match:
      method: GET
      path: /
    actions:
      - emit_event:
          verdict: probe
          tags: ["product:<product>"]
    respond:
      status: 200
      headers:
        Content-Type: text/html
        Server: "<persona>"
      body: "<html><body><h1>It works</h1></body></html>"

  # --- Default catch-all ---
  - name: default
    match:
      pathGlob: "/*"
    actions:
      - emit_event:
          verdict: unknown
          tags: []
    respond:
      status: 404
      headers:
        Content-Type: text/plain
      body: "not found"
```

### 3.2 Match rules: how to avoid overfitting

Prefer matching on:
- distinctive paths (or path prefixes)
- presence of parameter keys (not full payload values)
- short header tokens (only if truly distinctive)

Avoid:
- full payload regexes that capture weaponized strings
- matching on user-agent only
- matching on highly variable encodings unless necessary

Rule ordering:
- Most specific CVE rules first
- Generic landing/catch-all last

---

## Phase 4 — Validate & run (smoke)

1. Validate (if your platform supports it):
- `honeypot validate packs/low/<pack>.yaml`

2. Run:
- `honeypot run packs/low/<pack>.yaml`

3. Send harmless requests:
- `curl -i http://127.0.0.1:<port>/`
- `curl -i http://127.0.0.1:<port>/<known-probe-path>`

4. Confirm artifacts exist:
- event log (e.g., JSONL)
- stored request bodies (if enabled)

---

## Phase 5 — Document the pack

Create:

`packs/low/<cve-id>_<slug>.md`

Minimum contents:
- What it emulates (product/vuln family)
- What it captures (which endpoints, whether it stores bodies)
- Event tags/fields used
- How to run it (port, command)
- Known limitations (what is *not* emulated)

---

## Acceptance checklist

A pack is “done” when:

- [ ] YAML pack committed under `packs/low/`
- [ ] Pack has `metadata.id`, CVE tags, and persona headers
- [ ] ≥2 primary probe behaviors implemented from transcripts
- [ ] Every request emits an event
- [ ] POST/PUT bodies are stored when relevant (gzip, size limit)
- [ ] Responses are plausible (status + headers + small body)
- [ ] A short pack README exists under `packs/low/`

---

## Optional: future automation (scaffolder)

If you later build a CLI scaffolder, desired behavior:

- `honeypot scaffold --cve CVE-YYYY-NNNN --out packs/low/...`
- Pull CVE metadata and references
- Create YAML skeleton + README stub
- Leave TODOs for transcript-derived match rules
