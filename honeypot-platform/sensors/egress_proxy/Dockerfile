FROM python:3.11-slim
WORKDIR /app
COPY proxy/egress_capture_addon.py /app/egress_capture_addon.py
COPY proxy/gen_ca.py /app/gen_ca.py
COPY entrypoint.sh /entrypoint.sh
RUN pip install --no-cache-dir mitmproxy && chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
