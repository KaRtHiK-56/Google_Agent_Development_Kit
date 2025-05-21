import requests
from dotenv import load_dotenv
import os
from typing import Dict

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")
print("api_key",api_key)

async def weather_teller(city: str) -> Dict[str, str]:
    complete_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        temperature = round(data['main']['temp'] - 273.15, 2)
        place = data["name"]
        weather_desc = data['weather'][0]['main']
        return {
            "temperature": f"{temperature}°C",
            "place": place,
            "weather": weather_desc
        }
    else:
        return {
            "temperature": "N/A",
            "place": city,
            "weather": f"Error: {response.status_code}"
        }



