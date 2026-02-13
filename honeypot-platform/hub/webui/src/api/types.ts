export type HttpSummary = {
  method?: string | null
  path?: string | null
  status_code?: number | null
  host?: string | null
  user_agent?: string | null
}

export type SrcSummary = {
  ip?: string | null
  port?: number | null
  forwarded_for_first?: string | null
  forwarded_for_count?: number
  forwarded_for?: string[]
}

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
  artifact_badges?: string[]
  http_summary?: HttpSummary
  src_summary?: SrcSummary
}

export type EventArtifact = {
  kind?: string
  sha256?: string
  mime?: string
  storage_ref?: string
  meta?: Record<string, unknown>
  detected_mime?: string
  detected_desc?: string
  guessed_ext?: string
}

export type EventDetail = {
  event: {
    event_id?: string
    artifacts?: EventArtifact[]
    [key: string]: unknown
  }
  http_summary?: HttpSummary
  src_summary?: SrcSummary
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
  http_summary?: HttpSummary
  src_summary?: SrcSummary
}
