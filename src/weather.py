import requests
import os
from dotenv import load_dotenv

# Class to handle weather API calls and weather formatting
class Weather:
    def weather_api_call():
        load_dotenv()
        WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
        zip_code = 14201
        response = requests.get(f"https://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={zip_code}").json()

        # Get the temperature and convert to int to remove decimals, then to a string to add "degree" F
        weather_temp = str(int(response['current']['temp_f'])) + "\u00B0F"

        # Get the path to icon and format to the file structure
        full_icon_path = response['current']['condition']['icon']
        icon_path = "static/" + full_icon_path.split('com/')[1]
       
        return icon_path, weather_temp
