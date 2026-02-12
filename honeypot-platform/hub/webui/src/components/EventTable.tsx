import { Chip, Link, Table, TableBody, TableCell, TableHead, TableRow } from '@mui/material'
import dayjs from 'dayjs'
import { Link as RouterLink } from 'react-router-dom'
import type { EventSummary } from '../api/types'

export function EventTable({ events }: { events: EventSummary[] }) {
  return (
    <Table size="small">
      <TableHead>
        <TableRow>
          <TableCell>Timestamp</TableCell>
          <TableCell>Event</TableCell>
          <TableCell>Component</TableCell>
          <TableCell>Verdict</TableCell>
          <TableCell>Tags</TableCell>
        </TableRow>
      </TableHead>
      <TableBody>
        {events.map((event) => (
          <TableRow key={event.event_id}>
            <TableCell>{dayjs(event.ts).format('YYYY-MM-DD HH:mm:ss')}</TableCell>
            <TableCell>
              <Link component={RouterLink} to={`/ui/events/${event.event_id}`}>{event.event_name}</Link>
            </TableCell>
            <TableCell>{event.component}</TableCell>
            <TableCell>{event.verdict || '-'}</TableCell>
            <TableCell>
              {event.tags?.slice(0, 3).map((tag) => (
                <Chip key={tag} size="small" label={tag} sx={{ mr: 0.5 }} />
              ))}
            </TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  )
}
