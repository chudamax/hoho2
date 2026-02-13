import { Chip, List, ListItem, ListItemText, Paper, Stack } from '@mui/material'
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
              secondary={
                <Stack direction="row" spacing={1} alignItems="center" flexWrap="wrap">
                  <span>{`${dayjs(event.ts).format('HH:mm:ss')} · ${event.honeypot_id}/${event.session_id}`}</span>
                  {event.artifact_badges?.map((badge) => (
                    <Chip key={`${event.event_id}-${badge}`} size="small" label={badge.toUpperCase().slice(0, 4)} />
                  ))}
                </Stack>
              }
            />
          </ListItem>
        ))}
      </List>
    </Paper>
  )
}
