import ThirstyPlants from './ThirstyPlants.jsx'
import WeeklyTip from './WeeklyTip.jsx'
import PlantProfile from './PlantProfile.jsx'
import HealthStatus from './HealthStatus.jsx'
import UpcomingTasks from './UpcomingTasks.jsx'
import WeatherWidget from './WeatherWidget.jsx'

export default function Dashboard() {
  return (
    <main className="pl-72 pt-20 pb-16 min-h-screen">
      <div className="p-8 flex flex-col gap-8">
        {/* Weather Widget - Full Width */}
        <WeatherWidget />

        <div className="grid grid-cols-12 gap-8">
          {/* Left Column: Thirsty Today */}
          <section className="col-span-12 lg:col-span-4 flex flex-col gap-6">
            <ThirstyPlants />
            <WeeklyTip />
          </section>
          
          {/* Right Column: Plant Detail Profile */}
          <section className="col-span-12 lg:col-span-8">
            <PlantProfile />
            
            {/* Secondary Info Section */}
            <div className="mt-8 grid grid-cols-1 md:grid-cols-2 gap-8">
              <HealthStatus />
              <UpcomingTasks />
            </div>
          </section>
        </div>
      </div>
    </main>
  )
}
