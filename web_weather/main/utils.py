import requests
from django.conf import settings


def get_weather(city):
    WEATHER_API_KEY = settings.SECRET_API_KEY
    url_current = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}&lang=ru"

    response_current = requests.get(url_current)

    if response_current.status_code == 200:
        data_current = response_current.json()
        temp_c = data_current['current']['temp_c']
        return temp_c
