import unittest
import json
from blue_sky_monitor import fetch_weather_data, save_weather_data

class TestBlueSkyMonitor(unittest.TestCase):
    
    def setUp(self):
        """Set up a sample API response for testing."""
        self.sample_data = {
            "forecast": {
                "forecastday": [
                    {
                        "date": "2025-04-01",
                        "day": {
                            "avgtemp_c": 22,
                            "maxtemp_c": 25,
                            "mintemp_c": 18,
                            "condition": {"text": "Partly Cloudy"},
                            "avghumidity": 65,
                            "maxwind_kph": 15,
                            "totalprecip_mm": 1.2,
                            "uv": 5,
                            "avgvis_km": 10
                        },
                        "astro": {
                            "sunrise": "06:30 AM",
                            "sunset": "07:45 PM"
                        },
                        "hour": [{"pressure_mb": 1015, "dewpoint_c": 12}]
                    }
                ]
            }
        }
    
    def test_fetch_weather_data(self):
        """Test API data fetching (mocked)."""
        url = "http://mock-api.com/weather"
        response = fetch_weather_data(url)  # In actual tests, mock requests.get
        self.assertIsInstance(response, dict)

    def test_save_weather_data(self):
        """Test saving API data to CSV."""
        city = "New York"
        save_weather_data(self.sample_data, city)
        with open("data/weather_data.csv", "r") as file:
            content = file.read()
        self.assertIn("New York", content)
        self.assertIn("2025-04-01", content)

if __name__ == "__main__":
    unittest.main()
