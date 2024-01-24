#!/usr/bin/env python3
########################################################################
# Filename    : Blink.py
# Description : Basic usage of GPIO. Let led blink.
# auther      : www.freenove.com
# modification: 2019/12/28
########################################################################
import RPi.GPIO as GPIO
import time

ledPinGreen = 31    # define ledPin
ledPinYell = 33

def setup():
    GPIO.setmode(GPIO.BOARD)       # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPinGreen, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.setup(ledPinYell, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.output(ledPinGreen, GPIO.LOW)  # make ledPin output LOW level 
    GPIO.output(ledPinYell, GPIO.LOW)  # make ledPin output LOW level 
    print (f'using pin green {ledPinGreen}; using pin yellow {ledPinYell}; ')

def loop():
    while True:
        GPIO.output(ledPinGreen, GPIO.LOW)
        GPIO.output(ledPinYell, GPIO.HIGH)  # make ledPin output HIGH level to turn on led
        print ('led turned on >>>')     # print information on terminal
        time.sleep(0.1)                   # Wait for 1 second
        GPIO.output(ledPinYell, GPIO.LOW)   # make ledPin output LOW level to turn off led
        GPIO.output(ledPinGreen, GPIO.HIGH)   # make ledPin output LOW level to turn off led
        print ('led turned off <<<')
        time.sleep(0.1)                   # Wait for 1 second

def destroy():
    GPIO.cleanup()                      # Release all GPIO

if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()

