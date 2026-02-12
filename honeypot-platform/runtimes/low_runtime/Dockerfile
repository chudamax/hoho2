FROM python:3.11-slim

WORKDIR /app

COPY packages/hoho_core /src/hoho_core
COPY packages/hoho_runtime /src/hoho_runtime

RUN pip install --no-cache-dir /src/hoho_core /src/hoho_runtime

ENTRYPOINT ["python", "-m", "hoho_runtime.container.low_runtime"]
