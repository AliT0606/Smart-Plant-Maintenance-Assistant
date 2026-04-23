import { Outlet } from 'react-router-dom'
import TopNavBar from './TopNavBar.jsx'
import SideNavBar from './SideNavBar.jsx'
import Footer from './Footer.jsx'

export default function DashboardLayout() {
  return (
    <div className="bg-background text-on-surface min-h-screen">
      <TopNavBar />
      <SideNavBar />
      <Outlet />
      <Footer />
    </div>
  )
}
