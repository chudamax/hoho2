# AGENTS.md (repo root)

# Honeypots: low-interaction
- When asked to create a new low-interaction honeypot from a CVE, ALWAYS read:
  honeypot-platform/docs/runbooks/low-interaction-honeypot-from-cve.md
- Follow the runbook exactly: research -> derive request transcripts -> implement YAML pack -> validate/run -> document.


## Honeypots: high-interaction
- When asked to create a new high-interaction honeypot from a CVE, ALWAYS read:
  docs/runbooks/high-interaction-honeypot-from-cve.md
- Prioritize isolation + capture: pcap, proxy download capture, filesystem monitoring, process/audit logs.
- Provide a one-command reset that creates a new session artifact folder.