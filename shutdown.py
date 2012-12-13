#!/usr/bin/python

from datetime import date, timedelta, datetime
from time import sleep
import RPi.GPIO as GPIO
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pin = (17, 18, 27, 22)
for i in pin:
   print i
   GPIO.setup(i, GPIO.OUT)
   GPIO.output(i, GPIO.LOW)

