export default function UpcomingTasks() {
  return (
    <div className="bg-surface-container rounded-3xl p-6">
      <h5 className="font-bold text-primary mb-4 flex items-center gap-2">
        <span className="material-symbols-outlined text-primary">history</span>
        Yaklaşan Görevler
      </h5>
      <ul className="text-sm space-y-2 text-on-surface-variant">
        <li className="flex justify-between items-center">
          <span>Yaprak Temizliği</span>
          <span className="font-bold text-primary">Yarın</span>
        </li>
        <li className="flex justify-between items-center">
          <span>Saksı Değişimi</span>
          <span className="font-bold text-on-surface-variant opacity-60">
            2 ay sonra
          </span>
        </li>
      </ul>
    </div>
  )
}
