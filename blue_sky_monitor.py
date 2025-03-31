import requests 
import json
from urllib.parse import quote
from colorama import Fore, Style, init
import pandas as pd
from datetime import datetime
import os

# Initialize colorama
init()

# Replace with your API key
API_KEY = "YOUR API KEY"

# File to store city logs
CITY_LOG_FILE = "city_log.csv"
WEATHER_DATA_FILE = "weather_data.csv"

def log_city(city):
    """Log the city and timestamp to a CSV file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = {"City": city, "Timestamp": timestamp}
    
    # Check if the file exists
    file_exists = os.path.isfile(CITY_LOG_FILE)
    
    # Append the log entry to the CSV file
    df = pd.DataFrame([log_entry])
    df.to_csv(CITY_LOG_FILE, mode='a', header=not file_exists, index=False)
    print(f"{Fore.GREEN}City '{city}' logged with timestamp {timestamp}.{Style.RESET_ALL}")

# Prompt the user to enter the city name
CITY = input("Enter the city name: ").strip()

# Log the city
log_city(CITY)

# Weather API 7-day forecast API URL
encoded_city = quote(CITY)
URL = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={encoded_city}&days=7&aqi=yes&alerts=yes"

def fetch_weather_data(url):
    """Fetch weather data from the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"{Fore.RED}HTTP error occurred: {http_err}{Style.RESET_ALL}")
    except Exception as err:
        print(f"{Fore.RED}Other error occurred: {err}{Style.RESET_ALL}")
    return None

def display_weather_data(data):
    """Display the 7-day weather forecast in the terminal in a formatted column layout with colors."""
    if "forecast" in data:
        print(f"\n{Fore.CYAN}{'='*50}\n  7-Day Weather Forecast for {CITY}\n{'='*50}{Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}{'Date':<12}{'Condition':<20}{'Avg Temp (°C)':<15}{'Max Temp (°C)':<15}{'Min Temp (°C)':<15}{'Humidity (%)':<15}{'Wind Speed (km/h)':<20}{'Sunrise':<12}{'Sunset':<12}{Style.RESET_ALL}")
        print("-"*140)
        for forecast in data["forecast"]["forecastday"]:
            date = forecast["date"]
            condition = forecast["day"]["condition"]["text"]
            avg_temp = forecast["day"]["avgtemp_c"]
            max_temp = forecast["day"]["maxtemp_c"]
            min_temp = forecast["day"]["mintemp_c"]
            humidity = forecast["day"]["avghumidity"]
            wind_speed = forecast["day"]["maxwind_kph"]
            sunrise = forecast["astro"]["sunrise"]
            sunset = forecast["astro"]["sunset"]
            
            print(f"{Fore.GREEN}{date:<12}{condition:<20}{avg_temp:<15}{max_temp:<15}{min_temp:<15}{humidity:<15}{wind_speed:<20}{sunrise:<12}{sunset:<12}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Error: 'forecast' key not found in the response data.{Style.RESET_ALL}")

def save_weather_data(data, city):
    """Save the 7-day weather forecast to a CSV file."""
    if "forecast" in data:
        rows = []
        for forecast in data["forecast"]["forecastday"]:
            date = forecast["date"]
            day = forecast["day"]
            temp = day["avgtemp_c"]
            max_temp = day["maxtemp_c"]
            min_temp = day["mintemp_c"]
            condition = day["condition"]["text"]
            humidity = day["avghumidity"]
            wind_speed = day["maxwind_kph"]
            pressure = forecast["hour"][0]["pressure_mb"]  # First hour's pressure (approximation)
            precipitation = day["totalprecip_mm"]
            uv_index = day["uv"]
            visibility = day["avgvis_km"]
            sunrise = forecast["astro"]["sunrise"]
            sunset = forecast["astro"]["sunset"]
            dew_point = forecast["hour"][0]["dewpoint_c"]  # First hour's dew point (approximation)

            rows.append({
                "City": city,
                "Date": date,
                "Condition": condition,
                "Avg Temp (°C)": temp,
                "Max Temp (°C)": max_temp,
                "Min Temp (°C)": min_temp,
                "Humidity (%)": humidity,
                "Wind Speed (km/h)": wind_speed,
                "Pressure (hPa)": pressure,
                "Precipitation (mm)": precipitation,
                "UV Index": uv_index,
                "Visibility (km)": visibility,
                "Sunrise": sunrise,
                "Sunset": sunset,
                "Dew Point (°C)": dew_point
            })
        
        # Check if the file exists
        file_exists = os.path.isfile(WEATHER_DATA_FILE)
        
        # Load existing data if the file exists
        if file_exists:
            existing_data = pd.read_csv(WEATHER_DATA_FILE)
        else:
            existing_data = pd.DataFrame()

        # Create a DataFrame for the new data
        new_data = pd.DataFrame(rows)

        # Combine and remove duplicates
        combined_data = pd.concat([existing_data, new_data]).drop_duplicates(subset=["City", "Date"], keep="last")
        
        # Save the combined data back to the CSV file
        combined_data.to_csv(WEATHER_DATA_FILE, index=False)
        print(f"{Fore.GREEN}Weather data updated in {WEATHER_DATA_FILE}{Style.RESET_ALL}")

def main():
    """Main function to fetch, display, and save the weather forecast."""
    data = fetch_weather_data(URL)
    if data:
        display_weather_data(data)
        save_weather_data(data, CITY)

if __name__ == "__main__":
    main()
