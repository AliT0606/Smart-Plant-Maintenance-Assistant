import { useState } from 'react'
import { NavLink } from 'react-router-dom'
import AddPlantModal from '../dashboard/AddPlantModal.jsx'

const navLinkClass = ({ isActive }) =>
  isActive
    ? "flex items-center gap-4 bg-surface-variant text-primary rounded-xl px-4 py-3 font-bold translate-x-1 transition-transform"
    : "flex items-center gap-4 text-on-surface-variant px-4 py-3 rounded-xl hover:bg-surface-variant transition-all"

export default function SideNavBar() {
  const [showModal, setShowModal] = useState(false)

  return (
    <>
      <aside className="fixed left-0 top-20 bottom-0 flex flex-col p-6 gap-2 w-72 bg-surface overflow-y-auto">
        <div className="mb-8 px-4">
          <h2 className="text-lg font-bold text-primary">Bahçem</h2>
          <p className="text-xs text-on-surface-variant font-medium opacity-70">12 Sağlıklı Bitki</p>
        </div>

        <nav className="flex flex-col gap-1">
          <NavLink to="/dashboard" end className={navLinkClass}>
            <span className="material-symbols-outlined" style={{ fontVariationSettings: "'FILL' 1" }}>dashboard</span>
            <span>Panel</span>
          </NavLink>
          
          <NavLink to="/dashboard/library" className={navLinkClass}>
            <span className="material-symbols-outlined" style={{ fontVariationSettings: "'FILL' 1" }}>library_books</span>
            <span>Bitki Kütüphanesi</span>
          </NavLink>

          <NavLink to="/dashboard/calendar" className={navLinkClass}>
            <span className="material-symbols-outlined" style={{ fontVariationSettings: "'FILL' 1" }}>calendar_today</span>
            <span>Bakım Takvimi</span>
          </NavLink>
          
          <NavLink to="/dashboard/statistics" className={navLinkClass}>
            <span className="material-symbols-outlined" style={{ fontVariationSettings: "'FILL' 1" }}>bar_chart</span>
            <span>İstatistikler</span>
          </NavLink>

          <NavLink to="/dashboard/ai-diagnosis" className={navLinkClass}>
            <span className="material-symbols-outlined" style={{ fontVariationSettings: "'FILL' 1" }}>neurology</span>
            <span>Yapay Zeka Teşhisi</span>
          </NavLink>
        </nav>

        <button
          onClick={() => setShowModal(true)}
          className="mt-auto bg-primary text-on-primary rounded-xl py-4 font-bold flex items-center justify-center gap-2 hover:opacity-90 transition-opacity"
        >
          <span className="material-symbols-outlined">add</span>
          Yeni Bitki Ekle
        </button>
      </aside>

      {showModal && <AddPlantModal onClose={() => setShowModal(false)} />}
    </>
  )
}
