#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

PIR = 18 # pir pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_sensor, GPIO.IN)

with open('/home/pi/pir', 'w') as f:
    i = 0
    while i < 6:
        state = GPIO.input(PIR)
        f.write(state)
        sleep(1)
        i += 1

GPIO.cleanup(PIR)
