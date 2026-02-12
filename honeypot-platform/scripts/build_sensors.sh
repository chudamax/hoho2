#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

docker build -t hoho/sensor-fsmon:latest sensors/fsmon
docker build -t hoho/sensor-http-proxy:latest sensors/http_proxy
docker build -t hoho/sensor-pcap:latest sensors/pcap
docker build -t hoho/sensor-egress-proxy:latest sensors/egress_proxy
docker build -t hoho/sensor-falco:latest sensors/falco

# low interaction runtime
docker build -t hoho/low-runtime:latest -f runtimes/low_runtime/Dockerfile .
