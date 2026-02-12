import { Button, Stack, Typography } from '@mui/material'
import { useCallback, useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import { api } from '../api/client'
import type { EventSummary } from '../api/types'
import { EventTable } from '../components/EventTable'
import { useEventStream } from '../hooks/useEventStream'

export default function SessionPage() {
  const { honeypotId = '', sessionId = '' } = useParams()
  const [events, setEvents] = useState<EventSummary[]>([])

  useEffect(() => {
    api.sessionEvents(honeypotId, sessionId).then(setEvents)
  }, [honeypotId, sessionId])

  const onEvent = useCallback((evt: EventSummary) => {
    setEvents((prev) => [evt, ...prev.filter((e) => e.event_id !== evt.event_id)].slice(0, 500))
  }, [])

  useEventStream({ honeypot_id: honeypotId, session_id: sessionId }, onEvent)

  const loadMore = async () => {
    const tail = events[events.length - 1]
    const more = await api.sessionEvents(honeypotId, sessionId, tail?.ts)
    setEvents((prev) => [...prev, ...more])
  }

  return (
    <>
      <Typography variant="h5" sx={{ mb: 2 }}>{honeypotId} / {sessionId}</Typography>
      <EventTable events={events} />
      <Stack direction="row" sx={{ mt: 2 }}>
        <Button onClick={loadMore} variant="outlined">Load older</Button>
      </Stack>
    </>
  )
}
