#!/usr/bin/env bash
set -euo pipefail
HONEYPOT_ID="${HOHO_HONEYPOT_ID:-${HOHO_PACK_ID:-unknown-pack}}"
SESSION_ID="${HOHO_SESSION_ID:-unknown-session}"
AGENT_ID="${HOHO_AGENT_ID:-unknown-agent}"
ROOT="${HOHO_STORAGE_ROOT:-/artifacts}"
ROTATE_SECONDS="${PCAP_ROTATE_SECONDS:-60}"
ROTATE_COUNT="${PCAP_ROTATE_COUNT:-10}"
OUT_DIR="${ROOT}/${HONEYPOT_ID}/pcap"
mkdir -p "$OUT_DIR" "${ROOT}/${HONEYPOT_ID}/index"

tcpdump -i any -w "${OUT_DIR}/segment-%Y%m%d-%H%M%S.pcap" -G "$ROTATE_SECONDS" -W "$ROTATE_COUNT" || true
for f in "$OUT_DIR"/*.pcap; do
  [ -f "$f" ] || continue
  sha=$(sha256sum "$f" | awk '{print $1}')
  bdir="${ROOT}/${HONEYPOT_ID}/blobs/${sha:0:2}"
  mkdir -p "$bdir"
  cp "$f" "$bdir/$sha"
  printf '{"schema_version":2,"event_id":"pcap-%s","ts":"%s","honeypot_id":"%s","session_id":"%s","agent_id":"%s","event_name":"pcap.segment","component":"sensor.pcap","proto":"tcp","classification":{"verdict":"probe","tags":["pcap_segment"],"indicators":[]},"decision":{"truncated":false,"oversized":false,"rate_limited":false,"dropped":false},"artifacts":[{"kind":"pcap_segment","sha256":"%s","size":%s,"mime":"application/vnd.tcpdump.pcap","storage_ref":"blobs/%s/%s","meta":{"source":"%s"}}]}
' "$(date +%s)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$HONEYPOT_ID" "$SESSION_ID" "$AGENT_ID" "$sha" "$(wc -c < "$f")" "${sha:0:2}" "$sha" "$f" >> "${ROOT}/${HONEYPOT_ID}/index/events.jsonl"
done
