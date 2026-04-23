import { Outlet } from 'react-router-dom'

export default function AuthLayout() {
  return (
    <div className="min-h-screen bg-surface flex items-center justify-center relative overflow-hidden">
      {/* Botanical Background Elements */}
      <div className="absolute -top-32 -left-32 w-96 h-96 bg-primary-fixed/30 rounded-full blur-3xl"></div>
      <div className="absolute bottom-[-10%] right-[-5%] w-[40rem] h-[40rem] bg-secondary-container/40 rounded-full blur-3xl"></div>
      <div className="absolute top-1/4 right-1/4 w-64 h-64 bg-tertiary-fixed/20 rounded-full blur-3xl"></div>
      
      {/* Content Container */}
      <div className="relative z-10 w-full max-w-md px-6">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-extrabold text-primary tracking-tighter mb-2">
            Akıllı Bahçe
          </h1>
          <p className="text-on-surface-variant font-medium">
            Akıllı Bitki Bakım Asistanınız
          </p>
        </div>
        
        <Outlet />
      </div>
    </div>
  )
}
