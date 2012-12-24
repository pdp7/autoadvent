#!/bin/bash
LOG=/var/log/advent.log
# NOTE: if you have a Rev 2.0 Pi, then you'll need to 
# change "i2c-0" below to "i2c-1" as the I2C bus is on
# the GPIO header has changed between Rev 1 and 2
echo ds1307 0x68 > /sys/class/i2c-adapter/i2c-0/new_device
hwclock &> $LOG
date &>> $LOG
hwclock -s &>> $LOG
date &>> $LOG
/home/pi/autoadvent/autoadvent.py -v &>> $LOG
