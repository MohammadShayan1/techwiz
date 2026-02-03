# 🌤️ Weather Ninja - IoT Weather Monitoring System

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Poppins&weight=600&size=28&duration=3500&pause=500&color=151CF7&center=true&vCenter=true&width=435&lines=Weather+Ninja;IoT+Weather+Monitoring;Real-Time+Data+Visualization" alt="Typing SVG" />
</div>

---

## 📋 Project Overview

**Weather Ninja** is an IoT-based real-time weather monitoring system developed as part of **TechWiz 2024** by **Team Code Titans**. This project integrates hardware sensors with a modern web application to collect, process, and visualize environmental data including temperature and humidity readings.

The system uses a **Raspberry Pi** with a **DHT11 sensor** to collect real-time weather data and transmits it to a **Django-based web server** for storage and visualization.

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        WEATHER NINJA ARCHITECTURE                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   ┌──────────────────┐        ┌──────────────────┐        ┌───────────┐ │
│   │   Raspberry Pi    │  HTTP  │   Django Server   │  SQL   │  SQLite   │ │
│   │   + DHT11 Sensor  │ ─────► │   (Backend API)   │ ─────► │  Database │ │
│   │                   │  POST  │                   │        │           │ │
│   └──────────────────┘        └─────────┬──────────┘        └───────────┘ │
│                                         │                                 │
│                                         │ HTML/CSS/JS                     │
│                                         ▼                                 │
│                               ┌──────────────────┐                        │
│                               │   Web Dashboard   │                        │
│                               │   (Frontend UI)   │                        │
│                               │   - Charts        │                        │
│                               │   - Data Tables   │                        │
│                               └──────────────────┘                        │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Technology Stack

### Hardware
| Component | Purpose |
|-----------|---------|
| **Raspberry Pi** | Microcontroller for data collection and transmission |
| **DHT11 Sensor** | Temperature and humidity sensor (connected to GPIO 4) |

### Software & Frameworks
| Technology | Purpose |
|------------|---------|
| **Python** | Primary programming language |
| **Django** | Backend web framework |
| **Django REST Framework** | API handling |
| **SQLite** | Database for storing sensor data |
| **Bootstrap 4** | Frontend styling and responsive design |
| **Chart.js** | Interactive data visualization charts |
| **Adafruit_DHT Library** | DHT11 sensor communication library |

---

## 📁 Project Structure

```
techwiz/
├── README.md                          # Quick start guide
├── PROJECT_DOCUMENTATION.md           # Detailed documentation (this file)
├── sensor_script.py                   # Raspberry Pi sensor data collection script
├── IOT/
│   ├── Raspberry Pi Python Script.txt # Alternative sensor script
│   ├── weather/
│   │   └── templates/
│   │       ├── weather.html           # Frontend dashboard template
│   │       └── assets/
│   │           └── bg.jpg             # Background image
│   └── weather_monitor/               # Django project
│       ├── manage.py                  # Django management script
│       ├── db.sqlite3                 # SQLite database
│       ├── weather/                   # Django app
│       │   ├── models.py              # SensorData model
│       │   ├── views.py               # API and page views
│       │   ├── urls.py                # URL routing
│       │   ├── admin.py               # Admin configuration
│       │   └── migrations/            # Database migrations
│       └── weather_monitor/           # Django settings
│           ├── settings.py            # Project configuration
│           ├── urls.py                # Root URL configuration
│           ├── wsgi.py                # WSGI application
│           └── asgi.py                # ASGI application
```

---

## 🔄 How It Works

### 1. Data Collection (Raspberry Pi)
The Raspberry Pi runs a Python script (`sensor_script.py`) that:
- Reads temperature and humidity data from the DHT11 sensor connected to GPIO pin 4
- Processes the raw sensor data
- Sends the data to the Django server via HTTP POST request every 5 seconds

```python
# Key functionality from sensor_script.py
temperature = dhtDevice.temperature
humidity = dhtDevice.humidity
data = {'temperature': temperature, 'humidity': humidity}
response = requests.post(django_server_url, json=data)
```

### 2. Data Processing (Django Backend)
The Django backend:
- Receives sensor data via REST API endpoint (`/weather_data/`)
- Validates and stores the data in SQLite database
- Provides data retrieval for the frontend dashboard

**Data Model:**
```python
class SensorData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
```

### 3. Data Visualization (Web Dashboard)
The frontend dashboard:
- Displays real-time temperature and humidity readings
- Shows the last 5 sensor readings in a table format
- Visualizes data trends using interactive Chart.js line graphs
- Features a responsive Bootstrap design with weather-themed styling

---

## 🖥️ Features

### ✅ Real-Time Monitoring
- Live temperature readings in Celsius (°C)
- Live humidity readings in percentage (%)
- Automatic timestamp logging for each reading

### ✅ Data Visualization
- Interactive line charts showing temperature and humidity trends
- Responsive charts that adapt to screen size
- Color-coded data series for easy interpretation

### ✅ Data Management
- Persistent storage in SQLite database
- Admin dashboard for data management
- Historical data retrieval

### ✅ User Interface
- Modern, responsive Bootstrap design
- Weather-themed background and styling
- Clean tabular data presentation

---

## 🚀 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Display weather monitoring dashboard |
| `/weather_data/` | POST | Receive and store sensor data |
| `/admin/` | GET | Access Django admin dashboard |
| `/admin/login/` | GET/POST | Admin authentication |

### API Request Format
**POST** `/weather_data/`
```json
{
    "temperature": 25.5,
    "humidity": 60.0
}
```

### API Response Format
```json
{
    "status": "success",
    "message": "Data received and saved successfully"
}
```

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.x
- pip (Python package manager)
- Raspberry Pi with DHT11 sensor (for hardware setup)

### Backend Setup
```bash
# Navigate to project directory
cd IOT

# Install Django
pip install django

# Install Django REST Framework
pip install djangorestframework

# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Start the development server
python manage.py runserver 0.0.0.0:8000
```

### Raspberry Pi Setup
```bash
# Install required libraries
pip install adafruit-circuitpython-dht
pip install requests

# Run the sensor script
python sensor_script.py
```

---

## 🔐 Admin Access

> **Note:** For production deployments, create your own admin account using:
> ```bash
> python manage.py createsuperuser
> ```

**Default Development Credentials:**
| Field | Value |
|-------|-------|
| Username | `techwiz` |
| Email | `admin@codetitans.com` |
| Password | `abc@123456789` |

> ⚠️ These credentials are for development/demo purposes only. Always change default credentials in production.

---

## 👥 Team Code Titans

| Student ID | Name | Role |
|------------|------|------|
| Student1334497 | Amna Mustafa | Team Member |
| Student1413931 | Mohammad Shayan | Team Member |
| Student1413950 | Shahmeer Fareed | Team Member |

---

## 🎯 Key Learning Outcomes

This project demonstrates:
1. **IoT Integration** - Connecting physical hardware sensors to web applications
2. **Full-Stack Development** - Building both backend APIs and frontend interfaces
3. **Real-Time Data Processing** - Handling continuous data streams
4. **Data Visualization** - Creating interactive charts and dashboards
5. **REST API Design** - Implementing proper API endpoints and responses
6. **Database Management** - Storing and retrieving time-series data

---

## 📊 Use Cases

- **Smart Home Monitoring** - Track indoor temperature and humidity levels
- **Agricultural Applications** - Monitor greenhouse conditions
- **Industrial Monitoring** - Track environmental conditions in warehouses
- **Educational Projects** - Learn IoT and web development concepts

---

## 🔗 Related Links

- [Figma Prototype](https://www.figma.com/proto/eog5uf4qzKnbrPt2z2ymgT/ViroShield?type=design&node-id=1-2&t=H7V3aKDiBSrUN3Sm-1&scaling=scale-down&page-id=0%3A1&starting-point-node-id=1%3A2&mode=design)
- [GitHub Repository](https://github.com/MohammadShayan1/techwiz)

---

## 📝 License

This project was developed for TechWiz 2024 competition.

---

<div align="center">
  <p>Built with ❤️ by Team Code Titans for TechWiz 2024</p>
</div>
