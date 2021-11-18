#!/usr/bin/env python3
#Name: keyboard.py
#Purpose: 
#Developer: Jonathan Coffey

class Keyboard:
    KEY_COLORS = {'C5': 'GREEN', 'D5': 'RED', 'E5': 'ORANGE', 'F5': 'PINK', 'G5': 'PURPLE'}
    keyPlayed = None
    
    @staticmethod
    def playKey(key):
        keyPlayed = key 

    @staticmethod
    def resetKey():
        keyPlayed = None
