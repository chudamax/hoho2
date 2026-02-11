#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

fail() {
  echo "layout check failed: $1" >&2
  exit 1
}

RUNS_SUBTREE="runs"
LEGACY_RUNS_PATH="run/artifacts/${RUNS_SUBTREE}"

if [ -d "$LEGACY_RUNS_PATH" ]; then
  fail "forbidden path exists: ${LEGACY_RUNS_PATH}"
fi

if find honeypots -type f \( -name 'docker-compose*.yml' -o -name 'docker-compose*.yaml' \) | grep -q .; then
  fail "forbidden compose file found under honeypots/"
fi

python3 scripts/validate_honeypots_layout.py

echo "layout check passed"
