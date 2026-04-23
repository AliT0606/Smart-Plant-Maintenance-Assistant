import { Link } from 'react-router-dom'

export default function Footer() {
  return (
    <footer className="fixed bottom-0 right-0 left-72 px-8 py-4 flex justify-between items-center bg-background border-t border-outline-variant/30 z-40 backdrop-blur-md transition-colors duration-300">
      <div className="flex gap-8">
        <div className="flex items-center gap-2">
          <span className="w-2 h-2 rounded-full bg-primary"></span>
          <span className="font-plus-jakarta text-xs uppercase tracking-widest font-bold text-primary">
            Toplam Bitki: 12
          </span>
        </div>
        <div className="flex items-center gap-2">
          <span className="w-2 h-2 rounded-full bg-error"></span>
          <span className="font-plus-jakarta text-xs uppercase tracking-widest font-bold text-primary">
            Bugün Yapılması Gereken: 3
          </span>
        </div>
      </div>
      <div className="flex gap-4">
        <Link
          to="/dashboard/help"
          className="font-plus-jakarta text-xs uppercase tracking-widest font-bold text-on-surface-variant hover:text-primary transition-all"
        >
          Yardım Merkezi
        </Link>
        <span className="text-on-surface-variant opacity-30">•</span>
        <Link
          to="/dashboard/privacy"
          className="font-plus-jakarta text-xs uppercase tracking-widest font-bold text-on-surface-variant hover:text-primary transition-all"
        >
          Gizlilik Politikası
        </Link>
      </div>
      <div className="text-on-surface-variant text-[10px] font-bold opacity-60">
        © 2024 AKILLI BAHÇE • SİSTEM DURUMU: ÇEVRİMİÇİ
      </div>
    </footer>
  )
}
