import React, { useState } from 'react'

const MOCK_TASKS = {
  today: [
    { id: 1, type: 'water', plant: 'Barış Çiçeği', time: 'Sabah (09:00)', completed: false, icon: 'water_drop', color: 'text-[#42a5f5]' },
    { id: 2, type: 'fertilize', plant: 'Deve Tabanı', time: 'Öğle (13:00)', completed: false, icon: 'compost', color: 'text-[#8d6e63]' }
  ],
  tomorrow: [
    { id: 3, type: 'repot', plant: 'Aloe Vera', time: 'Tüm Gün', completed: false, icon: 'potted_plant', color: 'text-primary' }
  ],
  thisWeek: [
    { id: 4, type: 'clean', plant: 'Paşa Kılıcı', time: 'Çarşamba', completed: false, icon: 'cleaning_services', color: 'text-[#ab47bc]' },
    { id: 5, type: 'water', plant: 'Kurdele Çiçeği', time: 'Cuma', completed: false, icon: 'water_drop', color: 'text-[#42a5f5]' }
  ]
}

const WEEK_DAYS = [
  { day: 'Pzt', date: '12', active: false },
  { day: 'Sal', date: '13', active: false },
  { day: 'Çar', date: '14', active: false },
  { day: 'Per', date: '15', active: false },
  { day: 'Cum', date: '16', active: true }, // Today
  { day: 'Cmt', date: '17', active: false },
  { day: 'Paz', date: '18', active: false },
]

export default function Calendar() {
  const [tasks, setTasks] = useState(MOCK_TASKS);

  const toggleTask = (group, id) => {
    setTasks(prev => ({
      ...prev,
      [group]: prev[group].map(task => 
        task.id === id ? { ...task, completed: !task.completed } : task
      )
    }));
  }

  const renderTaskGroup = (title, groupKey, items) => {
    if (items.length === 0) return null;
    
    return (
      <div className="mb-10">
        <h3 className="text-xl font-bold text-on-surface mb-6 flex items-center gap-2">
          {title}
          <span className="bg-surface-container-high text-on-surface-variant text-xs px-3 py-1 rounded-full">
            {items.filter(i => !i.completed).length} görev
          </span>
        </h3>
        <div className="flex flex-col gap-4">
          {items.map(task => (
            <div 
              key={task.id} 
              className={`flex items-center gap-6 p-5 rounded-[1.5rem] border transition-all duration-300 ${
                task.completed 
                  ? 'bg-surface-container/50 border-transparent opacity-60' 
                  : 'bg-surface-container-lowest/80 backdrop-blur-xl border-outline-variant/10 shadow-sm hover:shadow-md hover:-translate-y-1'
              }`}
            >
              {/* Checkbox */}
              <button 
                onClick={() => toggleTask(groupKey, task.id)}
                className={`w-8 h-8 rounded-full border-2 flex items-center justify-center shrink-0 transition-all ${
                  task.completed 
                    ? 'bg-primary border-primary text-on-primary' 
                    : 'border-outline-variant text-transparent hover:border-primary'
                }`}
              >
                <span className="material-symbols-outlined text-[18px]">check</span>
              </button>

              {/* Icon */}
              <div className={`w-12 h-12 rounded-2xl flex items-center justify-center shrink-0 ${
                task.completed ? 'bg-surface-container-high text-on-surface-variant' : `bg-surface-container-high ${task.color}`
              }`}>
                <span className="material-symbols-outlined">{task.icon}</span>
              </div>

              {/* Content */}
              <div className="flex-1">
                <h4 className={`text-lg font-bold ${task.completed ? 'text-on-surface-variant line-through' : 'text-on-surface'}`}>
                  {task.plant}
                </h4>
                <p className="text-sm font-medium text-on-surface-variant flex items-center gap-1">
                  <span className="material-symbols-outlined text-[14px]">schedule</span>
                  {task.time}
                  <span className="mx-2 opacity-30">•</span>
                  {task.type === 'water' && 'Sulama'}
                  {task.type === 'fertilize' && 'Gübreleme'}
                  {task.type === 'repot' && 'Saksı Değişimi'}
                  {task.type === 'clean' && 'Yaprak Temizliği'}
                </p>
              </div>

            </div>
          ))}
        </div>
      </div>
    );
  }

  return (
    <main className="pl-72 pt-20 pb-16 min-h-screen font-body">
      <div className="p-8 max-w-4xl mx-auto flex flex-col gap-8">
        
        {/* Header */}
        <div>
          <h2 className="text-3xl font-extrabold text-primary tracking-tight mb-2">Bakım Takvimi</h2>
          <p className="text-on-surface-variant">Bitkilerinizin mutlu ve sağlıklı kalması için yaklaşan görevler.</p>
        </div>

        {/* Weekly Timeline Overview */}
        <div className="bg-surface-container-lowest/80 backdrop-blur-xl p-6 rounded-[2rem] border border-outline-variant/10 shadow-sm flex justify-between items-center overflow-x-auto gap-4 hide-scrollbar">
          {WEEK_DAYS.map((day, idx) => (
            <div 
              key={idx} 
              className={`flex flex-col items-center justify-center min-w-[4rem] h-20 rounded-2xl transition-all cursor-pointer ${
                day.active 
                  ? 'bg-primary text-on-primary shadow-md scale-105' 
                  : 'hover:bg-surface-container-high text-on-surface-variant'
              }`}
            >
              <span className={`text-xs font-bold uppercase tracking-widest ${day.active ? 'opacity-80' : 'opacity-60'}`}>
                {day.day}
              </span>
              <span className="text-2xl font-extrabold mt-1">{day.date}</span>
            </div>
          ))}
        </div>

        {/* Task Lists */}
        <div className="mt-4">
          {renderTaskGroup("Bugün", "today", tasks.today)}
          {renderTaskGroup("Yarın", "tomorrow", tasks.tomorrow)}
          {renderTaskGroup("Bu Hafta", "thisWeek", tasks.thisWeek)}

          {tasks.today.length === 0 && tasks.tomorrow.length === 0 && tasks.thisWeek.length === 0 && (
            <div className="py-16 text-center bg-surface-container-lowest/50 rounded-[2rem] border border-outline-variant/10">
              <span className="material-symbols-outlined text-6xl text-on-surface-variant opacity-20 mb-4">celebration</span>
              <p className="text-xl font-bold text-on-surface-variant">Tüm görevler tamamlandı!</p>
              <p className="text-sm text-on-surface-variant opacity-70 mt-2">Bitkileriniz güvende ve mutlu.</p>
            </div>
          )}
        </div>

      </div>
    </main>
  )
}
