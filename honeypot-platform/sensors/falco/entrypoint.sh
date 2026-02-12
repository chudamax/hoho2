#!/usr/bin/env sh
set -eu

RULES_CSV="${FALCO_RULES:-/runtime/falco/hoho_rules.yaml}"
PRIORITY_MIN="${FALCO_PRIORITY_MIN:-Warning}"
ENGINE="${FALCO_ENGINE:-modern_ebpf}"
APPEND_FIELDS="${HOHO_FALCO_APPEND_FIELDS:-}"

# Build args safely (no string concatenation)
set -- falco --unbuffered \
  -o json_output=true \
  -o "priority=${PRIORITY_MIN}" \
  -o program_output.enabled=true \
  -o program_output.keep_alive=true \
  -o "program_output.program=python3 /app/forwarder.py"

if [ "$ENGINE" = "modern_ebpf" ]; then
  set -- "$@" -o engine.kind=modern_ebpf
fi

# Convert HOHO_FALCO_APPEND_FIELDS (CSV) into a single append_output[] JSON object:
# - "evt.hostname" stays a string field
# - "k=v" becomes {"k":"v"}
# Falco expects append_output entries as objects. :contentReference[oaicite:1]{index=1}
if [ -n "$APPEND_FIELDS" ]; then
  APPEND_JSON="$(python3 - <<'PY'
import os, json
csv = os.environ.get("HOHO_FALCO_APPEND_FIELDS", "")
extra_fields = []
for raw in csv.split(","):
    raw = raw.strip()
    if not raw:
        continue
    if "=" in raw:
        k, v = raw.split("=", 1)
        k = k.strip()
        v = v.strip()
        if k:
            extra_fields.append({k: v})
    else:
        extra_fields.append(raw)  # e.g. "evt.hostname"

if extra_fields:
    obj = {"match": {"source": "syscall"}, "extra_fields": extra_fields}
    print(json.dumps(obj))
PY
)"
  if [ -n "$APPEND_JSON" ]; then
    set -- "$@" -o "append_output[]=${APPEND_JSON}"
  fi
fi

# Add rule files
OLDIFS="$IFS"
IFS=','

for rule_file in $RULES_CSV; do
  [ -n "$rule_file" ] || continue
  set -- "$@" -r "$rule_file"
done

IFS="$OLDIFS"

echo "$@"
exec "$@"
