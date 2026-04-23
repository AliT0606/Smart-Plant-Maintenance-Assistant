import React, { useState, useEffect } from 'react'

const WEATHER_TIPS = [
  { temp: 32, condition: 'sunny', icon: 'wb_sunny', label: 'Güneşli', color: 'text-amber-500', tip: 'Hava çok sıcak! Balkon bitkilerini sabah erken sulayın, öğleden sonra doğrudan güneşe çıkarmayın.' },
  { temp: 24, condition: 'cloudy', icon: 'cloud', label: 'Bulutlu', color: 'text-blue-400', tip: 'Bulutlu bir gün — iç mekan bitkileri için ideal. Pencerenin kenarına almanızı öneririz.' },
  { temp: 18, condition: 'rainy', icon: 'rainy', label: 'Yağmurlu', color: 'text-sky-400', tip: 'Bugün yağmur bekleniyor. Balkon bitkilerini sulamamanıza gerek yok, fazla su kök çürüklüğüne yol açabilir.' },
  { temp: 28, condition: 'partly_cloudy', icon: 'partly_cloudy_day', label: 'Parçalı Bulutlu', color: 'text-yellow-400', tip: 'Güzel bir gün! Bitkileri doğal ışıktan faydalandırmak için pencere kenarına alabilirsiniz.' },
]

export default function WeatherWidget() {
  const [weather] = useState(WEATHER_TIPS[0]) // Mock: Güneşli
  const [currentTime, setCurrentTime] = useState(new Date())

  useEffect(() => {
    const timer = setInterval(() => setCurrentTime(new Date()), 60000)
    return () => clearInterval(timer)
  }, [])

  const timeStr = currentTime.toLocaleTimeString('tr-TR', { hour: '2-digit', minute: '2-digit' })
  const dateStr = currentTime.toLocaleDateString('tr-TR', { weekday: 'long', day: 'numeric', month: 'long' })

  return (
    <div className="bg-gradient-to-r from-primary-container/60 to-secondary-container/40 border border-primary/10 rounded-[2rem] p-6 flex flex-col sm:flex-row items-start sm:items-center gap-6 backdrop-blur-xl shadow-sm">
      {/* Weather Icon + Temp */}
      <div className="flex items-center gap-4 shrink-0">
        <span className={`material-symbols-outlined text-6xl ${weather.color}`} style={{ fontVariationSettings: "'FILL' 1" }}>
          {weather.icon}
        </span>
        <div>
          <div className="text-4xl font-extrabold text-on-surface">{weather.temp}°C</div>
          <div className="text-sm font-bold text-on-surface-variant">{weather.label}</div>
        </div>
      </div>

      {/* Divider */}
      <div className="hidden sm:block w-px h-16 bg-outline-variant/30"></div>

      {/* Tip */}
      <div className="flex-1">
        <div className="flex items-center gap-2 mb-1">
          <span className="material-symbols-outlined text-primary text-[18px]" style={{ fontVariationSettings: "'FILL' 1" }}>tips_and_updates</span>
          <span className="text-xs font-extrabold uppercase tracking-widest text-primary">Akıllı Öneri</span>
        </div>
        <p className="text-sm text-on-surface-variant font-medium leading-relaxed">{weather.tip}</p>
      </div>

      {/* Date + Time */}
      <div className="shrink-0 text-right hidden lg:block">
        <div className="text-2xl font-extrabold text-on-surface">{timeStr}</div>
        <div className="text-xs text-on-surface-variant font-medium capitalize">{dateStr}</div>
      </div>
    </div>
  )
}
