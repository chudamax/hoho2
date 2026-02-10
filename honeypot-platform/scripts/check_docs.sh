#!/usr/bin/env bash
set -euo pipefail

DOCS=(
  docs/ARCHITECTURE.md
  docs/PACK_SPEC.md
  docs/DSL_REFERENCE.md
  docs/EVENT_SCHEMA.md
  docs/SENSORS.md
  docs/STORAGE_LAYOUT.md
  docs/DEPLOYMENT.md
  docs/SECURITY.md
)

MIN_LINES=12

for d in "${DOCS[@]}"; do
  [[ -f "$d" ]] || { echo "missing: $d"; exit 1; }
  lines=$(wc -l < "$d")
  (( lines >= MIN_LINES )) || { echo "too short: $d ($lines < $MIN_LINES)"; exit 1; }
  rg -q '^# ' "$d" || { echo "missing title heading: $d"; exit 1; }
  sec_count=$(rg -c '^## ' "$d")
  (( sec_count >= 2 )) || { echo "need at least 2 sections: $d"; exit 1; }
  echo "ok: $d"
done
