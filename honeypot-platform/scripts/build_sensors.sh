#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

mkdir -p sensors/fsmon/packages/
cp -r packages/hoho_core sensors/fsmon/packages/hoho_core
docker build -t hoho/sensor-fsmon:latest sensors/fsmon

mkdir -p sensors/http_proxy/packages/
cp -r packages/hoho_core sensors/http_proxy/packages/hoho_core
docker build -t hoho/sensor-http-proxy:latest sensors/http_proxy

mkdir -p sensors/pcap/packages/
cp -r packages/hoho_core sensors/pcap/packages/hoho_core
docker build -t hoho/sensor-pcap:latest sensors/pcap

mkdir -p sensors/egress_proxy/packages/
cp -r packages/hoho_core sensors/egress_proxy/packages/hoho_core
docker build -t hoho/sensor-egress-proxy:latest sensors/egress_proxy

mkdir -p sensors/falco/packages/
cp -r packages/hoho_core sensors/falco/packages/hoho_core
docker build -t hoho/sensor-falco:latest sensors/falco

# low interaction runtime
docker build -t hoho/low-runtime:latest -f runtimes/low_runtime/Dockerfile .

# docker build -t hoho/sensor-fsmon:latest        -f sensors/fsmon/        .
# docker build -t hoho/sensor-http-proxy:latest   -f sensors/http_proxy/Dockerfile   .
# docker build -t hoho/sensor-egress-proxy:latest -f sensors/egress_proxy/Dockerfile .
# docker build -t hoho/sensor-pcap:latest         -f sensors/pcap/Dockerfile         .
# docker build -t hoho/sensor-falco:latest        -f sensors/falco/Dockerfile        .

# docker build -t hoho/low-runtime:latest -f runtimes/low_runtime/Dockerfile .