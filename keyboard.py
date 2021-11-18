#!/usr/bin/env python3
#Name: keyboard.py
#Purpose: 
#Developer: Jonathan Coffey

class Keyboard:
    KEY_COLORS = {'C5': 'green', 'D5': 'red', 'E5': 'orange', 'F5': 'pink', 'G5': 'purple'}
    keyPlayed = None
    
    @staticmethod
    def playKey(key):
        keyPlayed = key 

    @staticmethod
    def resetKey():
        keyPlayed = None
