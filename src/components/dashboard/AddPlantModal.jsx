import React, { useState } from 'react'

const PLANT_TYPES = ['Salon Bitkisi', 'Sukulent', 'Kaktüs', 'Tropikal', 'Eğrelti Otu', 'Orkide', 'Diğer']
const WATER_FREQ = ['Her gün', '2 günde bir', '3 günde bir', 'Haftada bir', '2 haftada bir', 'Ayda bir']
const LIGHT_NEEDS = ['Tam Güneş', 'Dolaylı Güneş', 'Yarı Gölge', 'Tam Gölge']

export default function AddPlantModal({ onClose }) {
  const [form, setForm] = useState({ name: '', type: '', water: '', light: '', location: '' })
  const [image, setImage] = useState(null)
  const [imagePreview, setImagePreview] = useState(null)
  const [saved, setSaved] = useState(false)

  const handleImageChange = (e) => {
    const file = e.target.files[0]
    if (file) {
      setImage(file)
      setImagePreview(URL.createObjectURL(file))
    }
  }

  const handleSave = (e) => {
    e.preventDefault()
    setSaved(true)
    setTimeout(() => {
      onClose()
    }, 1500)
  }

  return (
    <div className="fixed inset-0 z-[200] flex items-center justify-center p-4">
      {/* Backdrop */}
      <div 
        className="absolute inset-0 bg-black/60 backdrop-blur-sm"
        onClick={onClose}
      />

      {/* Modal Card */}
      <div className="relative w-full max-w-lg bg-surface rounded-[2.5rem] shadow-2xl p-8 z-10 overflow-y-auto max-h-[90vh]">
        {/* Header */}
        <div className="flex justify-between items-center mb-8">
          <div>
            <h3 className="text-2xl font-extrabold text-primary">Yeni Bitki Ekle</h3>
            <p className="text-sm text-on-surface-variant mt-1">Bahçenize yeni bir üye katılıyor 🌿</p>
          </div>
          <button 
            onClick={onClose}
            className="material-symbols-outlined text-on-surface-variant hover:bg-surface-variant p-2 rounded-full transition-all"
          >
            close
          </button>
        </div>

        {/* Success State */}
        {saved ? (
          <div className="flex flex-col items-center py-12 gap-4">
            <div className="w-20 h-20 rounded-full bg-primary-container flex items-center justify-center animate-bounce">
              <span className="material-symbols-outlined text-4xl text-primary" style={{ fontVariationSettings: "'FILL' 1" }}>check_circle</span>
            </div>
            <p className="text-xl font-extrabold text-on-surface">Bitki Eklendi!</p>
            <p className="text-on-surface-variant text-sm">{form.name || 'Bitkinin'} bahçenize hoş geldi 🎉</p>
          </div>
        ) : (
          <form onSubmit={handleSave} className="flex flex-col gap-5">
            {/* Image Upload */}
            <label className="cursor-pointer">
              <div className={`w-full h-40 rounded-2xl border-2 border-dashed border-outline-variant/50 flex flex-col items-center justify-center gap-2 hover:border-primary hover:bg-primary-container/10 transition-all overflow-hidden ${imagePreview ? 'border-0' : ''}`}>
                {imagePreview ? (
                  <img src={imagePreview} alt="preview" className="w-full h-full object-cover" />
                ) : (
                  <>
                    <span className="material-symbols-outlined text-4xl text-on-surface-variant opacity-40">add_a_photo</span>
                    <span className="text-sm font-bold text-on-surface-variant opacity-60">Fotoğraf ekle (isteğe bağlı)</span>
                  </>
                )}
              </div>
              <input type="file" accept="image/*" className="hidden" onChange={handleImageChange} />
            </label>

            {/* Plant Name */}
            <div>
              <label className="text-xs font-extrabold uppercase tracking-widest text-on-surface-variant mb-2 block">Bitki Adı *</label>
              <input 
                required
                className="w-full bg-surface-container rounded-xl px-4 py-3 text-sm outline-none focus:ring-2 focus:ring-primary text-on-surface"
                placeholder="Örn: Barış Çiçeğim"
                value={form.name}
                onChange={e => setForm({...form, name: e.target.value})}
              />
            </div>

            {/* Type */}
            <div>
              <label className="text-xs font-extrabold uppercase tracking-widest text-on-surface-variant mb-2 block">Bitki Türü</label>
              <select 
                className="w-full bg-surface-container rounded-xl px-4 py-3 text-sm outline-none focus:ring-2 focus:ring-primary text-on-surface appearance-none"
                value={form.type}
                onChange={e => setForm({...form, type: e.target.value})}
              >
                <option value="">Seçin...</option>
                {PLANT_TYPES.map(t => <option key={t} value={t}>{t}</option>)}
              </select>
            </div>

            {/* Water + Light */}
            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="text-xs font-extrabold uppercase tracking-widest text-on-surface-variant mb-2 block">💧 Sulama Sıklığı</label>
                <select 
                  className="w-full bg-surface-container rounded-xl px-3 py-3 text-sm outline-none focus:ring-2 focus:ring-primary text-on-surface appearance-none"
                  value={form.water}
                  onChange={e => setForm({...form, water: e.target.value})}
                >
                  <option value="">Seçin...</option>
                  {WATER_FREQ.map(w => <option key={w} value={w}>{w}</option>)}
                </select>
              </div>
              <div>
                <label className="text-xs font-extrabold uppercase tracking-widest text-on-surface-variant mb-2 block">☀️ Işık İhtiyacı</label>
                <select 
                  className="w-full bg-surface-container rounded-xl px-3 py-3 text-sm outline-none focus:ring-2 focus:ring-primary text-on-surface appearance-none"
                  value={form.light}
                  onChange={e => setForm({...form, light: e.target.value})}
                >
                  <option value="">Seçin...</option>
                  {LIGHT_NEEDS.map(l => <option key={l} value={l}>{l}</option>)}
                </select>
              </div>
            </div>

            {/* Location */}
            <div>
              <label className="text-xs font-extrabold uppercase tracking-widest text-on-surface-variant mb-2 block">📍 Konum</label>
              <input 
                className="w-full bg-surface-container rounded-xl px-4 py-3 text-sm outline-none focus:ring-2 focus:ring-primary text-on-surface"
                placeholder="Örn: Salon, Balkon, Yatak Odası..."
                value={form.location}
                onChange={e => setForm({...form, location: e.target.value})}
              />
            </div>

            {/* Save Button */}
            <button 
              type="submit"
              className="w-full bg-primary text-on-primary py-4 rounded-2xl font-extrabold text-base hover:opacity-90 hover:shadow-lg transition-all mt-2 flex items-center justify-center gap-2"
            >
              <span className="material-symbols-outlined" style={{ fontVariationSettings: "'FILL' 1" }}>local_florist</span>
              Bahçeme Ekle
            </button>
          </form>
        )}
      </div>
    </div>
  )
}
