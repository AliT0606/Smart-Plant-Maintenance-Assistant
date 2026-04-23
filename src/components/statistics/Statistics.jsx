import React from 'react'

export default function Statistics() {
  return (
    <main className="pl-72 pt-20 pb-16 min-h-screen font-body">
      <div className="p-8 max-w-6xl mx-auto flex flex-col gap-8">
        
        {/* Header */}
        <div>
          <h2 className="text-3xl font-extrabold text-primary tracking-tight mb-2">İstatistikler</h2>
          <p className="text-on-surface-variant">Bahçenizin genel sağlık durumu ve bakım alışkanlıklarınız.</p>
        </div>

        {/* Overview Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-surface-container-lowest/80 backdrop-blur-xl p-6 rounded-[2rem] border border-outline-variant/10 shadow-sm flex items-center gap-6 hover:shadow-md transition-shadow">
            <div className="w-16 h-16 rounded-full bg-primary-container text-on-primary-container flex items-center justify-center shrink-0">
              <span className="material-symbols-outlined text-3xl">potted_plant</span>
            </div>
            <div>
              <p className="text-xs uppercase tracking-widest font-bold text-on-surface-variant opacity-70">Toplam Bitki</p>
              <p className="text-4xl font-extrabold text-on-surface mt-1">12</p>
            </div>
          </div>

          <div className="bg-surface-container-lowest/80 backdrop-blur-xl p-6 rounded-[2rem] border border-outline-variant/10 shadow-sm flex items-center gap-6 hover:shadow-md transition-shadow">
            <div className="w-16 h-16 rounded-full bg-tertiary-container text-on-tertiary-container flex items-center justify-center shrink-0">
              <span className="material-symbols-outlined text-3xl">check_circle</span>
            </div>
            <div>
              <p className="text-xs uppercase tracking-widest font-bold text-on-surface-variant opacity-70">Tamamlanan Görev</p>
              <p className="text-4xl font-extrabold text-on-surface mt-1">24</p>
            </div>
          </div>

          <div className="bg-surface-container-lowest/80 backdrop-blur-xl p-6 rounded-[2rem] border border-outline-variant/10 shadow-sm flex items-center gap-6 hover:shadow-md transition-shadow">
            <div className="w-16 h-16 rounded-full bg-secondary-container text-on-secondary-container flex items-center justify-center shrink-0">
              <span className="material-symbols-outlined text-3xl">psychology_alt</span>
            </div>
            <div>
              <p className="text-xs uppercase tracking-widest font-bold text-on-surface-variant opacity-70">Kurtarılan Bitki</p>
              <p className="text-4xl font-extrabold text-on-surface mt-1">2</p>
            </div>
          </div>
        </div>

        {/* Charts Row */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mt-4">
          
          {/* Health Score Circular Chart */}
          <div className="bg-surface-container-lowest/80 backdrop-blur-xl p-8 rounded-[2rem] border border-outline-variant/10 shadow-sm flex flex-col items-center">
            <h3 className="text-xl font-bold text-primary mb-8 w-full text-left">Genel Sağlık Skoru</h3>
            
            <div className="relative w-64 h-64 flex items-center justify-center">
              {/* Background Circle */}
              <svg className="w-full h-full rotate-[-90deg]" viewBox="0 0 100 100">
                <circle 
                  cx="50" cy="50" r="40" 
                  className="fill-none stroke-surface-container-high" 
                  strokeWidth="12"
                />
                {/* Foreground Circle (88%) */}
                <circle 
                  cx="50" cy="50" r="40" 
                  className="fill-none stroke-primary drop-shadow-lg transition-all duration-1000 ease-out" 
                  strokeWidth="12" 
                  strokeDasharray="251.2" 
                  strokeDashoffset="30.14" // 251.2 * (1 - 0.88)
                  strokeLinecap="round"
                />
              </svg>
              <div className="absolute flex flex-col items-center">
                <span className="text-5xl font-extrabold text-on-surface">%88</span>
                <span className="text-sm font-bold text-on-surface-variant opacity-80 mt-1">Çok Sağlıklı</span>
              </div>
            </div>

            <p className="text-sm text-center text-on-surface-variant mt-8 font-medium px-4">
              Bitkileriniz genel olarak harika durumda! Aloe Vera'nızın biraz daha güneşe ihtiyacı olabilir.
            </p>
          </div>

          {/* Tasks Distribution Horizontal Bar Chart */}
          <div className="bg-surface-container-lowest/80 backdrop-blur-xl p-8 rounded-[2rem] border border-outline-variant/10 shadow-sm flex flex-col">
            <h3 className="text-xl font-bold text-primary mb-8">Görev Dağılımı (Son 30 Gün)</h3>
            
            <div className="space-y-6 flex-1 flex flex-col justify-center">
              
              <div className="space-y-2">
                <div className="flex justify-between text-sm font-bold">
                  <span className="flex items-center gap-2"><span className="w-3 h-3 rounded-full bg-[#42a5f5]"></span>Sulama</span>
                  <span className="text-on-surface-variant">%60</span>
                </div>
                <div className="w-full bg-surface-container-high h-4 rounded-full overflow-hidden">
                  <div className="bg-[#42a5f5] w-[60%] h-full rounded-full transition-all duration-1000 ease-out"></div>
                </div>
              </div>

              <div className="space-y-2">
                <div className="flex justify-between text-sm font-bold">
                  <span className="flex items-center gap-2"><span className="w-3 h-3 rounded-full bg-[#ab47bc]"></span>Yaprak Temizliği</span>
                  <span className="text-on-surface-variant">%20</span>
                </div>
                <div className="w-full bg-surface-container-high h-4 rounded-full overflow-hidden">
                  <div className="bg-[#ab47bc] w-[20%] h-full rounded-full transition-all duration-1000 ease-out"></div>
                </div>
              </div>

              <div className="space-y-2">
                <div className="flex justify-between text-sm font-bold">
                  <span className="flex items-center gap-2"><span className="w-3 h-3 rounded-full bg-[#8d6e63]"></span>Gübreleme</span>
                  <span className="text-on-surface-variant">%15</span>
                </div>
                <div className="w-full bg-surface-container-high h-4 rounded-full overflow-hidden">
                  <div className="bg-[#8d6e63] w-[15%] h-full rounded-full transition-all duration-1000 ease-out"></div>
                </div>
              </div>

              <div className="space-y-2">
                <div className="flex justify-between text-sm font-bold">
                  <span className="flex items-center gap-2"><span className="w-3 h-3 rounded-full bg-primary"></span>Saksı Değişimi</span>
                  <span className="text-on-surface-variant">%5</span>
                </div>
                <div className="w-full bg-surface-container-high h-4 rounded-full overflow-hidden">
                  <div className="bg-primary w-[5%] h-full rounded-full transition-all duration-1000 ease-out"></div>
                </div>
              </div>

            </div>
          </div>

          {/* Water Consumption Vertical Bar Chart */}
          <div className="lg:col-span-2 bg-surface-container-lowest/80 backdrop-blur-xl p-8 rounded-[2rem] border border-outline-variant/10 shadow-sm">
            <h3 className="text-xl font-bold text-primary mb-8">Haftalık Su Tüketim Trendi (Litre)</h3>
            
            <div className="h-64 flex items-end justify-between gap-2 sm:gap-6 pt-4 border-b-2 border-outline-variant/20 relative">
              {/* Y-axis labels */}
              <div className="absolute left-0 top-0 bottom-0 flex flex-col justify-between text-[10px] font-bold text-on-surface-variant opacity-50 py-2">
                <span>5L</span>
                <span>4L</span>
                <span>3L</span>
                <span>2L</span>
                <span>1L</span>
                <span>0L</span>
              </div>

              {/* Bars */}
              <div className="flex-1 flex justify-around items-end h-full ml-8">
                {/* Week 1 */}
                <div className="w-8 sm:w-16 h-[60%] bg-secondary-container rounded-t-xl relative group transition-all duration-500 hover:opacity-80">
                  <div className="absolute -top-8 left-1/2 -translate-x-1/2 bg-surface-container-high text-xs font-bold px-2 py-1 rounded-lg opacity-0 group-hover:opacity-100 transition-opacity">3.0L</div>
                  <div className="absolute -bottom-8 left-1/2 -translate-x-1/2 text-xs font-bold text-on-surface-variant whitespace-nowrap">1. Hafta</div>
                </div>
                {/* Week 2 */}
                <div className="w-8 sm:w-16 h-[80%] bg-secondary-container rounded-t-xl relative group transition-all duration-500 hover:opacity-80">
                  <div className="absolute -top-8 left-1/2 -translate-x-1/2 bg-surface-container-high text-xs font-bold px-2 py-1 rounded-lg opacity-0 group-hover:opacity-100 transition-opacity">4.0L</div>
                  <div className="absolute -bottom-8 left-1/2 -translate-x-1/2 text-xs font-bold text-on-surface-variant whitespace-nowrap">2. Hafta</div>
                </div>
                {/* Week 3 */}
                <div className="w-8 sm:w-16 h-[40%] bg-secondary-container rounded-t-xl relative group transition-all duration-500 hover:opacity-80">
                  <div className="absolute -top-8 left-1/2 -translate-x-1/2 bg-surface-container-high text-xs font-bold px-2 py-1 rounded-lg opacity-0 group-hover:opacity-100 transition-opacity">2.0L</div>
                  <div className="absolute -bottom-8 left-1/2 -translate-x-1/2 text-xs font-bold text-on-surface-variant whitespace-nowrap">3. Hafta</div>
                </div>
                {/* Week 4 (Current) */}
                <div className="w-8 sm:w-16 h-[70%] bg-primary rounded-t-xl relative group shadow-[0_0_15px_rgba(var(--color-primary),0.5)] transition-all duration-500">
                  <div className="absolute -top-8 left-1/2 -translate-x-1/2 bg-surface-container-high text-xs font-bold px-2 py-1 rounded-lg opacity-0 group-hover:opacity-100 transition-opacity">3.5L</div>
                  <div className="absolute -bottom-8 left-1/2 -translate-x-1/2 text-xs font-bold text-primary whitespace-nowrap">Bu Hafta</div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </main>
  )
}
