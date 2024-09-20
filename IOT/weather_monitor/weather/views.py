from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import SensorData
import json

@csrf_exempt
def receive_sensor_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            temperature = data.get('temperature')
            humidity = data.get('humidity')

            # Save the sensor data to the database
            SensorData.objects.create(temperature=temperature, humidity=humidity)

            return JsonResponse({'status': 'success', 'message': 'Data received and saved successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def display_weather_data(request):
    # Fetch the last 5 entries ordered by the most recent timestamp
    weather_data = SensorData.objects.all().order_by('-timestamp')[:5]
    return render(request, 'weather.html', {'weather_data': weather_data})
