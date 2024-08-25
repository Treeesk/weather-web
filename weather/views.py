from django.shortcuts import render
import requests
import json


def index(request):
    if request.method == 'POST':
        API_KEY = 'ccde5c714b10e7862cb2c4bc180fb3c8'
        city_name = request.POST.get('city')
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric&lang=ru"
        response = requests.get(url).json()
        city_weather_updated = {
            'city': city_name,
            'country': response['sys']['country'],
            'description': response['weather'][0]['description'],
            'temperature': 'Температура:' + str(response['main']['temp']) + '°C',
            'wind': 'Ветер:' + str(response['wind']['speed']) + ' км/ч',
        }
    else:
        city_weather_updated = {}
    context = {'city_weather_updated': city_weather_updated}
    return render(request,'weather.html', context)
