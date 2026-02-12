import { AppBar, Box, CssBaseline, Drawer, List, ListItemButton, ListItemText, Toolbar, Typography } from '@mui/material'
import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom'
import Dashboard from './pages/Dashboard'
import EventDetailPage from './pages/EventDetail'
import FilesPage from './pages/Files'
import HoneypotPage from './pages/Honeypot'
import SessionPage from './pages/Session'

const drawerWidth = 220

export default function App() {
  return (
    <BrowserRouter>
      <CssBaseline />
      <AppBar position="fixed" sx={{ zIndex: (t) => t.zIndex.drawer + 1 }}>
        <Toolbar><Typography variant="h6">HOHO Hub</Typography></Toolbar>
      </AppBar>
      <Drawer
        variant="permanent"
        sx={{ width: drawerWidth, [`& .MuiDrawer-paper`]: { width: drawerWidth, boxSizing: 'border-box' } }}
      >
        <Toolbar />
        <List>
          <ListItemButton component="a" href="/ui/"><ListItemText primary="Dashboard" /></ListItemButton>
          <ListItemButton component="a" href="/ui/files"><ListItemText primary="Files" /></ListItemButton>
        </List>
      </Drawer>
      <Box component="main" sx={{ ml: `${drawerWidth}px`, p: 2 }}>
        <Toolbar />
        <Routes>
          <Route path="/ui" element={<Dashboard />} />
          <Route path="/ui/honeypots/:honeypotId" element={<HoneypotPage />} />
          <Route path="/ui/honeypots/:honeypotId/sessions/:sessionId" element={<SessionPage />} />
          <Route path="/ui/events/:eventId" element={<EventDetailPage />} />
          <Route path="/ui/files" element={<FilesPage />} />
          <Route path="*" element={<Navigate to="/ui" replace />} />
        </Routes>
      </Box>
    </BrowserRouter>
  )
}
