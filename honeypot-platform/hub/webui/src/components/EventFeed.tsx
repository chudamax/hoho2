import { List, ListItem, ListItemText, Paper } from '@mui/material'
import dayjs from 'dayjs'
import type { EventSummary } from '../api/types'

export function EventFeed({ events }: { events: EventSummary[] }) {
  return (
    <Paper variant="outlined" sx={{ maxHeight: 480, overflow: 'auto' }}>
      <List dense>
        {events.map((event) => (
          <ListItem key={event.event_id}>
            <ListItemText
              primary={`${event.event_name} · ${event.verdict || 'unknown'} · ${event.component}`}
              secondary={`${dayjs(event.ts).format('HH:mm:ss')} · ${event.honeypot_id}/${event.session_id}`}
            />
          </ListItem>
        ))}
      </List>
    </Paper>
  )
}
