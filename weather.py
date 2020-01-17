import os, requests
from pathlib import Path
from dotenv import load_dotenv
from utils import print_center

# .env reader
env_file = '.env'
env_path = Path('/Users/fastory/dashboardPython') / env_file
load_dotenv(dotenv_path=env_path)

# Colors
light_green = "\033[92m"
yellow = "\033[33m"
bold = "\033[1m"
blue = '\033[34m'
red = '\033[31m'
eoc = "\033[0m"

# OpenWeatherMap
open_weather_map_api_key = os.getenv('OPEN_WEATHER_MAP_API_KEY')
open_weather_map_version = os.getenv('OPEN_WEATHER_MAP_VERSION') or '2.5'
city_name = os.getenv('OPEN_WEATHER_MAP_CITY') or 'Montreuil'
country_code = os.getenv('OPEN_WEATHER_MAP_COUNTRY_CODE') or 'fr'
base_url = "http://api.openweathermap.org/data/" + open_weather_map_version + "/weather?"
location = city_name + "," + country_code
units = "metric"
complete_url = base_url + "appid=" + open_weather_map_api_key + "&q=" + location + "&units=" + units

def get_weather():
  res = requests.get(complete_url).json()
  if res['cod'] == 200:
    main = res['main']
    weather = res['weather'][0]
    temp = str(main['temp']) + 'ºC'
    temp_max = main['temp_max']
    temp_min = main['temp_min']
    max_min = str(temp_min) + ' / ' + str(temp_max)
    description = weather['description']
    location_name = 'Weather at ' + bold + city_name + eoc
    return temp, max_min, description, location_name
  elif res['cod'] == '404':
    print('City not found');
    exit()
  else:
    print('An error occured')
    exit()

def print_weather():
  temp, max_min, description, location_name = get_weather()
  print(blue)
  print_center(location_name, 16)
  print(blue)
  print_center(temp)
  print_center(max_min)
  print_center(description)
