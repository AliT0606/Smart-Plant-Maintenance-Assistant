import React, { useState, useRef } from 'react'

const DIAGNOSES = [
  {
    disease: 'Kök Çürüklüğü',
    confidence: 87,
    severity: 'Orta',
    severityColor: 'text-amber-500',
    icon: 'water_drop',
    iconBg: 'bg-blue-100',
    iconColor: 'text-blue-500',
    symptoms: ['Yaprak uçlarında sararma', 'Toprak sürekli ıslak', 'Kötü koku'],
    treatment: 'Sulamayı hemen kesin ve bitkiyi saksısından çıkarın. Çürümüş kökleri steril bir makasla kesin. Taze, iyi drene eden bir toprak karışımıyla yeniden saksılayın ve birkaç hafta sulamamayı bırakın.',
    prevention: 'Saksının dibinde delik olduğundan emin olun. Toprağın üst kısmı kurumadan sulama yapmayın.',
  },
  {
    disease: 'Güneş Yanığı',
    confidence: 91,
    severity: 'Hafif',
    severityColor: 'text-green-500',
    icon: 'wb_sunny',
    iconBg: 'bg-amber-100',
    iconColor: 'text-amber-500',
    symptoms: ['Yapraklarda kahverengi lekeler', 'Yaprak kenarları kıvrılıyor', 'Solma'],
    treatment: 'Bitkiyi doğrudan güneş ışığından uzaklaştırın. Hasarlı yaprakları kesin ve birkaç gün gölgede bırakın. Daha sonra sabah güneşinin olduğu, öğleden sonra gölgeli bir yere yerleştirin.',
    prevention: 'Yeni bitkileri yavaşça güneş ışığına alıştırın. Öğleden sonraki sert güneşten kaçının.',
  },
  {
    disease: 'Un Biti (Mealybug)',
    confidence: 79,
    severity: 'Yüksek',
    severityColor: 'text-red-500',
    icon: 'bug_report',
    iconBg: 'bg-red-100',
    iconColor: 'text-red-500',
    symptoms: ['Beyaz pamuksu kümeler', 'Yapışkan salgı (Bal özü)', 'Yapraklarda sararma'],
    treatment: 'Görünür zararlıları pamukla alkolle temizleyin. Tüm bitkiyi sabun+su karışımıyla veya neem yağıyla yıkayın. Etkilenen bitkiyi diğerlerinden ayırın. 1 hafta arayla 3-4 kez tekrarlayın.',
    prevention: 'Yeni bitkileri koleksiyona eklemeden önce 2 hafta karantinada tutun. Düzenli yaprak kontrolü yapın.',
  },
]

export default function AiDiagnosis() {
  const [image, setImage] = useState(null)
  const [imagePreview, setImagePreview] = useState(null)
  const [phase, setPhase] = useState('idle') // idle | scanning | result
  const [diagnosis, setDiagnosis] = useState(null)
  const [scanProgress, setScanProgress] = useState(0)
  const fileRef = useRef(null)

  const handleImageChange = (e) => {
    const file = e.target.files[0]
    if (file) {
      setImage(file)
      setImagePreview(URL.createObjectURL(file))
      setPhase('idle')
      setDiagnosis(null)
    }
  }

  const handleScan = () => {
    if (!imagePreview) return
    setPhase('scanning')
    setScanProgress(0)

    // Animate progress bar
    let progress = 0
    const interval = setInterval(() => {
      progress += Math.random() * 18
      if (progress >= 100) {
        progress = 100
        clearInterval(interval)
        setTimeout(() => {
          const randomDx = DIAGNOSES[Math.floor(Math.random() * DIAGNOSES.length)]
          setDiagnosis(randomDx)
          setPhase('result')
        }, 400)
      }
      setScanProgress(Math.min(progress, 100))
    }, 250)
  }

  const handleReset = () => {
    setImage(null)
    setImagePreview(null)
    setPhase('idle')
    setDiagnosis(null)
    setScanProgress(0)
  }

  return (
    <main className="pl-72 pt-20 pb-16 min-h-screen font-body">
      <div className="p-8 max-w-4xl mx-auto flex flex-col gap-8">
        {/* Header */}
        <div className="flex items-center gap-4">
          <div className="w-14 h-14 rounded-2xl bg-primary-container flex items-center justify-center shrink-0">
            <span className="material-symbols-outlined text-3xl text-primary" style={{ fontVariationSettings: "'FILL' 1" }}>neurology</span>
          </div>
          <div>
            <h2 className="text-3xl font-extrabold text-primary tracking-tight">Yapay Zeka Teşhisi</h2>
            <p className="text-on-surface-variant">Hasta bitkinin fotoğrafını yükleyin, anında teşhis alalım.</p>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Upload Panel */}
          <div className="bg-surface-container-lowest/80 backdrop-blur-xl p-8 rounded-[2rem] border border-outline-variant/10 shadow-sm flex flex-col gap-6">
            <h3 className="text-xl font-bold text-on-surface">Fotoğraf Yükle</h3>

            {/* Upload Area */}
            <label className="cursor-pointer flex-1">
              <div className={`rounded-2xl border-2 overflow-hidden relative min-h-[260px] flex flex-col items-center justify-center transition-all
                ${imagePreview
                  ? 'border-primary/20'
                  : 'border-dashed border-outline-variant/50 hover:border-primary hover:bg-primary-container/10'
                }`}
              >
                {imagePreview ? (
                  <>
                    <img src={imagePreview} alt="plant" className="w-full h-full object-cover absolute inset-0" />
                    {/* Scan animation overlay */}
                    {phase === 'scanning' && (
                      <div className="absolute inset-0 bg-black/40 flex flex-col items-center justify-center gap-4 z-10">
                        {/* Laser beam */}
                        <div className="absolute left-0 right-0 h-1 bg-gradient-to-r from-transparent via-green-400 to-transparent animate-[scanBeam_1.5s_ease-in-out_infinite] shadow-[0_0_20px_4px_rgba(74,222,128,0.8)]" style={{top: `${scanProgress}%`}}></div>
                        {/* Grid overlay */}
                        <div className="absolute inset-0" style={{
                          backgroundImage: 'linear-gradient(rgba(74,222,128,0.08) 1px, transparent 1px), linear-gradient(90deg, rgba(74,222,128,0.08) 1px, transparent 1px)',
                          backgroundSize: '30px 30px'
                        }}></div>
                        <div className="relative z-20 flex flex-col items-center gap-3">
                          <div className="w-12 h-12 rounded-full border-4 border-green-400 border-t-transparent animate-spin"></div>
                          <span className="text-green-400 font-extrabold text-lg">Taranıyor...</span>
                          <span className="text-green-300 text-sm font-bold">%{Math.round(scanProgress)}</span>
                        </div>
                      </div>
                    )}
                  </>
                ) : (
                  <div className="flex flex-col items-center gap-3 p-8">
                    <span className="material-symbols-outlined text-6xl text-on-surface-variant opacity-30">photo_camera</span>
                    <p className="text-sm font-bold text-on-surface-variant opacity-60 text-center">
                      Hasta bitkinin fotoğrafını<br />buraya sürükleyin ya da tıklayın
                    </p>
                    <span className="text-xs text-on-surface-variant opacity-40">JPG, PNG, WEBP desteklenir</span>
                  </div>
                )}
              </div>
              <input type="file" accept="image/*" ref={fileRef} className="hidden" onChange={handleImageChange} />
            </label>

            {/* Action Buttons */}
            <div className="flex gap-3">
              {imagePreview && phase !== 'scanning' && (
                <button onClick={handleReset} className="flex-1 border-2 border-outline-variant/30 text-on-surface-variant py-3 rounded-2xl font-bold text-sm hover:bg-surface-container transition-all flex items-center justify-center gap-2">
                  <span className="material-symbols-outlined text-[18px]">refresh</span>
                  Temizle
                </button>
              )}
              <button
                onClick={handleScan}
                disabled={!imagePreview || phase === 'scanning'}
                className={`flex-1 py-3 rounded-2xl font-extrabold text-sm transition-all flex items-center justify-center gap-2
                  ${!imagePreview || phase === 'scanning'
                    ? 'bg-surface-container text-on-surface-variant cursor-not-allowed'
                    : 'bg-primary text-on-primary hover:opacity-90 hover:shadow-lg'
                  }`}
              >
                <span className="material-symbols-outlined text-[18px]" style={{ fontVariationSettings: "'FILL' 1" }}>
                  {phase === 'scanning' ? 'hourglass_top' : 'biotech'}
                </span>
                {phase === 'scanning' ? 'Analiz Ediliyor...' : 'Teşhis Başlat'}
              </button>
            </div>
          </div>

          {/* Result Panel */}
          <div className="bg-surface-container-lowest/80 backdrop-blur-xl p-8 rounded-[2rem] border border-outline-variant/10 shadow-sm flex flex-col">
            <h3 className="text-xl font-bold text-on-surface mb-6">Teşhis Raporu</h3>

            {phase === 'idle' && (
              <div className="flex-1 flex flex-col items-center justify-center gap-4 text-center py-8">
                <span className="material-symbols-outlined text-6xl text-on-surface-variant opacity-20">article</span>
                <p className="text-on-surface-variant text-sm font-medium opacity-60">
                  Fotoğraf yükledikten sonra<br />"Teşhis Başlat" butonuna basın.
                </p>
              </div>
            )}

            {phase === 'scanning' && (
              <div className="flex-1 flex flex-col items-center justify-center gap-6 text-center py-8">
                <div className="w-20 h-20 rounded-full border-4 border-primary border-t-transparent animate-spin"></div>
                <div className="w-full bg-surface-container-high rounded-full h-2 overflow-hidden">
                  <div
                    className="h-full bg-gradient-to-r from-primary to-secondary transition-all duration-300 rounded-full"
                    style={{ width: `${scanProgress}%` }}
                  ></div>
                </div>
                <p className="text-on-surface-variant text-sm font-bold">Yaprak dokusu analiz ediliyor...</p>
              </div>
            )}

            {phase === 'result' && diagnosis && (
              <div className="flex flex-col gap-5 animate-in fade-in slide-in-from-bottom-4 duration-500">
                {/* Disease + Confidence */}
                <div className="flex items-center gap-4">
                  <div className={`w-14 h-14 rounded-2xl ${diagnosis.iconBg} flex items-center justify-center shrink-0`}>
                    <span className={`material-symbols-outlined text-2xl ${diagnosis.iconColor}`} style={{ fontVariationSettings: "'FILL' 1" }}>{diagnosis.icon}</span>
                  </div>
                  <div className="flex-1">
                    <h4 className="text-lg font-extrabold text-on-surface">{diagnosis.disease}</h4>
                    <div className="flex items-center gap-2 mt-1">
                      <span className={`text-sm font-bold ${diagnosis.severityColor}`}>{diagnosis.severity} Risk</span>
                      <span className="text-on-surface-variant opacity-30">•</span>
                      <span className="text-sm text-on-surface-variant font-bold">%{diagnosis.confidence} Kesinlik</span>
                    </div>
                  </div>
                </div>

                {/* Symptoms */}
                <div>
                  <p className="text-xs font-extrabold uppercase tracking-widest text-on-surface-variant mb-2">Belirtiler</p>
                  <div className="flex flex-wrap gap-2">
                    {diagnosis.symptoms.map(s => (
                      <span key={s} className="bg-error-container/40 text-on-error-container text-xs font-bold px-3 py-1 rounded-full">{s}</span>
                    ))}
                  </div>
                </div>

                {/* Treatment */}
                <div className="bg-primary-container/30 p-4 rounded-2xl">
                  <p className="text-xs font-extrabold uppercase tracking-widest text-primary mb-2">💊 Tedavi Önerisi</p>
                  <p className="text-sm text-on-surface-variant leading-relaxed">{diagnosis.treatment}</p>
                </div>

                {/* Prevention */}
                <div className="bg-secondary-container/30 p-4 rounded-2xl">
                  <p className="text-xs font-extrabold uppercase tracking-widest text-secondary mb-2">🛡️ Önleme</p>
                  <p className="text-sm text-on-surface-variant leading-relaxed">{diagnosis.prevention}</p>
                </div>

                <button onClick={handleReset} className="border-2 border-outline-variant/30 text-on-surface-variant py-3 rounded-2xl font-bold text-sm hover:bg-surface-container transition-all flex items-center justify-center gap-2">
                  <span className="material-symbols-outlined text-[18px]">restart_alt</span>
                  Yeni Tarama Yap
                </button>
              </div>
            )}
          </div>
        </div>
      </div>
    </main>
  )
}
