import { Chip, Link, Paper, Table, TableBody, TableCell, TableHead, TableRow, Tooltip, Typography } from '@mui/material'
import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import { api } from '../api/client'
import type { EventArtifact, EventDetail } from '../api/types'

function artifactFsPath(artifact: EventArtifact): string {
  const meta = artifact.meta
  if (!meta || typeof meta !== 'object') {
    return artifact.storage_ref || '-'
  }

  const candidates = ['path', 'filepath', 'file_path', 'target_path', 'url', 'filename']
  for (const key of candidates) {
    const value = meta[key]
    if (typeof value === 'string' && value.length > 0) {
      return value
    }
  }
  return artifact.storage_ref || '-'
}

export default function EventDetailPage() {
  const { eventId = '' } = useParams()
  const [event, setEvent] = useState<EventDetail | null>(null)

  useEffect(() => {
    api.eventDetail(eventId).then(setEvent)
  }, [eventId])

  const artifacts = event?.artifacts || []

  const prettyType = (artifact: EventArtifact) => artifact.detected_desc || artifact.mime || '-'

  return (
    <>
      <Typography variant="h5" sx={{ mb: 2 }}>Event {eventId}</Typography>
      <Paper variant="outlined" sx={{ p: 2, mb: 2, overflowX: 'auto' }}>
        <pre style={{ margin: 0 }}>{JSON.stringify(event, null, 2)}</pre>
      </Paper>
      <Typography variant="h6">Artifacts</Typography>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>Kind</TableCell>
            <TableCell>SHA256</TableCell>
            <TableCell>Type</TableCell>
            <TableCell>MIME</TableCell>
            <TableCell>Ext</TableCell>
            <TableCell>Honeypot Path</TableCell>
            <TableCell>Download</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {artifacts.map((a, i) => (
            <TableRow key={`${a.sha256 || i}`}>
              <TableCell>{a.kind || '-'}</TableCell>
              <TableCell>{a.sha256 || '-'}</TableCell>
              <TableCell>
                <Tooltip title={prettyType(a)}>
                  <span>{prettyType(a).slice(0, 64)}</span>
                </Tooltip>
              </TableCell>
              <TableCell>
                <Chip size="small" label={a.detected_mime || a.mime || 'unknown'} />
              </TableCell>
              <TableCell>{a.guessed_ext || '-'}</TableCell>
              <TableCell>
                <Tooltip title={artifactFsPath(a)}>
                  <span>{artifactFsPath(a).slice(0, 72)}</span>
                </Tooltip>
              </TableCell>
              <TableCell>
                {a.sha256 ? <Link href={`/blobs/${a.sha256}`}>Download</Link> : '-'}
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </>
  )
}
