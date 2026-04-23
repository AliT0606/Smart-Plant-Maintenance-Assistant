import React, { useState } from 'react'

const PLANTS_DATA = [
  {
    id: 1,
    name: "Barış Çiçeği",
    scientific: "Spathiphyllum",
    image: "https://images.unsplash.com/photo-1593696954577-ab3d39317b97?auto=format&fit=crop&w=600&q=80",
    water: "Haftada Bir",
    light: "Dolaylı Işık",
    difficulty: "Kolay",
    isToxic: true,
    airPurifying: true,
  },
  {
    id: 2,
    name: "Deve Tabanı",
    scientific: "Monstera Deliciosa",
    image: "https://images.unsplash.com/photo-1614594975525-e45190c55d0b?auto=format&fit=crop&w=600&q=80",
    water: "Toprak Kurudukça",
    light: "Aydınlık / Yarı Gölge",
    difficulty: "Orta",
    isToxic: true,
    airPurifying: false,
  },
  {
    id: 3,
    name: "Paşa Kılıcı",
    scientific: "Sansevieria Trifasciata",
    image: "https://images.unsplash.com/photo-1599598425947-330026e10f13?auto=format&fit=crop&w=600&q=80",
    water: "2-3 Haftada Bir",
    light: "Düşük Işığa Toleranslı",
    difficulty: "Çok Kolay",
    isToxic: true,
    airPurifying: true,
  },
  {
    id: 4,
    name: "Aloe Vera",
    scientific: "Aloe barbadensis miller",
    image: "https://images.unsplash.com/photo-1596547609652-9cb5d8d10b7b?auto=format&fit=crop&w=600&q=80",
    water: "Ayda Bir",
    light: "Doğrudan Güneş",
    difficulty: "Kolay",
    isToxic: true,
    airPurifying: true,
  },
  {
    id: 5,
    name: "Aşk Merdiveni",
    scientific: "Nephrolepis Exaltata",
    image: "https://images.unsplash.com/photo-1597561848529-68ff37803d3c?auto=format&fit=crop&w=600&q=80",
    water: "Sık Sulama / Yüksek Nem",
    light: "Dolaylı Işık / Gölge",
    difficulty: "Zor",
    isToxic: false,
    airPurifying: true,
  },
  {
    id: 6,
    name: "Kurdele Çiçeği",
    scientific: "Chlorophytum Comosum",
    image: "https://images.unsplash.com/photo-1610419330689-f538eec80f55?auto=format&fit=crop&w=600&q=80",
    water: "Haftada Bir",
    light: "Dolaylı Işık",
    difficulty: "Kolay",
    isToxic: false,
    airPurifying: true,
  }
];

export default function Library() {
  const [searchTerm, setSearchTerm] = useState("");

  const filteredPlants = PLANTS_DATA.filter(plant => 
    plant.name.toLowerCase().includes(searchTerm.toLowerCase()) || 
    plant.scientific.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <main className="pl-72 pt-20 pb-16 min-h-screen font-body">
      <div className="p-8 max-w-7xl mx-auto flex flex-col gap-8">
        
        {/* Header */}
        <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-6">
          <div>
            <h2 className="text-3xl font-extrabold text-primary tracking-tight mb-2">Bitki Kütüphanesi</h2>
            <p className="text-on-surface-variant">Yüzlerce bitki türünün bakım sırlarını keşfedin.</p>
          </div>
          
          <div className="relative w-full md:w-80">
            <input
              type="text"
              placeholder="Bitki veya bilimsel ad ara..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full bg-surface-container border-none rounded-2xl px-6 py-4 pl-12 focus:ring-2 focus:ring-primary focus:bg-surface-bright transition-all font-medium"
            />
            <span className="material-symbols-outlined absolute left-4 top-4 text-on-surface-variant">
              search
            </span>
          </div>
        </div>

        {/* Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mt-4">
          {filteredPlants.map(plant => (
            <div key={plant.id} className="bg-surface-container-lowest/80 backdrop-blur-xl rounded-[2rem] p-6 shadow-sm border border-outline-variant/10 hover:shadow-md transition-shadow group flex flex-col">
              
              {/* Image */}
              <div className="w-full h-48 rounded-[1.5rem] overflow-hidden mb-6 relative">
                {/* Fallback to gradient if image fails */}
                <div className="w-full h-full bg-surface-container-high absolute inset-0 -z-10"></div>
                <img 
                  src={plant.image} 
                  alt={plant.name} 
                  className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" 
                  onError={(e) => {e.target.src="https://images.unsplash.com/photo-1416879573089-13009d73d6e3?auto=format&fit=crop&w=400&q=80"}} 
                />
                
                {/* Top Badges */}
                <div className="absolute top-3 right-3 flex gap-2">
                  {plant.airPurifying && (
                    <div className="bg-surface-container-lowest/90 backdrop-blur-md text-primary px-3 py-1.5 rounded-full text-[10px] font-bold uppercase tracking-wider flex items-center gap-1 shadow-sm">
                      <span className="material-symbols-outlined text-sm">air</span>
                      Hava Temizler
                    </div>
                  )}
                  {plant.isToxic && (
                    <div className="bg-error/10 backdrop-blur-md text-error px-3 py-1.5 rounded-full text-[10px] font-bold uppercase tracking-wider flex items-center gap-1 shadow-sm">
                      <span className="material-symbols-outlined text-sm">pets</span>
                      Toksik
                    </div>
                  )}
                </div>
              </div>

              {/* Title & Info */}
              <div className="flex-1 flex flex-col">
                <h3 className="text-xl font-extrabold text-on-surface leading-tight mb-1">{plant.name}</h3>
                <p className="text-sm font-bold text-on-surface-variant italic mb-6 opacity-80">{plant.scientific}</p>
                
                <div className="flex flex-col gap-3 mt-auto">
                  {/* Water Need */}
                  <div className="flex items-center gap-3 bg-secondary-fixed/50 px-4 py-3 rounded-2xl">
                    <div className="w-8 h-8 rounded-full bg-secondary-fixed text-on-secondary-fixed flex items-center justify-center shrink-0">
                      <span className="material-symbols-outlined text-[18px]">water_drop</span>
                    </div>
                    <div>
                      <p className="text-[10px] uppercase tracking-widest font-bold text-on-surface-variant opacity-70">Su İhtiyacı</p>
                      <p className="text-sm font-bold text-on-surface">{plant.water}</p>
                    </div>
                  </div>

                  {/* Light Need */}
                  <div className="flex items-center gap-3 bg-tertiary-fixed/50 px-4 py-3 rounded-2xl">
                    <div className="w-8 h-8 rounded-full bg-tertiary-fixed text-on-tertiary-fixed flex items-center justify-center shrink-0">
                      <span className="material-symbols-outlined text-[18px]">light_mode</span>
                    </div>
                    <div>
                      <p className="text-[10px] uppercase tracking-widest font-bold text-on-surface-variant opacity-70">Işık İhtiyacı</p>
                      <p className="text-sm font-bold text-on-surface">{plant.light}</p>
                    </div>
                  </div>

                  {/* Difficulty */}
                  <div className="flex items-center gap-3 bg-primary-container/30 px-4 py-3 rounded-2xl mt-1">
                    <div className="w-8 h-8 rounded-full bg-primary-container text-on-primary-container flex items-center justify-center shrink-0">
                      <span className="material-symbols-outlined text-[18px]">psychology</span>
                    </div>
                    <div>
                      <p className="text-[10px] uppercase tracking-widest font-bold text-on-surface-variant opacity-70">Bakım Zorluğu</p>
                      <p className="text-sm font-bold text-on-surface">{plant.difficulty}</p>
                    </div>
                  </div>
                </div>
              </div>

            </div>
          ))}

          {filteredPlants.length === 0 && (
            <div className="col-span-full py-16 text-center bg-surface-container-lowest/50 rounded-[2rem] border border-outline-variant/10">
              <span className="material-symbols-outlined text-6xl text-on-surface-variant opacity-20 mb-4">search_off</span>
              <p className="text-xl font-bold text-on-surface-variant">Aradığınız bitki bulunamadı.</p>
              <p className="text-sm text-on-surface-variant opacity-70 mt-2">Lütfen başka bir isimle tekrar deneyin.</p>
            </div>
          )}
        </div>

      </div>
    </main>
  )
}
