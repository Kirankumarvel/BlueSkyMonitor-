
# 🌦️ BlueSkyMonitor

BlueSkyMonitor is a Python-based weather monitoring tool that fetches a 7-day forecast using the WeatherAPI and presents data in a structured, color-coded format in the terminal.

## 🚀 Features

- Fetches real-time weather data for any city.
- Displays the forecast in a formatted table with color highlights.
- Logs city queries and stores historical weather data in CSV files.
- Saves forecast data for future reference.

## 📁 Project Structure

```
BlueSkyMonitor/
├── blue_sky_monitor.py  # Main weather script
├── requirements.txt     # List of dependencies
├── config.py            # API key storage (ignored by Git)
├── README.md            # Project documentation
├── .gitignore           # Ignore unnecessary files
├── data/
│   ├── city_log.csv      # Logged city queries
│   ├── weather_data.csv  # Stored weather data
```

## 🔧 Installation

1️⃣ Clone the Repository

```bash
git clone https://github.com/Kirankumarvel/BlueSkyMonitor-.git
cd BlueSkyMonitor
```

2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate    # Windows
```

3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

4️⃣ Add API Key

Create a `config.py` file and add your WeatherAPI key:

```python
API_KEY = "your_api_key_here"
```

## 🏃‍♂️ Usage

Run the script and enter a city name:

```bash
python blue_sky_monitor.py
```

## 📊 Output Format

The script displays the 7-day forecast in a structured table:

```
==================================================================================
  7-Day Weather Forecast for New York
==================================================================================
Date        Condition           Avg Temp (°C)  Max Temp (°C)  Min Temp (°C)  Humidity (%)   Wind Speed (km/h)   Sunrise     Sunset   
----------------------------------------------------------------------------------
2025-04-01  Partly Cloudy       22             25             18             65            15                 06:30 AM    07:45 PM
...
```

## 📝 Logging & Data Storage

- **City Queries** → Stored in `data/city_log.csv`
- **Weather Forecast Data** → Stored in `data/weather_data.csv`

## 🧪 Running Tests

To run unit tests:

```bash
pytest tests/test_weather.py
```

## 📜 License

This project is licensed under the MIT License.

## 🌍 Contributing

Feel free to submit issues or pull requests to enhance BlueSkyMonitor!

⭐ Star this repo if you like it! 😊
