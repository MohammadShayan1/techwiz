from django.http import JsonResponse
from .models import WeatherData
from django.shortcuts import render

def record_weather_data(request):
    if request.method == 'POST':
        temperature = request.POST.get('temperature')
        humidity = request.POST.get('humidity')
        if temperature and humidity:
            weather = WeatherData(temperature=temperature, humidity=humidity)
            weather.save()
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'}, status=400)

def display_weather_data(request):
    weather_data = WeatherData.objects.all().order_by('-timestamp')
    return render(request, 'weather.html', {'weather_data': weather_data})
