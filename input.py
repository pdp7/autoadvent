#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_value = GPIO.input(23)
    if input_value == False:
        print "SHUTDOWN"
        os.system("sudo halt")
        sleep(1)
