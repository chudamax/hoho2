#!/usr/bin/env sh
set -eu

: "${PROXY_LISTEN_HOST:=0.0.0.0}"
: "${PROXY_LISTEN_PORT:=3128}"
: "${PROXY_STACK_ID:=${HOHO_PACK_ID:-unknown-pack}}"
: "${PROXY_TLS_MITM_ENABLED:=false}"
: "${PROXY_CA_CERT_PATH:=/runtime/ca/egress-ca.crt}"
: "${PROXY_CA_KEY_PATH:=/runtime/ca/egress-ca.key}"
: "${PROXY_MITM_BUNDLE_PATH:=/runtime/ca/mitmproxy-ca.pem}"
: "${PROXY_MITM_CERT_PATH:=/runtime/ca/mitmproxy-ca-cert.pem}"

CONF_DIR="/artifacts/${PROXY_STACK_ID}/mitmproxy-conf"
CA_DIR="/artifacts/${PROXY_STACK_ID}/ca"
mkdir -p "${CONF_DIR}" "${CA_DIR}"

is_truthy() {
  value=$(printf '%s' "$1" | tr '[:upper:]' '[:lower:]')
  [ "${value}" = "true" ] || [ "${value}" = "1" ] || [ "${value}" = "yes" ] || [ "${value}" = "on" ]
}

if is_truthy "${PROXY_TLS_MITM_ENABLED}"; then
  for required in "${PROXY_MITM_CERT_PATH}" "${PROXY_MITM_BUNDLE_PATH}" "${PROXY_CA_CERT_PATH}" "${PROXY_CA_KEY_PATH}"; do
    if [ ! -s "${required}" ]; then
      echo "ERROR: TLS MITM is enabled but required runtime CA file is missing: ${required}" >&2
      exit 1
    fi
  done

  cp "${PROXY_MITM_CERT_PATH}" "${CONF_DIR}/mitmproxy-ca-cert.pem"
  cp "${PROXY_MITM_BUNDLE_PATH}" "${CONF_DIR}/mitmproxy-ca.pem"
  cp "${PROXY_CA_CERT_PATH}" "${CA_DIR}/egress-ca.crt"
  TLS_ARGS=""
else
  TLS_ARGS="--set connection_strategy=lazy"
fi

set -- \
  --mode regular \
  --listen-host "${PROXY_LISTEN_HOST}" \
  --listen-port "${PROXY_LISTEN_PORT}" \
  --set confdir="${CONF_DIR}" \
  -s /app/egress_capture_addon.py

if [ -n "${TLS_ARGS}" ]; then
  # shellcheck disable=SC2086
  set -- "$@" ${TLS_ARGS}
fi

mitmdump "$@" &
child=$!

wait "$child"
