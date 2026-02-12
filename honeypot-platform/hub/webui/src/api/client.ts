import type { Artifact, EventSummary, HoneypotSummary, SessionSummary } from './types'

async function getJson<T>(url: string): Promise<T> {
  const res = await fetch(url)
  if (!res.ok) throw new Error(`request failed: ${res.status}`)
  return res.json() as Promise<T>
}

export const api = {
  honeypots: () => getJson<HoneypotSummary[]>('/api/v1/honeypots'),
  sessions: (honeypotId: string) => getJson<SessionSummary[]>(`/api/v1/honeypots/${encodeURIComponent(honeypotId)}/sessions`),
  sessionEvents: (honeypotId: string, sessionId: string, beforeTs?: string) => {
    const params = new URLSearchParams({ limit: '200' })
    if (beforeTs) params.set('before_ts', beforeTs)
    return getJson<EventSummary[]>(`/api/v1/honeypots/${encodeURIComponent(honeypotId)}/sessions/${encodeURIComponent(sessionId)}/events?${params.toString()}`)
  },
  eventDetail: (eventId: string) => getJson<Record<string, unknown>>(`/api/v1/events/${encodeURIComponent(eventId)}`),
  artifacts: (params: Record<string, string>) => getJson<Artifact[]>(`/api/v1/artifacts?${new URLSearchParams(params).toString()}`),
}
