"""
Your first API call
------------------------------------------------------------------------------------------
Let's get real weather data using a free weather API:
"""

import requests

# We need coordinates to get weather data
latitude = 12.97 # bng latitude | 48.85   # Paris latitude
longitude = 77.59 # bng latitude |  2.35  # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data) # it prints a big dictionary with all the weather info for that location

type(data) # it prints <class 'dict'>, which means we can work with it like a normal Python dictionary

data.keys() # it prints dict_keys(['latitude', 'longitude', 'timezone', 'elevation', 'current_units', 'current']), which shows us the main sections of the data we got back

data["current"] # it prints {'time': '2025-08-01T08:30', 'temperature_2m': 20.0}, which is the current weather info we asked for

data['current']['temperature_2m']
"""
First install requests: pip install requests
"""