# AGENTS.md (repo root)

## Honeypot layout (Simple Layout v1)
- Authoritative spec: `honeypot-platform/docs/DIRECTORY_LAYOUT.md`.
- Always use `honeypot_id == metadata.id`.
- Create packs only at `honeypot-platform/packs/{low,high}/<honeypot_id>.yaml`.
- Create docs only at `honeypot-platform/honeypots/{low,high}/<honeypot_id>/README.md`.
- Never create `.md` next to pack YAML files.
- Artifacts always go to `honeypot-platform/run/artifacts/<honeypot_id>/...`.
- Compose always goes to `honeypot-platform/deploy/compose/<honeypot_id>/docker-compose.yml`.
- Never create `honeypot-platform/run/artifacts/<runs-subtree>/**`.
- Never create non-canonical honeypot folders such as `honeypot-platform/honeypots/high/<cve-only>/`.

# Honeypots: low-interaction
- When asked to create a new low-interaction honeypot from a CVE, ALWAYS read:
  `honeypot-platform/docs/runbooks/low-interaction-honeypot-from-cve.md`
- Follow the runbook exactly: research -> derive request transcripts -> implement YAML pack -> validate/run -> document.

## Honeypots: high-interaction
- When asked to create a new high-interaction honeypot from a CVE, ALWAYS read:
  `honeypot-platform/docs/runbooks/high-interaction-honeypot-from-cve.md`
- Prioritize isolation + capture: pcap, proxy download capture, filesystem monitoring, process/audit logs.
- Provide a one-command reset script at `honeypot-platform/honeypots/high/<honeypot_id>/reset.sh`.
