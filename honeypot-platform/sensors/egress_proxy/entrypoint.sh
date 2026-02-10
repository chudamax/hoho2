#!/usr/bin/env sh
set -eu

: "${PROXY_LISTEN_HOST:=0.0.0.0}"
: "${PROXY_LISTEN_PORT:=3128}"
: "${PROXY_STACK_ID:=${HOHO_PACK_ID:-unknown-pack}}"
: "${PROXY_TLS_MITM_ENABLED:=false}"
: "${PROXY_CA_INSTALL_ENABLED:=true}"
: "${PROXY_CA_INSTALL_MODE:=auto}"
: "${PROXY_CUSTOM_CERT_PATH:=}"
: "${PROXY_CUSTOM_KEY_PATH:=}"

CONF_DIR="/artifacts/${PROXY_STACK_ID}/mitmproxy-conf"
CA_DIR="/artifacts/${PROXY_STACK_ID}/ca"
mkdir -p "${CONF_DIR}" "${CA_DIR}"

mode=$(printf '%s' "${PROXY_TLS_MITM_ENABLED}" | tr '[:upper:]' '[:lower:]')
if [ "${mode}" = "true" ] || [ "${mode}" = "1" ] || [ "${mode}" = "yes" ] || [ "${mode}" = "on" ]; then
  TLS_ARGS=""
else
  TLS_ARGS="--set connection_strategy=lazy"
fi

if [ "${PROXY_CA_INSTALL_MODE}" = "custom" ] && [ -n "${PROXY_CUSTOM_CERT_PATH}" ] && [ -n "${PROXY_CUSTOM_KEY_PATH}" ]; then
  cp "${PROXY_CUSTOM_CERT_PATH}" "${CONF_DIR}/mitmproxy-ca-cert.pem"
  cp "${PROXY_CUSTOM_KEY_PATH}" "${CONF_DIR}/mitmproxy-ca.pem"
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

for _ in $(seq 1 30); do
  if [ -f "${CONF_DIR}/mitmproxy-ca-cert.pem" ]; then
    cp "${CONF_DIR}/mitmproxy-ca-cert.pem" "${CA_DIR}/egress-ca.crt"
    break
  fi
  sleep 1
done

wait "$child"
