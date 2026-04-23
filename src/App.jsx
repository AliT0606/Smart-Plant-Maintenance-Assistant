import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import Landing from './components/landing/Landing.jsx'
import DashboardLayout from './components/layout/DashboardLayout.jsx'
import Dashboard from './components/dashboard/Dashboard.jsx'
import Settings from './components/settings/Settings.jsx'
import Library from './components/library/Library.jsx'
import Calendar from './components/calendar/Calendar.jsx'
import Statistics from './components/statistics/Statistics.jsx'
import HelpCenter from './components/info/HelpCenter.jsx'
import PrivacyPolicy from './components/info/PrivacyPolicy.jsx'
import AiDiagnosis from './components/ai/AiDiagnosis.jsx'
import AuthLayout from './components/auth/AuthLayout.jsx'
import Login from './components/auth/Login.jsx'
import Register from './components/auth/Register.jsx'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Public Landing Page */}
        <Route path="/" element={<Landing />} />

        {/* Authentication Routes */}
        <Route element={<AuthLayout />}>
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
        </Route>

        {/* Protected/Dashboard Routes */}
        <Route path="/dashboard" element={<DashboardLayout />}>
          <Route index element={<Dashboard />} />
          <Route path="settings" element={<Settings />} />
          <Route path="library" element={<Library />} />
          <Route path="calendar" element={<Calendar />} />
          <Route path="statistics" element={<Statistics />} />
          <Route path="help" element={<HelpCenter />} />
          <Route path="privacy" element={<PrivacyPolicy />} />
          <Route path="ai-diagnosis" element={<AiDiagnosis />} />
        </Route>

        {/* Catch-all redirect */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
