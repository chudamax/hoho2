FROM python:3.11-slim
WORKDIR /app
COPY fsmon/fsmon.py /app/fsmon.py
COPY fsmon/rules.schema.json /app/rules.schema.json
COPY entrypoint.sh /entrypoint.sh
RUN pip install --no-cache-dir watchdog && chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
