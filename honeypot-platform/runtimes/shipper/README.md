# HOHO Shipper Runner

Build:

```bash
docker build -t hoho/shipper:latest -f honeypot-platform/runtimes/shipper/Dockerfile honeypot-platform
```

Run:

```bash
docker run --rm \
  --env-file honeypot-platform/.env \
  -v "$(pwd)/honeypot-platform/run/artifacts:/artifacts" \
  hoho/shipper:latest
```
