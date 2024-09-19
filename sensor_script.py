import adafruit_dht
import board
import time

# Set up the DHT11 sensor on GPIO 4
dhtDevice = adafruit_dht.DHT11(board.D4)

try:
    while True:
        try:
            # Read temperature and humidity from DHT11
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity

            if temperature_c is not None and humidity is not None:
                print(f"Temp: {temperature_c:.1f}C  Humidity: {humidity}%")
            else:
                print("Failed to retrieve data from sensor")

        except RuntimeError as error:
            # Handle occasional read errors
            print(f"RuntimeError: {error.args[0]}")

        time.sleep(10)  # Read every 10 seconds

except KeyboardInterrupt:
    print("Script interrupted by user")