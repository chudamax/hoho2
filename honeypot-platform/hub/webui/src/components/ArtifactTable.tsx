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
          <TableCell>Timestamp</TableCell>
          <TableCell>Artifact</TableCell>
          <TableCell>Kind</TableCell>
          <TableCell>Type</TableCell>
          <TableCell>MIME</TableCell>
          <TableCell>Ext</TableCell>
          <TableCell>Size</TableCell>
          <TableCell>Actions</TableCell>
        </TableRow>
      </TableHead>
      <TableBody>
        {artifacts.map((artifact) => (
          <TableRow key={artifact.artifact_id}>
            <TableCell>{artifact.ts}</TableCell>
            <TableCell>
              <Link component={RouterLink} to={`/ui/events/${artifact.event_id}`}>{artifact.artifact_id}</Link>
            </TableCell>
            <TableCell><Chip label={artifact.kind || 'unknown'} size="small" /></TableCell>
            <TableCell>
              <Tooltip title={artifact.detected_desc || ''}>
                <span>{shortType(artifact.detected_desc)}</span>
              </Tooltip>
            </TableCell>
            <TableCell>
              <Chip label={artifact.detected_mime || artifact.mime || '-'} size="small" variant="outlined" />
            </TableCell>
            <TableCell>{artifact.guessed_ext || '-'}</TableCell>
            <TableCell>{artifact.size ?? '-'}</TableCell>
            <TableCell>
              <Button href={`/api/v1/artifacts/${encodeURIComponent(artifact.artifact_id)}/download`} size="small">Download</Button>
              <Button onClick={() => onPreview(artifact)} size="small">Preview</Button>
            </TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  )
}
