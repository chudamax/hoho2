# Telemetry Filters

Rules are ordered and first-match wins. If no rule matches, the default action is `keep`.

Supported operators: `eq`, `neq`, `in`, `contains`, `regex`, `gte`, `lte`, `exists`.

Example:
```yaml
telemetry:
  filters:
    emit:
      - name: drop_noise
        when:
          all:
            - field: event_name
              eq: http.request
            - field: request.path
              in: ["/favicon.ico", "/robots.txt"]
        action: drop
    forward:
      - name: keep_interesting
        when:
          any:
            - field: classification.verdict
              in: ["exploit", "postex", "alert", "enforcement"]
            - field: response.status_code
              gte: 400
        action: keep
      - name: drop_rest
        action: drop
```
