# AGENTS.md

This repo is designed so *humans* and *coding agents* (Codex, ChatGPT, etc.) can add honeypots in a predictable, reviewable way.

If you are an agent performing work in this repo, follow this file **exactly**.

---

## Agent contract

### MUST
- Follow the canonical filesystem layout (`honeypots/{low,high}/<honeypot_id>/...`) and the overwrite-based artifact layout (`run/artifacts/<honeypot_id>/...`). See:
  - `honeypot-platform/docs/DIRECTORY_LAYOUT.md`
  - `honeypot-platform/docs/STORAGE_LAYOUT.md`
- Validate your work with `hoho validate ...` before considering it “done”.
- Keep **all** honeypot-specific docs inside the honeypot folder as `README.md`.
- Keep any referenced local assets (scripts, configs, sample payloads) **inside the same honeypot folder**.

### MUST NOT
- Do **not** create run-id subtrees under `run/artifacts/` (no `run/artifacts/runs/...`).
- Do **not** create non-canonical honeypot folders (example forbidden: `honeypots/high/2021-41773_42013/`).
- Do **not** add new honeypot YAML definitions under `honeypot-platform/packs/` (deprecated compatibility only).
- Do **not** commit generated compose output.

---

## Docs you MUST read before editing/adding honeypots

- Spec + schema rules: `honeypot-platform/docs/PACK_SPEC.md`
- Low-interaction DSL: `honeypot-platform/docs/DSL_REFERENCE.md`
- Sensor behavior + env contracts: `honeypot-platform/docs/SENSORS.md`
- Storage layout + overwrite semantics: `honeypot-platform/docs/STORAGE_LAYOUT.md`
- Deployment notes: `honeypot-platform/docs/DEPLOYMENT.md`
- Compose output notes (incl. egress CA paths): `honeypot-platform/deploy/compose/README.md`
- Telemetry shipping: `honeypot-platform/docs/TELEMETRY_SHIPPING.md`

---

## Canonical layout (the only allowed layout)

### Low interaction
- Folder: `honeypot-platform/honeypots/low/<honeypot_id>/`
- Definition: `honeypot-platform/honeypots/low/<honeypot_id>/honeypot.yaml`
- Docs: `honeypot-platform/honeypots/low/<honeypot_id>/README.md`

### High interaction
- Folder: `honeypot-platform/honeypots/high/<honeypot_id>/`
- Definition: `honeypot-platform/honeypots/high/<honeypot_id>/honeypot.yaml`
- Docs: `honeypot-platform/honeypots/high/<honeypot_id>/README.md`
- Optional assets: any additional files under the same folder (e.g., `reset.sh`, `rules/`, `configs/`, `sample_requests/`)

### Generated output (never committed)
- Compose output: `honeypot-platform/deploy/compose/<honeypot_id>/docker-compose.yml` (overwritten)
- Runtime CA (when egress MITM enabled): `honeypot-platform/deploy/compose/<honeypot_id>/runtime/ca/*`
- Artifacts: `honeypot-platform/run/artifacts/<honeypot_id>/**` (overwritten)

> Important: the “simple layout” has **no run isolation**. Don’t run the same `<honeypot_id>` twice expecting separate histories. If you need a fresh run, clean the artifact directory first.

---

## When asked to “add a new honeypot”: required deliverables

For **every** new honeypot, deliver all items below:

1) `honeypot-platform/honeypots/{low,high}/<honeypot_id>/honeypot.yaml`
2) `honeypot-platform/honeypots/{low,high}/<honeypot_id>/README.md`
3) If high-interaction: include a sensible sensor set (see “High capture baseline”).
4) If the honeypot benefits from it: `reset.sh` (safe cleanup of volumes/state) and a small `sample_requests/` folder with benign curl requests.
5) Update this file (`AGENTS.md`) **only** if your change introduces a new rule or a new “golden example”.

---

## Honeypot ID and naming

- Use `<honeypot_id>` as the *only* filesystem identifier.
- `metadata.id` MUST equal the folder name.
- Preferred pattern:
  - `cve-YYYY-NNNNN_<product>_<vector>`
  - Examples: `cve-2021-41773_42013_apache_rce`, `cve-2017-12629_solr_rce`

---

## Runbooks (follow exactly)

- Low interaction: `honeypot-platform/docs/runbooks/low-interaction-honeypot-from-cve.md`
- High interaction: `honeypot-platform/docs/runbooks/high-interaction-honeypot-from-cve.md`
- Checklist (quick): `honeypot-platform/docs/runbooks/adding-new-honeypot-checklist.md`

---

## High-interaction capture baseline (recommended)

For “high” stacks, default to maximum visibility:

- `http_proxy` (reverse proxy) for inbound request/response metadata and request body capture.
- `egress_proxy` (forward proxy) to capture **outbound** downloads (post-exploitation stage). Enable TLS MITM when you want to capture HTTPS tooling fetches.
- `fsmon` to capture file writes **in shared mounted paths** (see fsmon rules below).
- `pcap` for ground-truth network capture.
- Optional (when you want process telemetry): `falco`.

### fsmon rules of thumb
- Only watch paths that are *actually writable* and *actually mounted* for the target service.
- Always include common temp dirs if they exist in the container and are relevant: `/tmp`, `/var/tmp`.
- Include app-specific writable/content dirs (examples):
  - WordPress: `/var/www/html/wp-content` and `/var/www/html/wp-content/uploads`
  - Apache CGI/RCE style targets: `/usr/local/apache2/logs`, `/var/log/apache2`, `/tmp`
  - Java apps: `/tmp`, `/opt/<app>/data`, `/var/lib/<app>`
- Keep deny globs for noisy directories (cache, sessions) when they would dominate output.

---

## Telemetry forwarding/shipping

- In-pack `telemetry.forwarding` is deprecated and ignored; shipping is done by the runtime shipper (`hoho ship`) using global env (`HOHO_HUB_URL`, `HOHO_HUB_TOKEN`, optional `HOHO_FORWARD_FILTERS_JSON`).

- `hoho` auto-loads `honeypot-platform/.env` by default (unless `--no-env`). Put hub config there for local/dev.

---

## Working reference honeypots (golden examples)

High interaction:
- `honeypot-platform/honeypots/high/cve-2021-41773_42013_apache_rce/honeypot.yaml`

Low interaction:
- `honeypot-platform/honeypots/low/cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce/honeypot.yaml`

---

## Operational commands (stop/cleanup)

- Stop everything: `hoho down-all` (optionally `--volumes`)
- Per-honeypot manual stop:
  - `docker compose -p "hoho-<honeypot_id>" -f deploy/compose/<honeypot_id>/docker-compose.yml down -v`
