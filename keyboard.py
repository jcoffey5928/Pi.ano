#!/usr/bin/env python3
#Name: keyboard.py
#Purpose: 
#Developer: Jonathan Coffey

from os import stat
#from gpiozero import RGBLED
#from gpiozero import Button
#from gpiozero import Buzzer
#from time import sleep

class Keyboard:
    keyColors = {'C': 'GREEN', 'D': 'RED', 'E': 'ORANGE', 'F': 'PINK', 'G': 'PURPLE'}
    keyPlayed = None

    #led = RGBLED(2, 3, 4)
    #led.off()
    
    @staticmethod
    def playKey(key):
        keyPlayed = key 

    @staticmethod
    def resetKey():
        keyPlayed = None
