import { Box, Button, Dialog, DialogContent, DialogTitle, Stack, TextField, Typography } from '@mui/material'
import { useEffect, useState } from 'react'
import { api } from '../api/client'
import type { Artifact } from '../api/types'
import { ArtifactTable } from '../components/ArtifactTable'

const MAX_PREVIEW = 64 * 1024

export default function FilesPage() {
  const [artifacts, setArtifacts] = useState<Artifact[]>([])
  const [filters, setFilters] = useState({ honeypot_id: '', session_id: '', kind: '', mime_prefix: '', q: '' })
  const [preview, setPreview] = useState<{ artifact: Artifact; body: string } | null>(null)

  const load = () => {
    const p = Object.fromEntries(Object.entries(filters).filter(([, v]) => Boolean(v))) as Record<string, string>
    api.artifacts(p).then(setArtifacts)
  }

  useEffect(() => {
    load()
  }, [])

  const onPreview = async (artifact: Artifact) => {
    if (!artifact.sha256) return
    if (artifact.mime?.startsWith('image/')) {
      setPreview({ artifact, body: '' })
      return
    }
    if (artifact.mime?.startsWith('text/') || artifact.mime?.startsWith('application/json')) {
      const res = await fetch(`/blobs/${artifact.sha256}`)
      const text = (await res.text()).slice(0, MAX_PREVIEW)
      setPreview({ artifact, body: text })
      return
    }
    setPreview({ artifact, body: 'No preview available for this mime type' })
  }

  return (
    <>
      <Typography variant="h5" sx={{ mb: 1 }}>Artifacts</Typography>
      <Stack direction="row" spacing={1} sx={{ mb: 2 }}>
        {Object.keys(filters).map((key) => (
          <TextField
            key={key}
            size="small"
            label={key}
            value={filters[key as keyof typeof filters]}
            onChange={(e) => setFilters((f) => ({ ...f, [key]: e.target.value }))}
          />
        ))}
        <Button variant="contained" onClick={load}>Apply</Button>
      </Stack>
      <ArtifactTable artifacts={artifacts} onPreview={onPreview} />

      <Dialog open={Boolean(preview)} onClose={() => setPreview(null)} maxWidth="md" fullWidth>
        <DialogTitle>Preview</DialogTitle>
        <DialogContent>
          {preview && preview.artifact.mime?.startsWith('image/') ? (
            <Box component="img" src={`/blobs/${preview.artifact.sha256}`} sx={{ maxWidth: '100%' }} />
          ) : (
            <pre>{preview?.body}</pre>
          )}
        </DialogContent>
      </Dialog>
    </>
  )
}
