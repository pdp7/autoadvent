#!/usr/bin/python

from datetime import date, timedelta, datetime
from time import sleep
import RPi.GPIO as GPIO
import sys
import argparse

class AutoAdvent():

    def __init__(self, today=None, debug=False):
        print "today: {0}".format(today)
        if(today == None):
            self.today = date.today()
        else:
            date_object = datetime.strptime(today, '%b %d %Y')
            self.today = datetime.date(date_object)
        print "self.today: {0}".format(self.today)

    #from http://stackoverflow.com/questions/2003870/how-can-i-select-all-of-the-sundays-for-a-year-using-python
    def allsundays(self, year):
       d = date(year, 11, 27)                    # January 1st
       d += timedelta(days = 6 - d.weekday())  # First Sunday
       while d.year == year:
          yield d
          d += timedelta(days = 7)

    def run(self):
        advent = []
        print self.today
        xmas=date(self.today.year,12,25)
        print self.today.year
        for d in self.allsundays(self.today.year):
            if d < xmas:
                advent.append(d)
    
        candles = 0
        for i in advent[-4:]:
            if self.today >= i and self.today <= xmas:
                print "{0} >= {1}".format(self.today,i)
                candles += 1
    
        print "candles: %d" % candles

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        pin = (17, 18, 21, 22)
        for i in range(candles):
            print pin[i]
            GPIO.setup(pin[i], GPIO.OUT)
            GPIO.output(pin[i], GPIO.HIGH)

        GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        while True:
            input_value = GPIO.input(23)
            if input_value == False:
                print "SHUTDOWN"
                os.system("sudo halt")
                sleep(1)


# following is executed when this script is run from the shell
if __name__ == '__main__':
    # parse arguments from the command line for the hashtag and LCD properties
    parser = argparse.ArgumentParser(description='Search Twitter for hashtag and display results on LCD')
    parser.add_argument('-v', '--verbose', action='store_true', default=False, help="print debug messages to shell")
    parser.add_argument('-t', '--today', help="specify a date for testing purposes, format: 'MMM DD YYYY'")
    args = parser.parse_args()
    autoAdvent = AutoAdvent(today=args.today, debug=args.verbose)
    autoAdvent.run()


