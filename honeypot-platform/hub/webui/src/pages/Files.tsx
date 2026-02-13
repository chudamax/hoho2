import { Box, Button, Checkbox, Dialog, DialogContent, DialogTitle, FormControlLabel, MenuItem, Stack, TextField, Typography } from '@mui/material'
import { useEffect, useMemo, useState } from 'react'
import { api } from '../api/client'
import type { Artifact } from '../api/types'
import { ArtifactTable } from '../components/ArtifactTable'

const MAX_PREVIEW = 64 * 1024

export default function FilesPage() {
  const [artifacts, setArtifacts] = useState<Artifact[]>([])
  const [filters, setFilters] = useState({ honeypot_id: '', session_id: '', kind: '', mime_prefix: '', detected_mime_prefix: '', q: '' })
  const [sortBy, setSortBy] = useState<'ts' | 'size' | 'detected_mime'>('ts')
  const [sortDir, setSortDir] = useState<'asc' | 'desc'>('desc')
  const [preview, setPreview] = useState<{ artifact: Artifact; body: string } | null>(null)
  const [httpOnly, setHttpOnly] = useState(false)

  const load = () => {
    const p = Object.fromEntries(Object.entries(filters).filter(([, v]) => Boolean(v))) as Record<string, string>
    api.artifacts(p).then(setArtifacts)
  }

  useEffect(() => {
    load()
  }, [])

  const onPreview = async (artifact: Artifact) => {
    if (!artifact.sha256) return
    const mime = artifact.detected_mime || artifact.mime
    if (mime?.startsWith('image/')) {
      setPreview({ artifact, body: '' })
      return
    }
    if (mime?.startsWith('text/') || mime?.startsWith('application/json')) {
      const res = await fetch(`/blobs/${artifact.sha256}`)
      const text = (await res.text()).slice(0, MAX_PREVIEW)
      setPreview({ artifact, body: text })
      return
    }
    setPreview({ artifact, body: 'No preview available for this mime type' })
  }

  const sortedArtifacts = useMemo(() => {
    const copied = [...artifacts].filter((a) => !httpOnly || Boolean(a.http_summary?.method || a.http_summary?.path))
    copied.sort((a, b) => {
      let left = ''
      let right = ''
      if (sortBy === 'size') {
        left = String(a.size ?? 0)
        right = String(b.size ?? 0)
      } else if (sortBy === 'detected_mime') {
        left = a.detected_mime || a.mime || ''
        right = b.detected_mime || b.mime || ''
      } else {
        left = a.ts || ''
        right = b.ts || ''
      }
      const base = left.localeCompare(right, undefined, { numeric: true })
      return sortDir === 'asc' ? base : -base
    })
    return copied
  }, [artifacts, sortBy, sortDir, httpOnly])

  return (
    <>
      <Typography variant="h5" sx={{ mb: 1 }}>Artifacts</Typography>
      <Stack direction="row" spacing={1} sx={{ mb: 2, flexWrap: 'wrap' }}>
        {Object.keys(filters).map((key) => (
          <TextField
            key={key}
            size="small"
            label={key}
            value={filters[key as keyof typeof filters]}
            onChange={(e) => setFilters((f) => ({ ...f, [key]: e.target.value }))}
          />
        ))}
        <TextField select size="small" label="sort_by" value={sortBy} onChange={(e) => setSortBy(e.target.value as typeof sortBy)}>
          <MenuItem value="ts">timestamp</MenuItem>
          <MenuItem value="size">size</MenuItem>
          <MenuItem value="detected_mime">detected_mime</MenuItem>
        </TextField>
        <TextField select size="small" label="sort_dir" value={sortDir} onChange={(e) => setSortDir(e.target.value as typeof sortDir)}>
          <MenuItem value="desc">desc</MenuItem>
          <MenuItem value="asc">asc</MenuItem>
        </TextField>
        <FormControlLabel control={<Checkbox checked={httpOnly} onChange={(e) => setHttpOnly(e.target.checked)} />} label="HTTP only" />
        <Button variant="contained" onClick={load}>Apply</Button>
      </Stack>
      <ArtifactTable artifacts={sortedArtifacts} onPreview={onPreview} />

      <Dialog open={Boolean(preview)} onClose={() => setPreview(null)} maxWidth="md" fullWidth>
        <DialogTitle>Preview</DialogTitle>
        <DialogContent>
          {preview && (preview.artifact.detected_mime || preview.artifact.mime)?.startsWith('image/') ? (
            <Box component="img" src={`/blobs/${preview.artifact.sha256}`} sx={{ maxWidth: '100%' }} />
          ) : (
            <pre>{preview?.body}</pre>
          )}
        </DialogContent>
      </Dialog>
    </>
  )
}
