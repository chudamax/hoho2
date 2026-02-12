import { Card, CardContent, Grid, Link, Typography } from '@mui/material'
import { useCallback, useEffect, useState } from 'react'
import { Link as RouterLink } from 'react-router-dom'
import { api } from '../api/client'
import type { EventSummary, HoneypotSummary } from '../api/types'
import { EventFeed } from '../components/EventFeed'
import { useEventStream } from '../hooks/useEventStream'

export default function Dashboard() {
  const [honeypots, setHoneypots] = useState<HoneypotSummary[]>([])
  const [events, setEvents] = useState<EventSummary[]>([])

  useEffect(() => {
    api.honeypots().then(setHoneypots)
  }, [])

  const onEvent = useCallback((evt: EventSummary) => {
    setEvents((prev) => [evt, ...prev].slice(0, 500))
  }, [])

  useEventStream({}, onEvent)

  return (
    <Grid container spacing={2}>
      <Grid size={{ xs: 12, md: 7 }}>
        <Typography variant="h5" sx={{ mb: 1 }}>Honeypots</Typography>
        {honeypots.map((h) => (
          <Card key={h.honeypot_id} sx={{ mb: 1 }}>
            <CardContent>
              <Typography variant="h6">
                <Link component={RouterLink} to={`/ui/honeypots/${h.honeypot_id}`}>{h.honeypot_id}</Link>
              </Typography>
              <Typography variant="body2">Events: {h.events_count} · Sessions: {h.sessions_count}</Typography>
            </CardContent>
          </Card>
        ))}
      </Grid>
      <Grid size={{ xs: 12, md: 5 }}>
        <Typography variant="h5" sx={{ mb: 1 }}>Latest Live Events</Typography>
        <EventFeed events={events} />
      </Grid>
    </Grid>
  )
}
