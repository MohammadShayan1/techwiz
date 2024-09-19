from django.http import JsonResponse
from .models import SensorData
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from .models import SensorData

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
    weather_data = SensorData.objects.all().order_by('-timestamp')
    return render(request, 'weather.html', {'weather_data': weather_data})
