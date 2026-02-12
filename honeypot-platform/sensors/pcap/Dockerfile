FROM python:3.11-slim
RUN apt update && apt install -y --no-install-recommends tcpdump
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
COPY packages/hoho_core /src/hoho_core
RUN pip install --no-cache-dir /src/hoho_core

ENTRYPOINT ["/entrypoint.sh"]
