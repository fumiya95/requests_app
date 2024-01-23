from django.shortcuts import render
from django.http import HttpResponse
import requests
from .weather_api import get_weather

def index(request):
    url = "https://weather.tsukumijima.net/api/forecast/city/"
    city = "270000"

    r = requests.get(url+city)
    
    # Check if the request was successful (status code 200)
    if r.status_code == 200:
        data = r.json()
        city_weather = {
            'title': data['title'],
           'city_weather': data['']
        }
        context = {'city_weather': city_weather}  
        return render(request, 'request/index.html', context)
    else:
       
        return HttpResponse(f"エラー: {r.status_code}")
