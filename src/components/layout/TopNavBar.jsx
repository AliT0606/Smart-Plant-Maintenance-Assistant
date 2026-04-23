import { useState, useRef, useEffect } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useTheme } from '../../context/ThemeContext.jsx'

const SEARCHABLE_PLANTS = [
  { id: 1, name: "Barış Çiçeği", type: "Salon Bitkisi", icon: "eco" },
  { id: 2, name: "Deve Tabanı", type: "Tropikal", icon: "energy_savings_leaf" },
  { id: 3, name: "Paşa Kılıcı", type: "Sukulent", icon: "grass" },
  { id: 4, name: "Aloe Vera", type: "Sukulent", icon: "local_florist" },
  { id: 5, name: "Aşk Merdiveni", type: "Erelti Otu", icon: "psychiatry" },
  { id: 6, name: "Kurdele Çiçeği", type: "Salon Bitkisi", icon: "potted_plant" }
];

const NOTIFICATIONS = [
  { id: 1, icon: 'water_drop', color: 'text-blue-400', bg: 'bg-blue-50', title: 'Sulama Zamanı!', body: 'Barış Çiçeği bugün sulanmalı.', time: '5 dk önce', read: false },
  { id: 2, icon: 'wb_sunny', color: 'text-amber-400', bg: 'bg-amber-50', title: 'Güneş Uyarısı', body: 'Deve Tabanı doğrudan güneşten uzak tutun.', time: '1 sa önce', read: false },
  { id: 3, icon: 'compost', color: 'text-green-500', bg: 'bg-green-50', title: 'Gübreleme Hatırlatıcısı', body: 'Aloe Vera bu haftaki gübrelemesini bekliyor.', time: '3 sa önce', read: true },
  { id: 4, icon: 'potted_plant', color: 'text-primary', bg: 'bg-primary-container/30', title: 'Saksı Değişimi', body: 'Orkide için saksı değişimi zamanı geldi.', time: 'Dün', read: true },
]

export default function TopNavBar() {
  const [searchQuery, setSearchQuery] = useState('');
  const [isSearchOpen, setIsSearchOpen] = useState(false);
  const [isNotifOpen, setIsNotifOpen] = useState(false);
  const [isUserOpen, setIsUserOpen] = useState(false);
  const [notifications, setNotifications] = useState(NOTIFICATIONS);
  const searchRef = useRef(null);
  const notifRef = useRef(null);
  const userRef = useRef(null);
  const navigate = useNavigate();
  const { isDark, toggleTheme } = useTheme();

  const unreadCount = notifications.filter(n => !n.read).length;

  useEffect(() => {
    function handleClickOutside(event) {
      if (searchRef.current && !searchRef.current.contains(event.target)) setIsSearchOpen(false);
      if (notifRef.current && !notifRef.current.contains(event.target)) setIsNotifOpen(false);
      if (userRef.current && !userRef.current.contains(event.target)) setIsUserOpen(false);
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  const filteredPlants = SEARCHABLE_PLANTS.filter(plant =>
    plant.name.toLowerCase().includes(searchQuery.toLowerCase())
  );

  const handlePlantClick = () => {
    setSearchQuery('');
    setIsSearchOpen(false);
    navigate('/dashboard/library');
  };

  const markAllRead = () => setNotifications(prev => prev.map(n => ({ ...n, read: true })));

  return (
    <header className="bg-background/80 backdrop-blur-xl fixed top-0 z-50 flex justify-between items-center w-full px-8 h-20 transition-colors duration-300 border-b border-outline-variant/10">
      <div className="text-2xl font-extrabold text-primary tracking-tighter">
        Akıllı Bahçe - Akıllı Bitki Bakım Asistanı
      </div>
      <div className="flex items-center gap-3">

        {/* Search Bar */}
        <div className="relative hidden lg:block" ref={searchRef}>
          <input
            className="bg-surface-container-high border-none rounded-full px-6 py-2 w-72 focus:ring-2 focus:ring-primary focus:bg-surface-bright text-sm transition-all outline-none relative z-20"
            placeholder="Bitki Ara..."
            type="text"
            value={searchQuery}
            onChange={(e) => { setSearchQuery(e.target.value); setIsSearchOpen(true); }}
            onFocus={() => setIsSearchOpen(true)}
          />
          <span className="material-symbols-outlined absolute right-4 top-2 text-on-surface-variant pointer-events-none z-20">search</span>
          {isSearchOpen && searchQuery.length > 0 && (
            <div className="absolute top-12 left-0 w-full bg-surface-container-lowest border border-outline-variant/20 rounded-2xl shadow-xl overflow-hidden z-30 pt-2">
              {filteredPlants.length > 0 ? (
                <div className="flex flex-col max-h-64 overflow-y-auto">
                  {filteredPlants.map(plant => (
                    <button key={plant.id} onClick={handlePlantClick}
                      className="flex items-center gap-3 px-4 py-3 hover:bg-surface-container-high transition-colors text-left w-full border-b border-outline-variant/10 last:border-0">
                      <div className="w-8 h-8 rounded-full bg-primary/10 text-primary flex items-center justify-center shrink-0">
                        <span className="material-symbols-outlined text-[18px]">{plant.icon}</span>
                      </div>
                      <div className="flex flex-col">
                        <span className="text-sm font-bold text-on-surface">{plant.name}</span>
                        <span className="text-[10px] uppercase tracking-widest text-on-surface-variant font-bold">{plant.type}</span>
                      </div>
                    </button>
                  ))}
                </div>
              ) : (
                <div className="px-4 py-6 text-center text-on-surface-variant text-sm font-medium">Sonuç bulunamadı</div>
              )}
            </div>
          )}
        </div>

        {/* Dark Mode Toggle */}
        <button onClick={toggleTheme} title={isDark ? 'Aydınlık Mod' : 'Gece Modu'}
          className="material-symbols-outlined text-on-surface-variant hover:bg-surface-variant p-2 rounded-full transition-all">
          {isDark ? 'light_mode' : 'dark_mode'}
        </button>

        {/* Notifications */}
        <div className="relative" ref={notifRef}>
          <button
            onClick={() => { setIsNotifOpen(p => !p); setIsUserOpen(false); }}
            className="relative material-symbols-outlined text-on-surface-variant hover:bg-surface-variant p-2 rounded-full transition-all"
            style={{ fontVariationSettings: "'FILL' 1" }}
          >
            notifications
            {unreadCount > 0 && (
              <span className="absolute top-1 right-1 w-4 h-4 bg-error text-on-error text-[9px] font-extrabold rounded-full flex items-center justify-center">
                {unreadCount}
              </span>
            )}
          </button>

          {isNotifOpen && (
            <div className="absolute top-14 right-0 w-96 bg-surface-container-lowest border border-outline-variant/20 rounded-[1.5rem] shadow-2xl z-50 overflow-hidden">
              <div className="flex justify-between items-center px-5 py-4 border-b border-outline-variant/10">
                <h4 className="font-extrabold text-on-surface text-base">Bildirimler</h4>
                <button onClick={markAllRead} className="text-xs font-bold text-primary hover:underline">Tümünü Okundu Say</button>
              </div>
              <div className="flex flex-col max-h-80 overflow-y-auto">
                {notifications.map(n => (
                  <div key={n.id} className={`flex gap-4 px-5 py-4 border-b border-outline-variant/10 last:border-0 transition-colors ${n.read ? 'opacity-60' : 'bg-primary-container/10'}`}>
                    <div className={`w-10 h-10 rounded-2xl ${n.bg} ${n.color} flex items-center justify-center shrink-0`}>
                      <span className="material-symbols-outlined text-[20px]" style={{ fontVariationSettings: "'FILL' 1" }}>{n.icon}</span>
                    </div>
                    <div className="flex-1 min-w-0">
                      <div className="flex items-start justify-between gap-2">
                        <p className="text-sm font-bold text-on-surface">{n.title}</p>
                        {!n.read && <span className="w-2 h-2 bg-primary rounded-full shrink-0 mt-1"></span>}
                      </div>
                      <p className="text-xs text-on-surface-variant mt-0.5 leading-relaxed">{n.body}</p>
                      <p className="text-[10px] text-on-surface-variant opacity-60 mt-1 font-bold uppercase tracking-wide">{n.time}</p>
                    </div>
                  </div>
                ))}
              </div>
              <div className="px-5 py-3 text-center border-t border-outline-variant/10">
                <button className="text-xs font-bold text-primary hover:underline">Tüm Bildirimleri Gör</button>
              </div>
            </div>
          )}
        </div>

        {/* Settings Icon */}
        <Link to="/dashboard/settings" title="Ayarlar"
          className="material-symbols-outlined text-on-surface-variant hover:bg-surface-variant p-2 rounded-full transition-all">
          settings
        </Link>

        {/* User Avatar + Dropdown */}
        <div className="relative" ref={userRef}>
          <button
            onClick={() => { setIsUserOpen(p => !p); setIsNotifOpen(false); }}
            className="w-10 h-10 rounded-full bg-secondary-container overflow-hidden border-2 border-primary/20 hover:border-primary/60 transition-all focus:outline-none"
          >
            <img
              className="w-full h-full object-cover"
              alt="Kullanıcı avatarı"
              src="https://lh3.googleusercontent.com/aida-public/AB6AXuCphgaEV6IGWsXU69PEwvKDVYrrc56BDh1KxW7DL-S_cJ9C7zUxxLLUdAtd57z4QiNWnY-Tk9CI-UxV1CcgMkqhsuF803I7Ck3VmQ0CLVmMqP_LR4y67wd7q-xFV0d0SXDv9azwIHRhWZk8jibhoq5F_ImyCTpw9WHnpKjBYTDPsSXK0mUjfmyf3fKFel67oNj6YOopU95kiW0AUlZkVS-RrY0-uSenl5Y_2lHpE6rYDfgGXf3phunCZqm77oeiQa-OIffFYy-Et0A"
            />
          </button>

          {isUserOpen && (
            <div className="absolute top-14 right-0 w-64 bg-surface-container-lowest border border-outline-variant/20 rounded-[1.5rem] shadow-2xl z-50 overflow-hidden">
              {/* Profile info */}
              <div className="flex items-center gap-3 px-5 py-4 border-b border-outline-variant/10">
                <div className="w-10 h-10 rounded-full overflow-hidden border-2 border-primary/20 shrink-0">
                  <img className="w-full h-full object-cover" alt="avatar"
                    src="https://lh3.googleusercontent.com/aida-public/AB6AXuCphgaEV6IGWsXU69PEwvKDVYrrc56BDh1KxW7DL-S_cJ9C7zUxxLLUdAtd57z4QiNWnY-Tk9CI-UxV1CcgMkqhsuF803I7Ck3VmQ0CLVmMqP_LR4y67wd7q-xFV0d0SXDv9azwIHRhWZk8jibhoq5F_ImyCTpw9WHnpKjBYTDPsSXK0mUjfmyf3fKFel67oNj6YOopU95kiW0AUlZkVS-RrY0-uSenl5Y_2lHpE6rYDfgGXf3phunCZqm77oeiQa-OIffFYy-Et0A"
                  />
                </div>
                <div>
                  <p className="text-sm font-extrabold text-on-surface">Akıllı Bahçe Kullanıcısı</p>
                  <p className="text-xs text-on-surface-variant">kullanici@bahce.com</p>
                </div>
              </div>
              {/* Menu items */}
              <div className="flex flex-col py-2">
                <Link to="/dashboard/settings" onClick={() => setIsUserOpen(false)}
                  className="flex items-center gap-3 px-5 py-3 hover:bg-surface-container-high transition-colors text-sm font-bold text-on-surface">
                  <span className="material-symbols-outlined text-[20px] text-on-surface-variant">manage_accounts</span>
                  Profil Ayarları
                </Link>
                <button
                  onClick={toggleTheme}
                  className="flex items-center gap-3 px-5 py-3 hover:bg-surface-container-high transition-colors text-sm font-bold text-on-surface w-full text-left"
                >
                  <span className="material-symbols-outlined text-[20px] text-on-surface-variant">{isDark ? 'light_mode' : 'dark_mode'}</span>
                  {isDark ? 'Aydınlık Mod' : 'Gece Modu'}
                </button>
                <div className="mx-4 my-1 border-t border-outline-variant/20"></div>
                <Link to="/" onClick={() => setIsUserOpen(false)}
                  className="flex items-center gap-3 px-5 py-3 hover:bg-error-container/20 transition-colors text-sm font-bold text-error">
                  <span className="material-symbols-outlined text-[20px]">logout</span>
                  Çıkış Yap
                </Link>
              </div>
            </div>
          )}
        </div>

      </div>
    </header>
  )
}
