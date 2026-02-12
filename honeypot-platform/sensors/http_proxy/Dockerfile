FROM python:3.11-slim
WORKDIR /app
COPY proxy/capture_addon.py /app/capture_addon.py
COPY entrypoint.sh /entrypoint.sh
COPY packages/hoho_core /src/hoho_core

RUN pip install --no-cache-dir /src/hoho_core mitmproxy PyYAML jsonschema && chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
