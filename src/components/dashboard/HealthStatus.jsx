export default function HealthStatus() {
  return (
    <div className="bg-surface-container rounded-3xl p-6">
      <h5 className="font-bold text-primary mb-4 flex items-center gap-2">
        <span className="material-symbols-outlined text-primary">
          health_and_safety
        </span>
        Sağlık Durumu
      </h5>
      <div className="w-full bg-surface-container-high h-3 rounded-full overflow-hidden">
        <div className="bg-primary w-[85%] h-full rounded-full"></div>
      </div>
      <p className="text-xs text-on-surface-variant mt-2 font-medium">
        %85 - Çok Sağlıklı
      </p>
    </div>
  )
}
