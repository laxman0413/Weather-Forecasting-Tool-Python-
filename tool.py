import os
import requests
from dotenv import load_dotenv

#My api Key
API_KEY="ec4c43397d0f3f5dbe726afa7dc718cc"

#fetching data from api
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data.")
        return None

#displaying the weather
def display_weather(weather_data):
    if weather_data is None:
        return
    weather_main = weather_data.get("weather", [{}])[0].get("main")
    weather_description = weather_data.get("weather", [{}])[0].get("description")
    temperature = weather_data.get("main", {}).get("temp")
    humidity = weather_data.get("main", {}).get("humidity")
    wind_speed = weather_data.get("wind", {}).get("speed")
    print("Weather forecast:")
    print(f"Main: {weather_main}")
    print(f"Description: {weather_description}")
    print(f"Temperature: {temperature} K")
    print(f"Humidity: {humidity} %")
    print(f"Wind Speed: {wind_speed} m/s")

if __name__ == "__main__":
    city = input("Enter the name of a city: ")
    weather_data = get_weather(city)
    try:
        weather_data = get_weather(city)
        if weather_data is None:
            print("Failed to fetch weather data.")
        else:
            display_weather(weather_data)
    except requests.exceptions.RequestException as e:
        print("An error occurred while making the API request:", str(e))
