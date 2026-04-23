import React, { useState } from 'react';

export default function PlantProfile() {
  const [note, setNote] = useState("Geçen hafta yapraklarında hafif sararma vardı, yerini pencereye biraz daha yaklaştırdıktan sonra hızla toparladı. Yeni filizler veriyor, şimdilik keyfi çok yerinde.");
  const [isEditingNote, setIsEditingNote] = useState(false);
  const [draftNote, setDraftNote] = useState("");
  const [plantImage, setPlantImage] = useState("https://lh3.googleusercontent.com/aida-public/AB6AXuA8kv09RDWl_QKvbPY4WMUqInWnq1Wvwkpxac9Xx0THueFaO-aCmMhD2cfcibNmlEqi0hRfvgWFDTN4w2lxeiOi0KX5mWGFjDgFpQCWh3j6ooXIuV6eLOLahCmAxQsmx89m_o6PuLaXhLlUB1BYSlfdLKfuZofGXl34c5vi3BBF8eRtt4iFMvBDyeko0yUTpVZHx9yL7Ow3NVpLzaXA4TLV4VRCVkdoAC8rollQ2qS-f8f5l8NLsblpde8hm9m5Quf-e_dmQivtIQc");
  const [wateredAt, setWateredAt] = useState(null);
  const [wateringAnim, setWateringAnim] = useState(false);

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setPlantImage(URL.createObjectURL(file));
    }
  };

  const handleWater = () => {
    setWateringAnim(true);
    setTimeout(() => {
      setWateredAt(new Date());
      setWateringAnim(false);
    }, 1200);
  };

  const handleEditClick = () => {
    setDraftNote(note);
    setIsEditingNote(true);
  };

  const handleSaveClick = () => {
    setNote(draftNote);
    setIsEditingNote(false);
  };

  return (
    <div className="bg-surface-container-lowest rounded-[2.5rem] p-8 md:p-12 shadow-sm relative overflow-hidden">
      {/* Glassmorphism decorative circles */}
      <div className="absolute -top-24 -right-24 w-64 h-64 bg-secondary-container/30 rounded-full blur-3xl"></div>
      <div className="absolute top-1/2 -left-32 w-48 h-48 bg-primary-fixed/20 rounded-full blur-3xl"></div>
      <div className="relative z-10 flex flex-col md:flex-row gap-12">
        {/* Image Section */}
        <div className="flex flex-col items-center gap-6">
          <div className="relative">
            <div className="w-64 h-64 rounded-full p-2 bg-gradient-to-tr from-primary to-secondary-fixed">
              <div className="w-full h-full rounded-full overflow-hidden bg-surface-container-high flex items-center justify-center relative">
                <img
                  className="w-full h-full object-cover"
                  alt="Bitki fotoğrafı"
                  src={plantImage}
                />
                <label className="absolute inset-0 bg-black/30 flex flex-col items-center justify-center opacity-0 hover:opacity-100 transition-opacity cursor-pointer">
                  <span className="bg-white text-primary px-4 py-2 rounded-full text-xs font-bold shadow-lg flex items-center gap-2 hover:scale-105 transition-transform">
                    <span className="material-symbols-outlined text-[16px]">add_a_photo</span>
                    Resim Ekle
                  </span>
                  <input 
                    type="file" 
                    accept="image/*" 
                    className="hidden" 
                    onChange={handleImageChange}
                  />
                </label>
              </div>
            </div>
            <div className="absolute bottom-4 right-4 bg-primary text-on-primary p-3 rounded-full shadow-xl">
              <span
                className="material-symbols-outlined"
                style={{ fontVariationSettings: "'FILL' 1" }}
              >
                eco
              </span>
            </div>
          </div>
          <div className="text-center">
            <h2 className="text-3xl font-extrabold text-primary tracking-tight">
              Barış Çiçeği
            </h2>
            <p className="text-on-surface-variant font-medium">Spathiphyllum</p>
          </div>
        </div>
        {/* Stats & Actions Section */}
        <div className="flex-1 flex flex-col justify-between">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
            <div className="bg-surface-container-low p-4 rounded-2xl flex flex-col gap-1">
              <span className="text-[10px] uppercase tracking-tighter font-bold text-on-surface-variant">
                Konum
              </span>
              <span className="font-bold text-primary">Salon</span>
            </div>
            <div className="bg-surface-container-low p-4 rounded-2xl flex flex-col gap-1">
              <span className="text-[10px] uppercase tracking-tighter font-bold text-on-surface-variant">
                Son Sulama
              </span>
              <span className="font-bold text-primary">2 gün önce</span>
            </div>
            <div className="bg-surface-container-low p-4 rounded-2xl flex flex-col gap-1">
              <span className="text-[10px] uppercase tracking-tighter font-bold text-on-surface-variant">
                Son Gübre
              </span>
              <span className="font-bold text-primary">1 ay önce</span>
            </div>
          </div>
          <div className="mb-10">
            <h4 className="text-sm font-bold text-on-surface-variant uppercase tracking-widest mb-4">
              Bakım İhtiyacı
            </h4>
            <div className="flex flex-wrap gap-4">
              <div className="flex items-center gap-3 bg-secondary-fixed text-on-secondary-fixed px-5 py-3 rounded-full">
                <span className="material-symbols-outlined text-xl">opacity</span>
                <span className="font-bold">Sulama: Orta</span>
              </div>
              <div className="flex items-center gap-3 bg-tertiary-fixed text-on-tertiary-fixed px-5 py-3 rounded-full">
                <span className="material-symbols-outlined text-xl">light_mode</span>
                <span className="font-bold">Işık: Dolaylı Güneş</span>
              </div>
            </div>
          </div>
          <div className="mb-8">
            <h4 className="text-sm font-bold text-on-surface-variant uppercase tracking-widest mb-3">
              Son Notlar
            </h4>
            
            {isEditingNote ? (
              <div className="bg-surface-container-high/50 border border-outline-variant/30 p-4 rounded-2xl flex flex-col gap-3">
                <textarea 
                  value={draftNote}
                  onChange={(e) => setDraftNote(e.target.value)}
                  className="w-full bg-surface-container-lowest border-none rounded-xl p-3 text-sm focus:ring-2 focus:ring-primary focus:bg-surface-bright transition-all resize-none h-24 text-on-surface"
                  placeholder="Çiçeğinizin durumu hakkında notlar alın..."
                  autoFocus
                />
                <div className="flex justify-end gap-2">
                  <button 
                    onClick={() => setIsEditingNote(false)}
                    className="px-4 py-2 text-xs font-bold text-on-surface-variant hover:bg-surface-container-highest rounded-xl transition-all"
                  >
                    İptal
                  </button>
                  <button 
                    onClick={handleSaveClick}
                    className="bg-primary text-on-primary px-4 py-2 rounded-xl text-xs font-bold hover:shadow-md transition-all"
                  >
                    Kaydet
                  </button>
                </div>
              </div>
            ) : (
              <div className="bg-surface-container-high/50 border border-outline-variant/10 p-4 rounded-2xl relative group">
                <span className="material-symbols-outlined absolute top-4 right-4 text-on-surface-variant opacity-20 text-4xl">format_quote</span>
                <p className="text-sm text-on-surface-variant italic font-medium relative z-10 pr-8 min-h-[3rem]">
                  {note ? `"${note}"` : <span className="opacity-50">Henüz bir not eklenmedi...</span>}
                </p>
                <div className="flex justify-between items-end mt-3">
                  <div className="text-[10px] text-primary font-bold uppercase tracking-wider">
                    {note ? "ŞİMDİ GÜNCELLENDİ" : ""}
                  </div>
                </div>
              </div>
            )}
          </div>
          <div className="flex flex-col sm:flex-row gap-4 mt-auto">
            {/* Watering Button */}
            <button
              onClick={handleWater}
              disabled={wateringAnim}
              className={`flex-1 rounded-2xl py-4 font-bold flex items-center justify-center gap-2 transition-all
                ${wateredAt
                  ? 'bg-secondary-container text-on-secondary-container hover:bg-secondary-container/80'
                  : 'bg-gradient-to-r from-primary to-primary-container text-on-primary hover:shadow-lg active:scale-95'
                } ${wateringAnim ? 'animate-pulse cursor-wait' : ''}`}
            >
              <span className="material-symbols-outlined" style={{ fontVariationSettings: wateringAnim ? "'FILL' 0" : "'FILL' 1" }}>
                {wateringAnim ? 'hourglass_top' : wateredAt ? 'water_drop' : 'check_circle'}
              </span>
              {wateringAnim
                ? 'Kaydediliyor...'
                : wateredAt
                  ? `Sulandı \u2022 ${wateredAt.toLocaleTimeString('tr-TR', { hour: '2-digit', minute: '2-digit' })}`
                  : 'Sulanmış Olarak İşaretle'
              }
            </button>
            <button 
              onClick={handleEditClick}
              className="flex-1 bg-secondary-container text-on-secondary-container rounded-2xl py-4 font-bold flex items-center justify-center gap-2 hover:bg-outline-variant/30 transition-all"
            >
              <span className="material-symbols-outlined">edit_note</span>
              {note ? 'Notu Düzenle' : 'Not Ekle'}
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}
