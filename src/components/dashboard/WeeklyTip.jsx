export default function WeeklyTip() {
  return (
    <div className="bg-primary-container text-on-primary-container p-6 rounded-3xl overflow-hidden relative group">
      <div className="relative z-10">
        <p className="text-xs uppercase tracking-widest font-bold opacity-80 mb-2">
          Haftalık İpucu
        </p>
        <h4 className="text-lg font-bold leading-tight">
          Bitkilerinizi sabah saatlerinde sulamak, mantar oluşumunu engeller.
        </h4>
      </div>
      <span className="material-symbols-outlined absolute -right-4 -bottom-4 text-8xl opacity-10 group-hover:scale-110 transition-transform">
        eco
      </span>
    </div>
  )
}
