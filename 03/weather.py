import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")


def convert_temperature(kelvin, unit):
    if unit == "celsius":
        return round(kelvin - 273.15, 2)
    elif unit == "fahrenheit":
        return round((kelvin - 273.15) * 9 / 5 + 32, 2)

def get_current_weather(loc, unit="celsius"):

    location = loc.split(",")[0]
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        current_temp = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]

        weather_info = {
            "location": location,
            "temperature": convert_temperature(current_temp, unit),
            "unit": unit,
            "forecast": description,
        }

        # make sure to convert to stringified json object
        return json.dumps(weather_info)

    except requests.HTTPError as err:
        print(f"HTTP Fehler: {err}")
        return

# location = "Berlin, Germany"
# weather_result = get_current_weather(location)
# print(weather_result)