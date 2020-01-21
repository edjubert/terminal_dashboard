# Terminal Dashboard

## Setup
### .env
The dashboard uses **open weather map** to provide weather forcast.
You can create an API_KEY on [openweathermap.com](https://openweathermap.org/api_keys)
It also uses **Github** token to provide your notifications, you can create yours [here](https://github.com/settings/tokens)

You will not be able to use `weather.py` nor `dashboard.py` without **OPEN_WEATHER_MAP_API_KEY**
You will not be able to use `github.py` nor `dashboard.py` without **GITHUB_TOKEN**

The default **OPEN_WEATHER_MAP_VERSION** is set to `2.5`

You need to create a `.env` file and format it as follow
```.env
OPEN_WEATHER_MAP_API_KEY=<OWM_API_KEY>
OPEN_WEATHER_MAP_VERSION=<OPEN_WEATHER_MAP_VERSION>
OPEN_WEATHER_MAP_CITY=<CITY_NAME>
OPEN_WEATHER_MAP_COUNTRY_CODE=<COUNTRY_CODE>
GITHUB_USERNAME=<GITHUB_USERNAME>
GITHUB_TOKEN=<GITHUB_TOKEN>
```

## Install and run
The dashboard uses `Pillow`, `requests` and `python-dotenv` packages.
To install these packages, you need to run first:
```python
pip3 -r requirements.txt
```

Once all packages are installed, you can run the dashboard as follow:
```python
cd <PATH_TO_THE_DASHBOARD>
python3 dashboard.py
```

You can also run each part independently.
For example, to run the clock:
```python
python3 clock.py
```

## Author
[@edjubert](https://github.com/settings/tokens)