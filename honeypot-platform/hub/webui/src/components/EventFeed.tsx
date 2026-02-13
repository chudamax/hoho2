import { Chip, List, ListItem, ListItemText, Paper, Stack, Tooltip } from '@mui/material'
import dayjs from 'dayjs'
import type { EventSummary } from '../api/types'

export function EventFeed({ events }: { events: EventSummary[] }) {
  return (
    <Paper variant="outlined" sx={{ maxHeight: 480, overflow: 'auto' }}>
      <List dense>
        {events.map((event) => (
          <ListItem key={event.event_id}>
            <ListItemText
              primary={`${event.action || event.event_name || '-'} · ${event.verdict || 'unknown'} · ${event.component}`}
              secondary={
                <Stack direction="row" spacing={1} alignItems="center" flexWrap="wrap">
                  <span>{`${dayjs(event.ts).format('HH:mm:ss')} · ${event.honeypot_id}/${event.session_id}`}</span>
                  <Tooltip title={event.event_name}><Chip size="small" variant="outlined" label={`event: ${event.event_name}`} /></Tooltip>
                  {event.http_summary?.status_code && <Chip size="small" label={event.http_summary.status_code} />}
                  {event.http_summary?.host && <Chip size="small" variant="outlined" label={event.http_summary.host} />}
                  {event.src_summary?.ip && <Chip size="small" label={`${event.src_summary.ip}:${event.src_summary.port || '-'}`} />}
                  {!!event.src_summary?.forwarded_for_count && (
                    <Chip size="small" label={`XFF: ${event.src_summary.forwarded_for_first} (+${Math.max((event.src_summary.forwarded_for_count || 1) - 1, 0)})`} />
                  )}
                  {event.http_summary?.user_agent && (
                    <Tooltip title={event.http_summary.user_agent}>
                      <Chip size="small" variant="outlined" label={event.http_summary.user_agent} />
                    </Tooltip>
                  )}
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
