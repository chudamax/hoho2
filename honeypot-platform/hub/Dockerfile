FROM node:20-alpine AS webui-build
WORKDIR /webui
COPY webui/package.json webui/package-lock.json* ./
RUN if [ -f package-lock.json ]; then npm ci; else npm install; fi
COPY webui/ ./
RUN npm run build

FROM python:3.11-slim
WORKDIR /app
COPY app /app/app
COPY --from=webui-build /webui/dist /app/app/webui_dist
RUN pip install --no-cache-dir fastapi uvicorn jinja2
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
