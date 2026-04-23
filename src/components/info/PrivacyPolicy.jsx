import React from 'react'

export default function PrivacyPolicy() {
  return (
    <main className="pl-72 pt-20 pb-16 min-h-screen font-body">
      <div className="p-8 max-w-4xl mx-auto flex flex-col gap-8">
        <div>
          <h2 className="text-3xl font-extrabold text-primary tracking-tight mb-2">Gizlilik Politikası</h2>
          <p className="text-on-surface-variant">Verilerinizi nasıl koruduğumuz ve kullandığımız hakkında bilgiler.</p>
        </div>

        <div className="bg-surface-container-lowest/80 backdrop-blur-xl p-8 md:p-12 rounded-[2rem] border border-outline-variant/10 shadow-sm space-y-8 text-on-surface-variant leading-relaxed">
          
          <section>
            <h3 className="text-xl font-bold text-on-surface mb-4">1. Toplanan Veriler</h3>
            <p>
              Akıllı Bahçe uygulamasını kullandığınızda, size daha iyi bir hizmet sunabilmek için bazı verileri topluyoruz. Bunlar şunları içerir:
            </p>
            <ul className="list-disc pl-6 mt-2 space-y-1">
              <li>Adınız ve e-posta adresiniz (Kayıt sırasında)</li>
              <li>Eklediğiniz bitki türleri ve özellikleri</li>
              <li>Uygulama içi kullanım istatistikleri ve tıklama verileri</li>
              <li>İsteğe bağlı olarak yüklediğiniz bitki fotoğrafları</li>
            </ul>
          </section>

          <section>
            <h3 className="text-xl font-bold text-on-surface mb-4">2. Verilerin Kullanımı</h3>
            <p>
              Toplanan veriler yalnızca size özel bitki bakım takvimi oluşturmak, sulama hatırlatıcıları göndermek ve kullanıcı deneyiminizi geliştirmek amacıyla kullanılır. Verileriniz kesinlikle üçüncü parti şirketlerle reklam amacıyla paylaşılmaz veya satılmaz.
            </p>
          </section>

          <section>
            <h3 className="text-xl font-bold text-on-surface mb-4">3. Veri Güvenliği</h3>
            <p>
              Verileriniz modern şifreleme yöntemleri ile korunmaktadır. Sunucularımızda saklanan tüm hassas bilgiler (şifreler vb.) kriptolanmış formatta tutulur. Ancak unutulmamalıdır ki, internet üzerinden yapılan hiçbir veri iletimi %100 güvenli değildir.
            </p>
          </section>

          <section>
            <h3 className="text-xl font-bold text-on-surface mb-4">4. Çerezler (Cookies)</h3>
            <p>
              Uygulamamız, oturumunuzu açık tutmak ve tercihlerinizi hatırlamak için çerezleri kullanır. Tarayıcı ayarlarınızdan çerezleri devre dışı bırakabilirsiniz ancak bu durum uygulamanın bazı işlevlerini düzgün kullanmanızı engelleyebilir.
            </p>
          </section>

          <section>
            <h3 className="text-xl font-bold text-on-surface mb-4">5. İletişim</h3>
            <p>
              Gizlilik politikamız ile ilgili soru veya endişeleriniz varsa, lütfen <strong className="text-primary">destek@akillibahce.com</strong> adresi üzerinden bizimle iletişime geçin.
            </p>
          </section>

          <div className="mt-8 pt-6 border-t border-outline-variant/20 text-sm opacity-60">
            Son güncelleme tarihi: 21 Nisan 2026
          </div>
        </div>
      </div>
    </main>
  )
}
