#Name: keyboard.py
#Purpose: 
#Developer: Jonathan Coffey

import RPi.GPIO as GPIO
import time

class Keyboard:
    KEY_COLORS = {'C5': 'green', 'D5': 'red', 'E5': 'orange', 'F5': 'pink', 'G5': 'purple'}
    keyPlayed = None

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4,GPIO.IN)
    GPIO.setup(14,GPIO.IN)
    GPIO.setup(15,GPIO.IN)
    GPIO.setup(17,GPIO.IN)
    GPIO.setup(18,GPIO.IN)
    
    @staticmethod
    def playKey(key):
        keyPlayed = key 

    @staticmethod
    def resetKey():
        keyPlayed = None

    @staticmethod
    def play(buzzer):
        #initialise a previous input variable to 0 (Assume no pressure applied)
        prev_input = 0
        try:
            while True:
                #take a reading
                KEY1 = GPIO.input(4)
                KEY2 = GPIO.input(4)
                KEY3 = GPIO.input(4)
                KEY4 = GPIO.input(4)
                KEY5 = GPIO.input(4)
                #if the last reading was low and this one high, alert us
                if ((not prev_input) and KEY1):
                    print(KEY1)
                #update previous input
                prev_input = input
                #slight pause
                time.sleep(0.10)
        except KeyboardInterrupt:
            pass
        finally:
            GPIO.cleanup()