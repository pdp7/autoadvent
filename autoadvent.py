#!/usr/bin/python

from datetime import date, timedelta, datetime
from time import sleep
import RPi.GPIO as GPIO
import sys
import argparse

class AutoAdvent():

    def __init__(self, today=None, debug=False):
        self.debug = debug
        if self.debug == True:
            print "today: {0}".format(today)
        if(today == None):
            self.today = date.today()
        else:
            date_object = datetime.strptime(today, '%b %d %Y')
            self.today = datetime.date(date_object)
        if self.debug == True:
            print "self.today: {0}".format(self.today)

    #from http://stackoverflow.com/questions/2003870/how-can-i-select-all-of-the-sundays-for-a-year-using-python
    def allsundays(self, year):
       # start with Nov-27 which is the first possible day of Advent
       d = date(year, 11, 27)
       # find the next Sunday after the above date
       d += timedelta(days = 6 - d.weekday()) 
       while d.year == year:
          yield d
          d += timedelta(days = 7)

    def run(self):
        advent = []
        xmas=date(self.today.year,12,25)
        for d in self.allsundays(self.today.year):
            if d < xmas:
                advent.append(d)
    
        candles = 0
        for i in advent[-4:]:
            if self.today >= i and self.today < xmas:
                if self.debug == True:
                    print "{0} >= {1}".format(self.today,i)
                candles += 1
    
        if self.debug == True:
            print "candles: %d" % candles

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        #Pin configuration for Rev 1.0 Pi
        pin = (17, 18, 21, 22)
        #NOTE: if you have a Rev 2.0 Pi, then comment the above line and uncomment the following line
        #pin = (17, 18, 27, 22)
        for i in range(candles):
            if self.debug == True:
                print "Turning on pin: {0}".format(pin[i])
            GPIO.setup(pin[i], GPIO.OUT)
            GPIO.output(pin[i], GPIO.HIGH)

        #Push button is connected to GPIO #23 with internal pull-up resistor on
        GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        while True:
            input_value = GPIO.input(23)
            if input_value == False:
                if self.debug == True:
                    print "SHUTDOWN"
                os.system("sudo halt")
                sleep(1)


# following is executed when this script is run from the shell
if __name__ == '__main__':
    # parse arguments from the command line for the hashtag and LCD properties
    parser = argparse.ArgumentParser(description='Raspberry Pi controlled LED Advent candles')
    parser.add_argument('-v', '--verbose', action='store_true', default=False, help="print debug messages to shell")
    parser.add_argument('-t', '--today', help="specify a date for testing purposes, format: 'MMM DD YYYY'")
    args = parser.parse_args()
    autoAdvent = AutoAdvent(today=args.today, debug=args.verbose)
    autoAdvent.run()


