import { Button, Chip, Link, Table, TableBody, TableCell, TableHead, TableRow } from '@mui/material'
import { Link as RouterLink } from 'react-router-dom'
import type { Artifact } from '../api/types'

export function ArtifactTable({ artifacts, onPreview }: { artifacts: Artifact[]; onPreview: (a: Artifact) => void }) {
  return (
    <Table size="small">
      <TableHead>
        <TableRow>
          <TableCell>Timestamp</TableCell>
          <TableCell>Artifact</TableCell>
          <TableCell>Kind</TableCell>
          <TableCell>Mime</TableCell>
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
            <TableCell>{artifact.mime || '-'}</TableCell>
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
