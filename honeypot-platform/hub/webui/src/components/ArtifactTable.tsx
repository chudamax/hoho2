import { Button, Chip, Link, Table, TableBody, TableCell, TableHead, TableRow, Tooltip } from '@mui/material'
import { Link as RouterLink } from 'react-router-dom'
import type { Artifact } from '../api/types'

function shortType(desc?: string) {
  if (!desc) return '-'
  return desc.length > 64 ? `${desc.slice(0, 61)}...` : desc
}

export function ArtifactTable({ artifacts, onPreview }: { artifacts: Artifact[]; onPreview: (a: Artifact) => void }) {
  return (
    <Table size="small">
      <TableHead>
        <TableRow>
          <TableCell>Timestamp</TableCell><TableCell>Artifact</TableCell><TableCell>Kind</TableCell><TableCell>HTTP</TableCell><TableCell>Status</TableCell><TableCell>Host</TableCell><TableCell>User-Agent</TableCell><TableCell>Source</TableCell><TableCell>XFF</TableCell><TableCell>Type</TableCell><TableCell>MIME</TableCell><TableCell>Ext</TableCell><TableCell>Size</TableCell><TableCell>Actions</TableCell>
        </TableRow>
      </TableHead>
      <TableBody>
        {artifacts.map((artifact) => (
          <TableRow key={artifact.artifact_id}>
            <TableCell>{artifact.ts}</TableCell>
            <TableCell><Link component={RouterLink} to={`/ui/events/${artifact.event_id}`}>{artifact.artifact_id}</Link></TableCell>
            <TableCell><Chip label={artifact.kind || 'unknown'} size="small" /></TableCell>
            <TableCell>{artifact.http_summary?.method ? <Link component={RouterLink} to={`/ui/events/${artifact.event_id}`} sx={{ fontFamily: 'monospace' }}>{`${artifact.http_summary?.method || '-'} ${artifact.http_summary?.path || '-'}`}</Link> : '-'}</TableCell>
            <TableCell>{artifact.http_summary?.status_code || '-'}</TableCell>
            <TableCell>{artifact.http_summary?.host || '-'}</TableCell>
            <TableCell><Tooltip title={artifact.http_summary?.user_agent || ''}><span>{artifact.http_summary?.user_agent || '-'}</span></Tooltip></TableCell>
            <TableCell>{artifact.src_summary?.ip ? `${artifact.src_summary.ip}:${artifact.src_summary.port || '-'}` : '-'}</TableCell>
            <TableCell>{artifact.src_summary?.forwarded_for_count ? `${artifact.src_summary.forwarded_for_first} (+${Math.max((artifact.src_summary.forwarded_for_count || 1) - 1, 0)})` : '-'}</TableCell>
            <TableCell><Tooltip title={artifact.detected_desc || ''}><span>{shortType(artifact.detected_desc)}</span></Tooltip></TableCell>
            <TableCell><Chip label={artifact.detected_mime || artifact.mime || '-'} size="small" variant="outlined" /></TableCell>
            <TableCell>{artifact.guessed_ext || '-'}</TableCell>
            <TableCell>{artifact.size ?? '-'}</TableCell>
            <TableCell><Button href={`/api/v1/artifacts/${encodeURIComponent(artifact.artifact_id)}/download`} size="small">Download</Button><Button onClick={() => onPreview(artifact)} size="small">Preview</Button></TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  )
}
