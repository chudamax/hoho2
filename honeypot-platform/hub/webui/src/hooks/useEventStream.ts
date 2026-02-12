import { useEffect } from 'react'
import type { EventSummary } from '../api/types'

export function useEventStream(filters: { honeypot_id?: string; session_id?: string; since_ts?: string }, onEvent: (evt: EventSummary) => void) {
  useEffect(() => {
    const params = new URLSearchParams()
    if (filters.honeypot_id) params.set('honeypot_id', filters.honeypot_id)
    if (filters.session_id) params.set('session_id', filters.session_id)
    if (filters.since_ts) params.set('since_ts', filters.since_ts)

    const es = new EventSource(`/api/v1/stream/events?${params.toString()}`)
    es.onmessage = (msg) => {
      onEvent(JSON.parse(msg.data) as EventSummary)
    }
    return () => es.close()
  }, [filters.honeypot_id, filters.session_id, filters.since_ts, onEvent])
}
