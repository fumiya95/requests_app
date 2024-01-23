# weather_app/views.py
from django.shortcuts import render
import requests
import pprint

def get_weather(request):
    num = "270000"
    params = {"city": num}
    response = requests.get("https://weather.tsukumijima.net/api/forecast", params=params)
    json_response = response.json()
    
    return render(request, 'weather_app/weather.html', {'weather_data': json_response})
