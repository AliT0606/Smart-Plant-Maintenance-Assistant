import { Link } from 'react-router-dom'

export default function Login() {
  return (
    <div className="bg-surface-container-lowest/80 backdrop-blur-xl rounded-[2rem] p-8 shadow-sm border border-outline-variant/10">
      <h2 className="text-2xl font-bold text-on-surface mb-6">Giriş Yap</h2>
      
      <form className="space-y-5" onSubmit={(e) => e.preventDefault()}>
        <div className="space-y-1">
          <label className="text-xs uppercase tracking-widest font-bold text-on-surface-variant ml-4">
            E-posta Adresi
          </label>
          <input
            type="email"
            placeholder="ornek@mail.com"
            className="w-full bg-surface-container-high border-none rounded-xl px-4 py-3 focus:ring-2 focus:ring-primary focus:bg-surface-bright transition-all"
          />
        </div>
        
        <div className="space-y-1">
          <label className="text-xs uppercase tracking-widest font-bold text-on-surface-variant ml-4">
            Şifre
          </label>
          <input
            type="password"
            placeholder="••••••••"
            className="w-full bg-surface-container-high border-none rounded-xl px-4 py-3 focus:ring-2 focus:ring-primary focus:bg-surface-bright transition-all"
          />
        </div>

        <div className="flex justify-end">
          <a href="#" className="text-xs font-bold text-primary hover:text-primary-container transition-colors">
            Şifremi Unuttum
          </a>
        </div>

        <Link
          to="/dashboard"
          className="w-full bg-gradient-to-r from-primary to-primary-container text-on-primary rounded-2xl py-4 font-bold flex items-center justify-center gap-2 hover:shadow-lg transition-all scale-98 active:opacity-80 mt-2"
        >
          <span className="material-symbols-outlined">login</span>
          Giriş Yap
        </Link>
      </form>

      <div className="mt-8 text-center">
        <p className="text-sm text-on-surface-variant">
          Hesabınız yok mu?{' '}
          <Link to="/register" className="font-bold text-primary hover:text-primary-container transition-colors">
            Hesap Oluştur
          </Link>
        </p>
      </div>
    </div>
  )
}
