# 🌿 Smart Plant Maintenance Assistant

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![SQL Server](https://img.shields.io/badge/SQL_Server-CC2927?style=for-the-badge&logo=microsoft-sql-server&logoColor=white)

The Smart Plant Maintenance Assistant is an intelligent web application designed to automate your indoor and outdoor plant care routines, monitor local weather, and diagnose plant diseases using symptom-based algorithms.

## ✨ Core Features

*   **Smart Calendar:** Automatically calculates watering, fertilizing, and cleaning schedules based on plant species using a custom local database.
*   **Weather-Aware Integration:** Fetches real-time weather data via API. If rain is expected, the system automatically skips watering reminders for outdoor plants (balcony/garden).
*   **Algorithmic Disease Diagnosis:** Analyzes leaf condition, soil moisture, and environmental factors through custom logic to identify plant issues (e.g., root rot, fungal infections, pests) and suggests treatments. It dynamically reduces the plant's health score based on the severity of the symptoms.
*   **Advanced Statistics:** Calculates your garden's overall health status, care delays, and your personal "Gardening Score".
*   **Bilingual Support:** Full support for both English and Turkish interfaces.

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Frontend** | Python (Streamlit) |
| **Backend** | Python |
| **Database** | Microsoft SQL Server (pyodbc) |
| **Weather API** | OpenWeatherMap API |
| **Plant Data Module** | Custom Local Service (`perenual_service.py`) |

## 👥 Development Team & Roles

*   **Ali Türk (Master / Team Lead):** System integration, bug-fixing, and Full-Stack development of the algorithmic Sick Plant Diagnosis system.
*   **Fikriye:** UI/UX design. Streamlit frontend coding for the Dashboard, Library, Calendar, and Statistics pages.
*   **Hüseyin:** Database (SQL Server) architecture, `database_handler.py` setup, and CRUD operations.
*   **Ünal:** OpenWeather API integration (`weather_service.py`), and backend algorithms for the Calendar and Dashboard pages.
*   **Rasim:** Statistics and Plant Library backend architecture, data processing, and custom plant data module management.

## 🔌 Data Services & APIs

### 1. OpenWeatherMap API (`weather_service.py`)
*   **Endpoint:** `http://api.openweathermap.org/data/2.5/weather`
*   **Parameters:** `q={city_name}`, `units=metric`, `lang=en/tr`
*   **Purpose:** Fetches real-time temperature, humidity, and weather codes. If rain codes (2xx, 3xx, 5xx) are detected, `yagmur_var_mi = True` is returned, and outdoor watering tasks are skipped.

### 2. Local Plant Data Module (`perenual_service.py`)
*   **Purpose:** Instead of relying on external plant APIs, the system utilizes a robust, hardcoded local data dictionary. When a new plant is added, this module provides the ideal watering frequency (in days) and light requirements based on the plant's species, ensuring fast and reliable offline data access.

## 🚀 Installation & Setup

1. Clone the repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install streamlit pyodbc pandas requests
