#!/usr/bin/env python

# 2018-07-02 DHT22.py

import time
import pigpio

DHTAUTO = 0
DHT11 = 1
DHTXX = 2

MAX_TIME = 0.05
MAX_COUNT = 100

OK = 0
ERROR_CHECKSUM = 1
ERROR_TIMEOUT = 2

class sensor:
    """
    A class to read relative humidity and temperature
    from the DHT11 or DHT22 sensor using the pigpio
    library.  No GPIO timing requirements.
    """

    def __init__(self, pi, gpio, model=DHTAUTO):
        """
        Instantiate with the Pi and the GPIO connected
        to the DHT22 output pin.
        """
        self.pi = pi
        self.gpio = gpio
        self.model = model
        self.cb = None

        self.humidity = 0
        self.temperature = 0

        self.bad_CS = 0
        self.bad_SM = 0
        self.bad_MM = 0
        self.bad_SR = 0

        self.no_response = 0
        self.bad_checksum = 0
        self.short_message = 0
        self.missing_message = 0

        pi.set_pull_up_down(gpio, pigpio.PUD_OFF)

    def read(self):
        """
        Reads relative humidity and temperature.
        Returns (status, humidity, temperature).
        """
        pi = self.pi
        gpio = self.gpio

        pi.write(gpio, pigpio.LOW)
        time.sleep(0.02)

        pi.set_mode(gpio, pigpio.INPUT)
        count = 0
        while pi.read(gpio) == 1:
            count += 1
            if count > MAX_COUNT:
                return ERROR_TIMEOUT, 0, 0

        pulse_len = []
        while len(pulse_len) < 82:
            high = time.time()
            while pi.read(gpio) == 0:
                pass
            pulse_len.append(time.time() - high)

        pulse_sum = 0
        for x in range(2, 42, 2):
            pulse_sum += pulse_len[x]

        bit_count = 0
        humidity = 0
        temperature = 0
        checksum = 0

        for x in range(2, 42, 2):
            if pulse_len[x] > (pulse_sum/20):
                bit_count += 1
                humidity |= (1 << 7-(bit_count % 8))
                if bit_count == 16:
                    bit_count = 0
                    temperature |= (1 << 7-(bit_count % 8))
                    checksum = (checksum + humidity + temperature) & 255
                    return OK, humidity, temperature

        return ERROR_CHECKSUM, 0, 0

if __name__ == "__main__":
    pi = pigpio.pi()

    s = sensor(pi, 4)

    for i in range(10):
        status, humidity, temperature = s.read()
        print(f"Humidity: {humidity} % | Temperature: {temperature} °C")

    s.cancel()
    pi.stop()
