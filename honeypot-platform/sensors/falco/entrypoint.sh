#!/usr/bin/env sh
set -eu

RULES_CSV="${FALCO_RULES:-/app/rules/hoho_rules.yaml}"
PRIORITY_MIN="${FALCO_PRIORITY_MIN:-Warning}"
ENGINE="${FALCO_ENGINE:-modern_ebpf}"
APPEND_FIELDS="${HOHO_FALCO_APPEND_FIELDS:-}"

set -- falco --unbuffered \
  -o json_output=true \
  -o "priority=${PRIORITY_MIN}" \
  -o program_output.enabled=true \
  -o program_output.keep_alive=true \
  -o "program_output.program=python3 /app/forwarder.py"

if [ "$ENGINE" = "modern_ebpf" ]; then
  set -- "$@" -o engine.kind=modern_ebpf
fi

if [ -n "$APPEND_FIELDS" ]; then
  APPEND_JSON="$(python3 - <<'PY'
import json
import os

csv = os.environ.get("HOHO_FALCO_APPEND_FIELDS", "")
extra_fields = []
for raw in csv.split(","):
    item = raw.strip()
    if not item:
        continue
    if "=" in item:
        key, value = item.split("=", 1)
        key = key.strip()
        value = value.strip()
        if key:
            extra_fields.append({key: value})
    else:
        extra_fields.append(item)

if extra_fields:
    print(json.dumps({"match": {"source": "syscall"}, "extra_fields": extra_fields}))
PY
)"
  if [ -n "$APPEND_JSON" ]; then
    set -- "$@" -o "append_output[]=${APPEND_JSON}"
  fi
fi

OLDIFS="$IFS"
IFS=','
for rule_file in $RULES_CSV; do
  trimmed="$(printf '%s' "$rule_file" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
  [ -n "$trimmed" ] || continue
  set -- "$@" -r "$trimmed"
done
IFS="$OLDIFS"

printf 'Starting Falco command: %s\n' "$*"
exec "$@"
