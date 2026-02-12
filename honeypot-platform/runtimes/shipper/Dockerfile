FROM python:3.12-slim

WORKDIR /app

COPY packages/hoho_core /app/packages/hoho_core
COPY packages/hoho_runtime /app/packages/hoho_runtime

RUN pip install --no-cache-dir /app/packages/hoho_core /app/packages/hoho_runtime

ENTRYPOINT ["python", "-m", "hoho_runtime.cli", "ship", "--follow", "--artifacts-root", "/artifacts"]
