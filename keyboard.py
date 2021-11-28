#Name: keyboard.py
#Purpose: 
#Developer: Jonathan Coffey

import RPi.GPIO as GPIO
import time

class Keyboard:
    KEY_COLORS = {'C5': 'green', 'D5': 'red', 'E5': 'orange', 'F5': 'pink', 'G5': 'purple'}
    keyPlayed = None

    GPIO.setmode(GPIO.BCM)
    KEY1 = GPIO.setup(4,GPIO.IN)
    KEY2 = GPIO.setup(14,GPIO.IN)
    KEY3 = GPIO.setup(15,GPIO.IN)
    KEY4 = GPIO.setup(17,GPIO.IN)
    KEY5 = GPIO.setup(18,GPIO.IN)
    
    @staticmethod
    def playKey(key):
        keyPlayed = key 

    @staticmethod
    def resetKey():
        keyPlayed = None

    @staticmethod
    def play():
        #initialise a previous input variable to 0 (Assume no pressure applied)
        prev_input = 0
        try:
            while True:
                #take a reading
                input = GPIO.input(4)
                #if the last reading was low and this one high, alert us
                if ((not prev_input) and input):
                    print("Under Pressure")
                #update previous input
                prev_input = input
                #slight pause
                time.sleep(0.10)
        except KeyboardInterrupt:
            pass
        finally:
            GPIO.cleanup()