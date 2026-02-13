FROM node:20-alpine AS webui-build
WORKDIR /webui
COPY webui/package.json webui/package-lock.json* ./
RUN if [ -f package-lock.json ]; then npm ci; else npm install; fi
COPY webui/ ./
RUN npm run build

FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN apt-get update && apt-get install -y --no-install-recommends libmagic1 && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY app /app/app
COPY --from=webui-build /webui/dist /app/app/webui_dist
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
