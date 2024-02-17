import requests
import pandas as pd

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
API_KEY = '**************************'
CITY = 'Denver'


BASE_URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&units=metric&appid={API_KEY}'

def fetch_weather_data():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        data = response.json()

        # Extract relevant information from the API response
        weather_info = {
            'City': data['name'],
            'Temperature (Celsius)': data['main']['temp'],
            'Humidity (%)': data['main']['humidity'],
            'Weather Description': data['weather'][0]['description'],
        }

        return weather_info

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def main():
    # Fetch weather data
    weather_data = fetch_weather_data()

    if weather_data:
        # Convert data to a DataFrame
        df = pd.DataFrame([weather_data])

        # Save data to a CSV file
        df.to_csv('weather.csv', index=False)
        print("Weather data saved successfully.")

if __name__ == "__main__":
    main()