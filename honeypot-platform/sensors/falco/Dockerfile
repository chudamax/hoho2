# sensors/falco/Dockerfile
FROM falcosecurity/falco:0.39.1

USER root

RUN set -eux; \
    if command -v apt-get >/dev/null 2>&1; then \
        # Falco image adds download.falco.org repo but may not ship the GPG key -> apt update fails.
        # We don't need that repo for installing python.
        rm -f /etc/apt/sources.list.d/*falco* /etc/apt/sources.list.d/*falcosecurity* || true; \
        # Also remove any list that references download.falco.org, just in case
        grep -Rls "download.falco.org" /etc/apt/sources.list /etc/apt/sources.list.d 2>/dev/null | xargs -r rm -f || true; \
        apt-get update; \
        apt-get install -y --no-install-recommends python3 python3-pip ca-certificates; \
        rm -rf /var/lib/apt/lists/*; \
    else \
        echo "Expected apt-get in Falco base image, but not found"; \
        exit 1; \
    fi

WORKDIR /app

# Forwarder that converts Falco JSON alerts -> hoho events.jsonl
COPY forwarder.py /app/forwarder.py
COPY entrypoint.sh /app/entrypoint.sh

# If your forwarder talks to docker.sock, you likely want the docker SDK
RUN set -eux; \
    python3 -m pip install --no-cache-dir --break-system-packages docker requests; \
    chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
