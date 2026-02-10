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

is_truthy() {
  value=$(printf '%s' "$1" | tr '[:upper:]' '[:lower:]')
  [ "${value}" = "true" ] || [ "${value}" = "1" ] || [ "${value}" = "yes" ] || [ "${value}" = "on" ]
}

if is_truthy "${PROXY_TLS_MITM_ENABLED}"; then
  TLS_ARGS=""
else
  TLS_ARGS="--set connection_strategy=lazy"
fi

CA_MODE=$(printf '%s' "${PROXY_CA_INSTALL_MODE}" | tr '[:upper:]' '[:lower:]')
CA_READY=0
if is_truthy "${PROXY_TLS_MITM_ENABLED}" && is_truthy "${PROXY_CA_INSTALL_ENABLED}" && [ "${CA_MODE}" != "off" ]; then
  case "${CA_MODE}" in
    custom)
      if [ -n "${PROXY_CUSTOM_CERT_PATH}" ] && [ -n "${PROXY_CUSTOM_KEY_PATH}" ]; then
        cp "${PROXY_CUSTOM_CERT_PATH}" "${CONF_DIR}/mitmproxy-ca-cert.pem"
        cp "${PROXY_CUSTOM_KEY_PATH}" "${CONF_DIR}/mitmproxy-ca.pem"
        cp "${CONF_DIR}/mitmproxy-ca-cert.pem" "${CA_DIR}/egress-ca.crt"
        echo "Using custom CA from ${PROXY_CUSTOM_CERT_PATH}"
        CA_READY=1
      else
        echo "WARN: PROXY_CA_INSTALL_MODE=custom but custom cert/key paths are missing"
      fi
      ;;
    auto)
      if [ ! -s "${CONF_DIR}/mitmproxy-ca-cert.pem" ]; then
        if python /app/gen_ca.py "${CONF_DIR}"; then
          echo "Generated CA in ${CONF_DIR}"
        else
          echo "WARN: failed to generate CA via gen_ca.py; falling back to mitmproxy CA generation"
        fi
      fi
      if [ -s "${CONF_DIR}/mitmproxy-ca-cert.pem" ]; then
        cp "${CONF_DIR}/mitmproxy-ca-cert.pem" "${CA_DIR}/egress-ca.crt"
        echo "Exported CA to ${CA_DIR}/egress-ca.crt"
        CA_READY=1
      fi
      ;;
    *)
      echo "WARN: unknown PROXY_CA_INSTALL_MODE=${PROXY_CA_INSTALL_MODE}; skipping early CA export"
      ;;
  esac
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

if is_truthy "${PROXY_TLS_MITM_ENABLED}" && is_truthy "${PROXY_CA_INSTALL_ENABLED}" && [ "${CA_MODE}" != "off" ] && [ "${CA_READY}" -eq 0 ]; then
  for _ in $(seq 1 30); do
    if [ -s "${CONF_DIR}/mitmproxy-ca-cert.pem" ]; then
      cp "${CONF_DIR}/mitmproxy-ca-cert.pem" "${CA_DIR}/egress-ca.crt"
      echo "Exported fallback CA to ${CA_DIR}/egress-ca.crt"
      break
    fi
    sleep 1
  done
fi

wait "$child"
