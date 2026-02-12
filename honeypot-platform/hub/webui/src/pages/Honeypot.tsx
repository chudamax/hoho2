import { List, ListItemButton, ListItemText, Typography } from '@mui/material'
import { useCallback, useEffect, useState } from 'react'
import { Link as RouterLink, useParams } from 'react-router-dom'
import { api } from '../api/client'
import type { EventSummary, SessionSummary } from '../api/types'
import { EventFeed } from '../components/EventFeed'
import { useEventStream } from '../hooks/useEventStream'

export default function HoneypotPage() {
  const { honeypotId = '' } = useParams()
  const [sessions, setSessions] = useState<SessionSummary[]>([])
  const [events, setEvents] = useState<EventSummary[]>([])

  useEffect(() => {
    api.sessions(honeypotId).then(setSessions)
  }, [honeypotId])

  const onEvent = useCallback((evt: EventSummary) => {
    setEvents((prev) => [evt, ...prev].slice(0, 500))
  }, [])

  useEventStream({ honeypot_id: honeypotId }, onEvent)

  return (
    <>
      <Typography variant="h5" sx={{ mb: 1 }}>{honeypotId}</Typography>
      <Typography variant="h6">Sessions</Typography>
      <List dense>
        {sessions.map((s) => (
          <ListItemButton key={s.session_id} component={RouterLink} to={`/ui/honeypots/${honeypotId}/sessions/${s.session_id}`}>
            <ListItemText primary={s.session_id} secondary={`${s.agent_id || 'unknown'} · ${s.last_seen_ts}`} />
          </ListItemButton>
        ))}
      </List>
      <Typography variant="h6">Live feed</Typography>
      <EventFeed events={events} />
    </>
  )
}
