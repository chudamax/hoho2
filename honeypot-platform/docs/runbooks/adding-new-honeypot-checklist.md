# Checklist: adding a new honeypot

Use this as a fast, copy/paste checklist when adding a new honeypot.

---

## 0) Pick interaction level
- [ ] Low: pure behavior emulation (safe request/response rules)
- [ ] High: real stack in containers + sensors

## 1) Pick honeypot_id
- [ ] Folder name and `metadata.id` match exactly
- [ ] Prefer `cve-YYYY-NNNNN_<product>_<vector>`

## 2) Create canonical folder + files
- [ ] `honeypot-platform/honeypots/{low,high}/<honeypot_id>/honeypot.yaml`
- [ ] `honeypot-platform/honeypots/{low,high}/<honeypot_id>/README.md`
- [ ] Optional: `reset.sh`, `sample_requests/`, `assets/` (all inside the same folder)

## 3) Low-interaction specifics
- [ ] Stable matchers (path/encoding/protocol traits), not PoC strings
- [ ] `emit_event` verdicts: `probe` / `exploit` / `unknown`
- [ ] Capture only what you need (`store_body` / `store_multipart`) and enforce limits

## 4) High-interaction specifics
- [ ] Stack starts and exposes the intended port(s)
- [ ] Sensors: `http_proxy`, `egress_proxy` (if post-exploitation downloads matter), `fsmon`, `pcap`
- [ ] `fsmon.watch`: include `/tmp` and app writable dirs; avoid noisy caches via deny globs
- [ ] If TLS MITM enabled: CA/trust install works and is documented

## 5) Validation / run
- [ ] `hoho validate ...` passes
- [ ] `hoho run ...` produces `run/artifacts/<honeypot_id>/index/events.jsonl`
- [ ] README includes benign curl tests and stop/cleanup commands

## 6) Final “don’ts”
- [ ] No new files under `honeypot-platform/packs/`
- [ ] No run-id subtrees under `run/artifacts/`
- [ ] Do not commit generated `deploy/compose/<honeypot_id>/`
