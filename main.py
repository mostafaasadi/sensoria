import Adafruit_DHT
from time import sleep
import RPi.GPIO as GPIO


def blink(pin):
    timeon = 0.2
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, True)
    sleep(timeon)
    GPIO.output(pin, False)
    sleep(timeon)


def main():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(dht, sensor_pin)

        if humidity is not None and temperature is not None:
            print("Temperature={}℃  Humidity={}%".format(temperature, humidity))

            if humidity > hum_cond:
                blink(high_hum_pin)
            else:
                blink(down_hum_pin)
            if temperature > temp_cond:
                blink(high_temp_pin)
            else:
                blink(down_temp_pin)

        else:
            print("Failed to retrieve data from sensor")


if __name__ == '__main__':
    # init sesor and pins
    dht = Adafruit_DHT.DHT11

    # set pins
    sensor_pin = 14
    high_temp_pin = 18
    down_temp_pin = 15
    high_hum_pin = 24
    down_hum_pin = 23

    # set conditions
    temp_cond = 29
    hum_cond = 39
    main()
