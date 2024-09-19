import adafruit_dht
import board
import requests
import json
import time

# Set up DHT11 sensor on GPIO 4
dhtDevice = adafruit_dht.DHT11(board.D4)

# Define the Django server URL (replace with your Django server IP)
django_server_url = "http://localhost:8000/weather_data/"

try:
    while True:
        try:
            # Read temperature and humidity from DHT11
            temperature = dhtDevice.temperature
            humidity = dhtDevice.humidity

            if temperature is not None and humidity is not None:
                print(f"Temp: {temperature:.1f}C  Humidity: {humidity}%")

                # Send the data to Django server as a POST request
                data = {'temperature': temperature, 'humidity': humidity}
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