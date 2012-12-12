#!/usr/bin/python 

from datetime import date, timedelta
import sys

year = int(sys.argv[1])

def allsundays(year):
   d = date(year, 1, 1)                    # January 1st
   d += timedelta(days = 6 - d.weekday())  # First Sunday
   while d.year == year:
      yield d
      d += timedelta(days = 7)

#for d in allsundays(2012):
   #print d
advent = []
xmas=date(year,12,25)
for d in allsundays(year):
   if d < xmas:
     advent.append(d)

today = date.today()

for i in advent[-4:]:
    print i  

candles = 0
for i in advent[-4:]:
   if today > i:
     print "{0} > {1}".format(today,i)
     candles += 1

print "candles: %d" % candles
