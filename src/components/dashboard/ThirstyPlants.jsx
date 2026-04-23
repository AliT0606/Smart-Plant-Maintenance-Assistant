import { useState } from 'react'

export default function ThirstyPlants() {
  const [searchQuery, setSearchQuery] = useState('');

  const thirstyPlants = [
    { name: 'Barış Çiçeği', task: 'Sulama' },
    { name: 'Sukulent', task: 'Su' },
    { name: 'Orkide', task: 'Gübre' },
    { name: 'Para Çiçeği', task: 'Kontrol' },
  ]

  const filteredPlants = thirstyPlants.filter(plant => 
    plant.name.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <div className="bg-surface-container-low rounded-3xl p-6 h-fit border border-outline-variant/10">
      <h3 className="text-xl font-bold text-primary mb-6 flex items-center gap-2">
        <span className="material-symbols-outlined text-primary">water_drop</span>
        Bugün Susayanlar
      </h3>
      <div className="space-y-3 min-h-[160px]">
        {filteredPlants.length > 0 ? (
          filteredPlants.map((plant, index) => (
            <label
              key={index}
              className="flex items-center gap-4 p-4 bg-surface-container-lowest rounded-2xl cursor-pointer hover:bg-surface-bright transition-all group"
            >
              <input
                className="w-5 h-5 rounded border-outline-variant text-primary focus:ring-primary"
                type="checkbox"
              />
              <div className="flex flex-col">
                <span className="font-bold text-on-surface group-hover:text-primary transition-colors">
                  {plant.name}
                </span>
                <span className="text-xs text-on-surface-variant">
                  {plant.task}
                </span>
              </div>
            </label>
          ))
        ) : (
          <div className="text-center py-8 text-on-surface-variant text-sm font-medium">
            Bitki bulunamadı
          </div>
        )}
      </div>
      <div className="mt-8 pt-6 border-t border-outline-variant/20">
        <div className="relative">
          <input
            className="w-full bg-surface-container border-none rounded-xl px-4 py-3 text-sm focus:ring-2 focus:ring-primary focus:bg-surface-bright outline-none"
            placeholder="Bitki Ara..."
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />
          <span className="material-symbols-outlined absolute right-3 top-2.5 text-on-surface-variant text-xl pointer-events-none">
            search
          </span>
        </div>
      </div>
    </div>
  )
}
