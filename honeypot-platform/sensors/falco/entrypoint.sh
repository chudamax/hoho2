#!/usr/bin/env sh
set -eu

RULES_CSV="${FALCO_RULES:-/runtime/falco/hoho_rules.yaml}"
PRIORITY_MIN="${FALCO_PRIORITY_MIN:-Warning}"
ENGINE="${FALCO_ENGINE:-modern_ebpf}"
APPEND_FIELDS="${HOHO_FALCO_APPEND_FIELDS:-}"

FALCO_ARGS="--unbuffered -o json_output=true -o priority=${PRIORITY_MIN} -o program_output.enabled=true -o program_output.keep_alive=true -o program_output.program='python3 /app/forwarder.py'"

if [ "$ENGINE" = "modern_ebpf" ]; then
  FALCO_ARGS="$FALCO_ARGS -o engine.kind=modern_ebpf"
fi

if [ -n "$APPEND_FIELDS" ]; then
  OLDIFS="$IFS"
  IFS=','
  for field in $APPEND_FIELDS; do
    [ -n "$field" ] || continue
    FALCO_ARGS="$FALCO_ARGS -o append_output[]=${field}"
  done
  IFS="$OLDIFS"
fi

OLDIFS="$IFS"
IFS=','
for rule_file in $RULES_CSV; do
  [ -n "$rule_file" ] || continue
  FALCO_ARGS="$FALCO_ARGS -r $rule_file"
done
IFS="$OLDIFS"

# shellcheck disable=SC2086
exec sh -c "falco $FALCO_ARGS"
