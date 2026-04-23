import React from 'react'

export default function HelpCenter() {
  return (
    <main className="pl-72 pt-20 pb-16 min-h-screen font-body">
      <div className="p-8 max-w-4xl mx-auto flex flex-col gap-8">
        <div>
          <h2 className="text-3xl font-extrabold text-primary tracking-tight mb-2">Yardım Merkezi</h2>
          <p className="text-on-surface-variant">Sıkça sorulan sorular ve sorun giderme rehberi.</p>
        </div>

        <div className="space-y-6">
          <div className="bg-surface-container-lowest/80 backdrop-blur-xl p-8 rounded-[2rem] border border-outline-variant/10 shadow-sm">
            <h3 className="text-xl font-bold text-on-surface mb-6">Sıkça Sorulan Sorular</h3>
            
            <div className="space-y-6">
              <div>
                <h4 className="text-lg font-bold text-primary mb-2">Nasıl yeni bitki ekleyebilirim?</h4>
                <p className="text-on-surface-variant leading-relaxed">
                  Sol menünün en altındaki "Yeni Bitki Ekle" butonuna tıklayarak bitkinizin fotoğrafını, türünü ve bakım ihtiyaçlarını girebilirsiniz. Sistem sizin için otomatik bir takvim oluşturacaktır.
                </p>
              </div>
              <hr className="border-outline-variant/20" />
              <div>
                <h4 className="text-lg font-bold text-primary mb-2">Sulama bildirimlerini nasıl kapatırım?</h4>
                <p className="text-on-surface-variant leading-relaxed">
                  Sağ üst köşedeki ayarlar (çark) simgesine veya sol menüden Ayarlar sayfasına giderek "Bildirim Tercihleri" altından sulama hatırlatıcılarını kapatabilirsiniz.
                </p>
              </div>
              <hr className="border-outline-variant/20" />
              <div>
                <h4 className="text-lg font-bold text-primary mb-2">Bitkimin türünü bilmiyorum, ne yapmalıyım?</h4>
                <p className="text-on-surface-variant leading-relaxed">
                  Yakında eklenecek olan yapay zeka destekli fotoğraf tanıma özelliğimizi kullanarak bitkinizin türünü tespit edebilirsiniz. Şimdilik "Bitki Kütüphanesi" sekmesinden görsellere bakarak tahmin yürütebilirsiniz.
                </p>
              </div>
            </div>
          </div>

          <div className="bg-primary-container/30 backdrop-blur-xl p-8 rounded-[2rem] border border-primary/10 shadow-sm flex flex-col items-center text-center">
            <span className="material-symbols-outlined text-4xl text-primary mb-4">support_agent</span>
            <h3 className="text-xl font-bold text-on-surface mb-2">Daha fazla yardıma mı ihtiyacınız var?</h3>
            <p className="text-on-surface-variant mb-6">Destek ekibimiz hafta içi 09:00 - 18:00 saatleri arasında hizmetinizdedir.</p>
            <button className="bg-primary text-on-primary px-8 py-3 rounded-full font-bold shadow-md hover:shadow-lg transition-all hover:opacity-90">
              Bize Ulaşın
            </button>
          </div>
        </div>
      </div>
    </main>
  )
}
