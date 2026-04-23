import React from 'react'

export default function Settings() {
  return (
    <main className="pl-72 pt-20 pb-16 min-h-screen">
      <div className="p-8 max-w-4xl mx-auto flex flex-col gap-8">
        <h2 className="text-3xl font-extrabold text-primary tracking-tight mb-2">Ayarlar</h2>

        {/* Profil Ayarları */}
        <section className="bg-surface-container-lowest rounded-[2rem] p-8 shadow-sm border border-outline-variant/10">
          <h3 className="text-xl font-bold text-primary mb-6 flex items-center gap-2">
            <span className="material-symbols-outlined text-primary">person</span>
            Hesabım
          </h3>
          <div className="flex flex-col md:flex-row gap-8">
            <div className="flex flex-col items-center gap-4">
              <div className="w-32 h-32 rounded-full overflow-hidden border-4 border-surface-container-high relative group cursor-pointer">
                <img
                  className="w-full h-full object-cover"
                  alt="Profile"
                  src="https://lh3.googleusercontent.com/aida-public/AB6AXuCphgaEV6IGWsXU69PEwvKDVYrrc56BDh1KxW7DL-S_cJ9C7zUxxLLUdAtd57z4QiNWnY-Tk9CI-UxV1CcgMkqhsuF803I7Ck3VmQ0CLVmMqP_LR4y67wd7q-xFV0d0SXDv9azwIHRhWZk8jibhoq5F_ImyCTpw9WHnpKjBYTDPsSXK0mUjfmyf3fKFel67oNj6YOopU95kiW0AUlZkVS-RrY0-uSenl5Y_2lHpE6rYDfgGXf3phunCZqm77oeiQa-OIffFYy-Et0A"
                />
                <div className="absolute inset-0 bg-black/30 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
                  <span className="material-symbols-outlined text-white">photo_camera</span>
                </div>
              </div>
              <button className="text-xs font-bold text-primary hover:text-primary-container transition-colors">
                Fotoğrafı Değiştir
              </button>
            </div>
            
            <div className="flex-1 space-y-5">
              <div className="space-y-1">
                <label className="text-xs uppercase tracking-widest font-bold text-on-surface-variant ml-4">Ad Soyad</label>
                <input
                  type="text"
                  defaultValue="Akıllı Bahçe Kullanıcısı"
                  className="w-full bg-surface-container border-none rounded-xl px-4 py-3 focus:ring-2 focus:ring-primary focus:bg-surface-bright transition-all"
                />
              </div>
              <div className="space-y-1">
                <label className="text-xs uppercase tracking-widest font-bold text-on-surface-variant ml-4">E-posta</label>
                <input
                  type="email"
                  defaultValue="ornek@mail.com"
                  className="w-full bg-surface-container border-none rounded-xl px-4 py-3 focus:ring-2 focus:ring-primary focus:bg-surface-bright transition-all"
                />
              </div>
            </div>
          </div>
        </section>

        {/* Bildirim Ayarları */}
        <section className="bg-surface-container-lowest rounded-[2rem] p-8 shadow-sm border border-outline-variant/10">
          <h3 className="text-xl font-bold text-primary mb-6 flex items-center gap-2">
            <span className="material-symbols-outlined text-primary">notifications_active</span>
            Bildirim Tercihleri
          </h3>
          <div className="space-y-4">
            <div className="flex items-center justify-between p-4 bg-surface-container-low rounded-2xl">
              <div>
                <p className="font-bold text-on-surface">Sulama Hatırlatıcıları</p>
                <p className="text-xs text-on-surface-variant">Bitkilerinizin sulama vakti geldiğinde bildirim alın.</p>
              </div>
              <label className="relative inline-flex items-center cursor-pointer">
                <input type="checkbox" className="sr-only peer" defaultChecked />
                <div className="w-11 h-6 bg-surface-container-highest peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary"></div>
              </label>
            </div>
            
            <div className="flex items-center justify-between p-4 bg-surface-container-low rounded-2xl">
              <div>
                <p className="font-bold text-on-surface">Haftalık İpuçları</p>
                <p className="text-xs text-on-surface-variant">Bahçe bakımıyla ilgili yeni ipuçlarını kaçırmayın.</p>
              </div>
              <label className="relative inline-flex items-center cursor-pointer">
                <input type="checkbox" className="sr-only peer" defaultChecked />
                <div className="w-11 h-6 bg-surface-container-highest peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary"></div>
              </label>
            </div>
          </div>
        </section>

        {/* Görünüm Ayarları */}
        <section className="bg-surface-container-lowest rounded-[2rem] p-8 shadow-sm border border-outline-variant/10">
          <h3 className="text-xl font-bold text-primary mb-6 flex items-center gap-2">
            <span className="material-symbols-outlined text-primary">palette</span>
            Görünüm
          </h3>
          <div className="flex gap-4">
            <button className="flex-1 flex flex-col items-center gap-3 p-6 rounded-2xl border-2 border-primary bg-primary/5 transition-all">
              <span className="material-symbols-outlined text-3xl text-primary">light_mode</span>
              <span className="font-bold text-primary">Açık Tema</span>
            </button>
            <button className="flex-1 flex flex-col items-center gap-3 p-6 rounded-2xl border-2 border-transparent bg-surface-container-high hover:bg-surface-container-highest transition-all opacity-60 cursor-not-allowed">
              <span className="material-symbols-outlined text-3xl text-on-surface-variant">dark_mode</span>
              <span className="font-bold text-on-surface-variant">Koyu Tema (Yakında)</span>
            </button>
          </div>
        </section>

        <div className="flex justify-end mt-4">
          <button className="bg-primary text-on-primary rounded-2xl px-8 py-4 font-bold flex items-center gap-2 hover:shadow-lg transition-all scale-98 active:opacity-80">
            <span className="material-symbols-outlined">save</span>
            Değişiklikleri Kaydet
          </button>
        </div>

      </div>
    </main>
  )
}
