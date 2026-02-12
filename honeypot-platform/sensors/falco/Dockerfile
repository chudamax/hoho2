FROM falcosecurity/falco:0.39.1

USER root
RUN apk add --no-cache python3 py3-pip

WORKDIR /app
COPY entrypoint.sh /app/entrypoint.sh
COPY forwarder.py /app/forwarder.py
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
