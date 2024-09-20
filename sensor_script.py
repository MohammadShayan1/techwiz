import adafruit_dht
import board
import requests
import json
import time
import RPi.GPIO as GPIO
import adafruit_bmp280
import busio

# Set up DHT11 sensor on GPIO 4
dhtDevice = adafruit_dht.DHT11(board.D4)

# Set up rain sensor on GPIO 17
RAIN_SENSOR_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(RAIN_SENSOR_PIN, GPIO.IN)

# Set up BMP280 pressure sensor using I2C
i2c = busio.I2C(board.SCL, board.SDA)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

# Define the Django server URL (replace with your Django server IP)
django_server_url = "http://localhost:8000/weather_data/"

try:
    while True:
        try:
            # Read temperature and humidity from DHT11
            temperature = dhtDevice.temperature
            humidity = dhtDevice.humidity

            # Read rain sensor (digital input, 1 for dry, 0 for rain detected)
            rain_detected = GPIO.input(RAIN_SENSOR_PIN)

            # Read pressure from BMP280
            pressure = bmp280.pressure

            if temperature is not None and humidity is not None:
                print(f"Temp: {temperature:.1f}C  Humidity: {humidity}%")
                print(f"Pressure: {pressure:.2f} hPa")
                if rain_detected == 0:
                    print("Rain detected!")
                else:
                    print("No rain detected.")

                # Prepare data to send
                data = {
                    'temperature': temperature,
                    'humidity': humidity,
                    'pressure': pressure,
                    'rain_detected': rain_detected  # 0 for rain, 1 for no rain
                }

                # Send the data to Django server as a POST request
                response = requests.post(django_server_url, json=data)

                # Handle the response, even if it's not in JSON format
                try:
                    response_json = response.json()  # Attempt to parse JSON response
                    print(f"Server Response: {response.status_code} - {response_json}")
                except ValueError:  # If response is not JSON, print plain text response
                    print(f"Server Response: {response.status_code} - {response.text}")

            else:
                print("Failed to retrieve data from sensor")

        except RuntimeError as error:
            # Handle occasional read errors
            print(f"RuntimeError: {error.args[0]}")

        time.sleep(5)  # Wait before reading again

except KeyboardInterrupt:
    print("Script interrupted by user")
    GPIO.cleanup()  # Clean up GPIO pins when interrupted