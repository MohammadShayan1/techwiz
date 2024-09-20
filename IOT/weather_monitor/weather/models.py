from django.db import models

class SensorData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()  # Ensure this is FloatField without any incorrect default
    rain_detected = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Temp: {self.temperature}, Humidity: {self.humidity}, Pressure: {self.pressure}, Rain: {self.rain_detected} at {self.timestamp}"