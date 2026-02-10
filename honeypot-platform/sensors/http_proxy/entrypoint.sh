#!/usr/bin/env sh
set -eu

: "${UPSTREAM:=http://upstream:80}"
: "${PROXY_LISTEN_HOST:=0.0.0.0}"
: "${PROXY_LISTEN_PORT:=8080}"
: "${PROXY_KEEP_HOST_HEADER:=true}"
: "${PROXY_EXTRA_ARGS:=}"

is_truthy() {
    value=$(printf '%s' "$1" | tr '[:upper:]' '[:lower:]')
    case "$value" in
        1|true|yes|on)
            return 0
            ;;
        *)
            return 1
            ;;
    esac
}

set -- \
    --mode "reverse:${UPSTREAM}" \
    --listen-host "${PROXY_LISTEN_HOST}" \
    --listen-port "${PROXY_LISTEN_PORT}" \
    -s /app/capture_addon.py

if is_truthy "${PROXY_KEEP_HOST_HEADER}"; then
    set -- "$@" --set keep_host_header=true
fi

if [ -n "${PROXY_EXTRA_ARGS}" ]; then
    # shellcheck disable=SC2086
    set -- "$@" ${PROXY_EXTRA_ARGS}
fi

exec mitmdump "$@"
