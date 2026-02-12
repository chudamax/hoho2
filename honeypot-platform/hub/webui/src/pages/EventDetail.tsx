import { Link, Paper, Typography } from '@mui/material'
import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import { api } from '../api/client'

export default function EventDetailPage() {
  const { eventId = '' } = useParams()
  const [event, setEvent] = useState<Record<string, unknown> | null>(null)

  useEffect(() => {
    api.eventDetail(eventId).then(setEvent)
  }, [eventId])

  const artifacts = (event?.artifacts as Array<Record<string, unknown>> | undefined) || []

  return (
    <>
      <Typography variant="h5" sx={{ mb: 2 }}>Event {eventId}</Typography>
      <Paper variant="outlined" sx={{ p: 2, mb: 2, overflowX: 'auto' }}>
        <pre style={{ margin: 0 }}>{JSON.stringify(event, null, 2)}</pre>
      </Paper>
      <Typography variant="h6">Artifacts</Typography>
      {artifacts.map((a, i) => (
        <div key={i}>
          <Link href={`/blobs/${a.sha256}`}>{String(a.kind || 'artifact')} · {String(a.sha256 || '')}</Link>
        </div>
      ))}
    </>
  )
}
