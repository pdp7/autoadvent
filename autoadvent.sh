#!/bin/bash
LOG=/var/log/advent.log
echo ds1307 0x68 > /sys/class/i2c-adapter/i2c-1/new_device
hwclock &> $LOG
date &>> $LOG
hwclock -s &>> $LOG
date &>> $LOG
/home/pi/autoadvent/autoadvent.py "Dec 20 2012" &>> $LOG
