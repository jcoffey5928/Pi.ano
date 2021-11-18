#!/usr/bin/env python3
#Name: keyboard.py
#Purpose: 
#Developer: Jonathan Coffey

#from gpiozero import RGBLED
#from time import sleep

class Keyboard:
    KEY_COLORS = {'C5': 'GREEN', 'D5': 'RED', 'E5': 'ORANGE', 'F5': 'PINK', 'G5': 'PURPLE'}
    keyPlayed = None

    #led = RGBLED(2, 3, 4)
    #led.off()
    
    @staticmethod
    def playKey(key):
        keyPlayed = key 

    @staticmethod
    def resetKey():
        keyPlayed = None
