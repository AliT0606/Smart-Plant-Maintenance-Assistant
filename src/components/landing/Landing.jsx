import { Link } from 'react-router-dom'

export default function Landing() {
  return (
    <div className="min-h-screen bg-background relative overflow-hidden flex flex-col font-body">
      {/* Background Decorative Elements */}
      <div className="absolute top-[-10%] right-[-5%] w-[40rem] h-[40rem] bg-secondary-container/40 rounded-full blur-3xl -z-10"></div>
      <div className="absolute top-1/2 left-[-10%] w-96 h-96 bg-primary-fixed/20 rounded-full blur-3xl -z-10"></div>

      {/* Header */}
      <header className="flex justify-between items-center p-8 lg:px-16 z-10">
        <div className="text-2xl font-extrabold text-primary tracking-tighter flex items-center gap-2">
          <span className="material-symbols-outlined" style={{ fontVariationSettings: "'FILL' 1" }}>eco</span>
          Akıllı Bahçe
        </div>
        <div className="flex gap-4">

          <Link to="/register" className="bg-primary text-on-primary px-6 py-3 rounded-full font-bold hover:opacity-90 transition-all shadow-md">
            Ücretsiz Başla
          </Link>
        </div>
      </header>

      {/* Hero Section */}
      <main className="flex-1 flex flex-col items-center justify-center text-center px-6 mt-12 lg:mt-24 z-10">
        <span className="bg-secondary-fixed text-on-secondary-fixed text-xs font-bold uppercase tracking-widest px-4 py-2 rounded-full mb-6 inline-block">
          %100 Doğal Zeka
        </span>
        <h1 className="text-5xl lg:text-7xl font-extrabold text-on-surface tracking-tighter mb-6 max-w-4xl leading-tight">
          Dijital Botanik <span className="text-transparent bg-clip-text bg-gradient-to-r from-primary to-primary-fixed-dim">Bahçenize</span> Hoş Geldiniz.
        </h1>
        <p className="text-lg text-on-surface-variant max-w-2xl mb-10 font-medium">
          Bitkilerinizin su, ışık ve gübre ihtiyaçlarını takip edin, bakım takvimleri oluşturun ve modern seranızı cebinizde taşıyın.
        </p>
        
        <div className="flex flex-col sm:flex-row gap-4">
          <Link to="/register" className="bg-gradient-to-r from-primary to-primary-container text-on-primary px-8 py-4 rounded-2xl font-bold text-lg hover:shadow-xl transition-all scale-98 active:opacity-80 flex items-center justify-center gap-2">
            Hemen Başla
            <span className="material-symbols-outlined">arrow_forward</span>
          </Link>
          <Link to="/login" className="bg-surface-container-high text-on-surface px-8 py-4 rounded-2xl font-bold text-lg hover:bg-surface-container-highest transition-all flex items-center justify-center">
            Mevcut Hesaba Giriş
          </Link>
        </div>
      </main>

      {/* Features Grid */}
      <section className="px-8 lg:px-16 py-24 z-10">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-7xl mx-auto">
          {/* Feature 1 */}
          <div className="bg-surface-container-lowest/80 backdrop-blur-xl p-8 rounded-3xl border border-outline-variant/10 hover:-translate-y-2 transition-transform duration-300">
            <div className="w-14 h-14 bg-secondary-container text-on-secondary-container rounded-2xl flex items-center justify-center mb-6">
              <span className="material-symbols-outlined text-3xl">water_drop</span>
            </div>
            <h3 className="text-xl font-bold text-on-surface mb-3">Akıllı Sulama</h3>
            <p className="text-on-surface-variant">Her bitkinin kendine özgü sulama takvimini oluşturun ve bir daha hiçbir bitkinizi susuz bırakmayın.</p>
          </div>

          {/* Feature 2 */}
          <div className="bg-surface-container-lowest/80 backdrop-blur-xl p-8 rounded-3xl border border-outline-variant/10 hover:-translate-y-2 transition-transform duration-300">
            <div className="w-14 h-14 bg-primary-container text-on-primary-container rounded-2xl flex items-center justify-center mb-6">
              <span className="material-symbols-outlined text-3xl">library_books</span>
            </div>
            <h3 className="text-xl font-bold text-on-surface mb-3">Bitki Kütüphanesi</h3>
            <p className="text-on-surface-variant">Yüzlerce bitki türü hakkında bilgi edinin. Işık, ısı ve gübre gereksinimlerini tek tıkla öğrenin.</p>
          </div>

          {/* Feature 3 */}
          <div className="bg-surface-container-lowest/80 backdrop-blur-xl p-8 rounded-3xl border border-outline-variant/10 hover:-translate-y-2 transition-transform duration-300">
            <div className="w-14 h-14 bg-tertiary-container text-on-tertiary-container rounded-2xl flex items-center justify-center mb-6">
              <span className="material-symbols-outlined text-3xl">health_and_safety</span>
            </div>
            <h3 className="text-xl font-bold text-on-surface mb-3">Sağlık Takibi</h3>
            <p className="text-on-surface-variant">Bitkilerinizin büyüme süreçlerini not alın, fotoğraflarını çekin ve sağlık skorlarını anlık izleyin.</p>
          </div>
        </div>
      </section>
      
      {/* Footer minimal */}
      <footer className="text-center py-8 text-sm font-bold text-on-surface-variant opacity-60 z-10">
        © 2024 AKILLI BAHÇE • THE MODERN CONSERVATORY
      </footer>
    </div>
  )
}
