import { Chip, Link, Table, TableBody, TableCell, TableHead, TableRow, Tooltip } from '@mui/material'
import dayjs from 'dayjs'
import { Link as RouterLink } from 'react-router-dom'
import type { EventSummary } from '../api/types'

function statusColor(code?: number | null): 'default' | 'success' | 'warning' | 'error' {
  if (!code) return 'default'
  if (code < 300) return 'success'
  if (code < 400) return 'default'
  if (code < 500) return 'warning'
  return 'error'
}

export function EventTable({ events }: { events: EventSummary[] }) {
  return (
    <Table size="small">
      <TableHead>
        <TableRow>
          <TableCell>Timestamp</TableCell>
          <TableCell>Event</TableCell>
          <TableCell>Action</TableCell>
          <TableCell>Source</TableCell>
          <TableCell>Component</TableCell>
          <TableCell>Verdict</TableCell>
          <TableCell>Tags</TableCell>
          <TableCell>Artifacts</TableCell>
        </TableRow>
      </TableHead>
      <TableBody>
        {events.map((event) => (
          <TableRow key={event.event_id}>
            <TableCell>{dayjs(event.ts).format('YYYY-MM-DD HH:mm:ss')}</TableCell>
            <TableCell>
              <Link component={RouterLink} to={`/ui/events/${event.event_id}`}>{event.event_name}</Link>
            </TableCell>
            <TableCell>
              <Link component={RouterLink} to={`/ui/events/${event.event_id}`} sx={{ fontFamily: 'monospace' }}>
                {event.action || event.event_name || '-'}
              </Link>
              <Tooltip title={event.event_name}>
                <span style={{ marginLeft: 8, opacity: 0.65 }}>{event.event_name}</span>
              </Tooltip>
              {!!event.http_summary?.status_code && <Chip size="small" color={statusColor(event.http_summary.status_code)} label={event.http_summary.status_code} sx={{ ml: 0.5 }} />}
            </TableCell>
            <TableCell>
              {event.src_summary?.ip ? `${event.src_summary.ip}:${event.src_summary.port || '-'}` : '-'}
              {!!event.src_summary?.forwarded_for_count && event.src_summary.forwarded_for_count > 0 && (
                <Tooltip title={event.src_summary.forwarded_for_first || ''}>
                  <Chip size="small" sx={{ ml: 0.5 }} label={`XFF: ${event.src_summary.forwarded_for_first} (+${Math.max((event.src_summary.forwarded_for_count || 1) - 1, 0)})`} />
                </Tooltip>
              )}
            </TableCell>
            <TableCell>{event.component}</TableCell>
            <TableCell>{event.verdict || '-'}</TableCell>
            <TableCell>
              {event.tags?.slice(0, 3).map((tag) => (
                <Chip key={tag} size="small" label={tag} sx={{ mr: 0.5 }} />
              ))}
            </TableCell>
            <TableCell>
              {event.artifact_badges?.map((badge) => (
                <Chip key={badge} size="small" label={badge.toUpperCase().slice(0, 4)} sx={{ mr: 0.5 }} />
              ))}
            </TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  )
}
