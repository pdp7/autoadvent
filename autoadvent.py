#!/usr/bin/python

from datetime import date, timedelta, datetime
from time import sleep
import RPi.GPIO as GPIO
import sys

#from http://stackoverflow.com/questions/2003870/how-can-i-select-all-of-the-sundays-for-a-year-using-python
def allsundays(year):
   d = date(year, 11, 27)                    # January 1st
   d += timedelta(days = 6 - d.weekday())  # First Sunday
   while d.year == year:
      yield d
      d += timedelta(days = 7)

advent = []
now = sys.argv[1]
date_object = datetime.strptime(now, '%b %d %Y')
#today = date.today()
today = datetime.date(date_object)
print today
xmas=date(today.year,12,25)
print today.year
for d in allsundays(today.year):
   if d < xmas:
     advent.append(d)


candles = 0
for i in advent[-4:]:
   if today >= i and today <= xmas:
     print "{0} >= {1}".format(today,i)
     candles += 1

print "candles: %d" % candles

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pin = (17, 18, 27, 22)
for i in range(candles):
   print pin[i]
   GPIO.setup(pin[i], GPIO.OUT)
   GPIO.output(pin[i], GPIO.HIGH)

sleep(10)
GPIO.output(17, GPIO.LOW)

for i in range(candles):
   print pin[i]
   GPIO.output(pin[i], GPIO.LOW)

