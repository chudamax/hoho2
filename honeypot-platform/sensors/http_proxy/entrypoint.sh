#!/usr/bin/env sh
set -eu
: "${UPSTREAM:=http://upstream:80}"
exec mitmdump --mode "reverse:${UPSTREAM}" -s /app/capture_addon.py
