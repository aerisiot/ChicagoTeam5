#!/usr/bin/env python
import RPi.GPIO as GPIO
from time import sleep

TouchPin = x #pin where sensor is connected on GPIO board

var = 1
counter = 0 

GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
GPIO.setup(TouchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def pi_callback(channel):
  if var ==1:
    sleep(1.5)
    if GPIO.input(TouchPin):
      print "Sensor active"
   
      GPIO.remove_event_detect(TouchPin)
      GPIO.add_event_detect(TouchPin, GPIO.RISING, callback=pi_callback, bouncetime=300) 

GPIO.add_event_detect(TouchPin, GPIO.RISING, callback=pi_callback,bouncetime=300)

while True:
 pass
