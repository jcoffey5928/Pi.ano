#Name: keyboard.py
#Purpose: 
#Developer: Jonathan Coffey

import RPi.GPIO as GPIO
import time

class Keyboard:
    keyPlayed = None

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4,GPIO.IN)
    GPIO.setup(14,GPIO.IN)
    GPIO.setup(15,GPIO.IN)
    GPIO.setup(17,GPIO.IN)
    GPIO.setup(18,GPIO.IN)

    KEY1 = GPIO.input(4)
    KEY2 = GPIO.input(14)
    KEY3 = GPIO.input(15)
    KEY4 = GPIO.input(17)
    KEY5 = GPIO.input(18)

    KEY_NOTES = {KEY1 : 'C5', 
                KEY2 : 'D5', 
                KEY3 : 'E5' , 
                KEY4 : 'F5' , 
                KEY5 : 'G5'}
    KEY_COLORS = {KEY_NOTES.get(KEY1) : 'green', 
                 KEY_NOTES.get(KEY2) : 'red',
                 KEY_NOTES.get(KEY3) : 'orange', 
                 KEY_NOTES.get(KEY4) : 'pink', 
                 KEY_NOTES.get(KEY5) : 'purple'}
    
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
                #if the last reading was low and this one high, alert us
                if ((not prev_input) and Keyboard.KEY1):
                    print()
                #update previous input
                prev_input = input
                #slight pause
                time.sleep(0.10)
        except KeyboardInterrupt:
            pass
        finally:
            GPIO.cleanup()