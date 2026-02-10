#!/usr/bin/env bash
set -euo pipefail
PACK_ID="${HOHO_PACK_ID:-unknown-pack}"
ROOT="${HOHO_STORAGE_ROOT:-/artifacts}"
ROTATE_SECONDS="${PCAP_ROTATE_SECONDS:-60}"
ROTATE_COUNT="${PCAP_ROTATE_COUNT:-10}"
OUT_DIR="${ROOT}/${PACK_ID}/pcap"
mkdir -p "$OUT_DIR" "${ROOT}/${PACK_ID}/index"

tcpdump -i any -w "${OUT_DIR}/segment-%Y%m%d-%H%M%S.pcap" -G "$ROTATE_SECONDS" -W "$ROTATE_COUNT" || true
for f in "$OUT_DIR"/*.pcap; do
  [ -f "$f" ] || continue
  sha=$(sha256sum "$f" | awk '{print $1}')
  bdir="${ROOT}/${PACK_ID}/blobs/${sha:0:2}"
  mkdir -p "$bdir"
  cp "$f" "$bdir/$sha"
  printf '{"schema_version":1,"event_id":"pcap-%s","ts":"%s","pack_id":"%s","interaction":"high","component":"sensor.pcap","src":{"ip":null,"port":null,"forwarded_for":[],"user_agent":null},"proto":"tcp","request":{},"response":{"status_code":null,"bytes_sent":0,"profile":null},"classification":{"verdict":"probe","tags":["pcap_segment"],"indicators":[]},"decision":{"truncated":false,"oversized":false,"rate_limited":false,"dropped":false},"artifacts":[{"kind":"pcap_segment","sha256":"%s","size":%s,"mime":"application/vnd.tcpdump.pcap","storage_ref":"blobs/%s/%s","meta":{"source":"%s"}}]}\n' "$(date +%s)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$PACK_ID" "$sha" "$(wc -c < "$f")" "${sha:0:2}" "$sha" "$f" >> "${ROOT}/${PACK_ID}/index/events.jsonl"
done
