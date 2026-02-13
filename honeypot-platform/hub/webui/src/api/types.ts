export type EventSummary = {
  event_id: string
  ts: string
  honeypot_id: string
  session_id: string
  event_name: string
  component: string
  verdict: string
  tags: string[]
  artifacts_count?: number
}

export type HoneypotSummary = {
  honeypot_id: string
  last_seen_ts: string
  sessions_count: number
  events_count: number
}

export type SessionSummary = {
  session_id: string
  agent_id: string
  started_ts: string
  last_seen_ts: string
}

export type Artifact = {
  artifact_id: string
  ts: string
  honeypot_id: string
  session_id: string
  event_id: string
  kind: string
  sha256: string
  size: number
  mime: string
  storage_ref: string
  meta: Record<string, unknown>
  detected_mime?: string
  detected_desc?: string
  guessed_ext?: string
}
