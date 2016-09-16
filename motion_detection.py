#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

pir_sensor = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(pir_sensor, GPIO.IN)

fl = open('/home/pi/pir', 'w')

i = 0
current_state = 0
while i < 6:
    current_state = GPIO.input(pir_sensor)
    fl.write('%s' % (current_state))
    sleep(1)
    i += 1

GPIO.cleanup(18)
fl.close()
