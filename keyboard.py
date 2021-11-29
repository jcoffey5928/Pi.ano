#Name: keyboard.py
#Purpose: 
#Developer: Jonathan Coffey

import RPi.GPIO as GPIO
from time import sleep

class Keyboard:
    KEY_COLORS = {'C5': 'green', 'D5': 'red', 'E5': 'orange', 'F5': 'pink', 'G5': 'purple'}
    RETURN_SEQUENCE = ['C5', 'C5', 'C5', 'C5', 'C5']
    keyPlayed = None

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4,GPIO.IN)
    GPIO.setup(14,GPIO.IN)
    GPIO.setup(15,GPIO.IN)
    GPIO.setup(17,GPIO.IN)
    GPIO.setup(18,GPIO.IN)

    @staticmethod
    def play(controller):
        keyReturnList = []
        #initialise a previous input variable to 0 (Assume no pressure applied)
        prev_KEY1 = 0
        prev_KEY2 = 0
        prev_KEY3 = 0
        prev_KEY4 = 0
        prev_KEY5 = 0
        while True:
            print(keyReturnList)
            if (len(keyReturnList) == 5):
                if (keyReturnList == Keyboard.RETURN_SEQUENCE):
                    break;
            if (len(keyReturnList) > 5):
                keyReturnList.pop(0)
            #take a reading
            KEY1 = GPIO.input(4)
            KEY2 = GPIO.input(14)
            KEY3 = GPIO.input(15)
            KEY4 = GPIO.input(17)
            KEY5 = GPIO.input(18)
            #if the last reading was low and this one high, alert us
            if ((not prev_KEY1) and KEY1):
                print("Played: C5")
                keyReturnList.append("C5")
                Keyboard.keyPlayed = "C5"
            elif ((not prev_KEY2) and KEY2):
                print("Played: D5")
                keyReturnList.append("D5")
                Keyboard.keyPlayed = "D5"
            elif ((not prev_KEY3) and KEY3):
                print("Played: E5")
                keyReturnList.append("E5")
                Keyboard.keyPlayed = "E5"
            elif ((not prev_KEY4) and KEY4):
                print("Played: F5")
                keyReturnList.append("F5")
                Keyboard.keyPlayed = "F5"
            elif ((not prev_KEY5) and KEY5):
                print("Played: G5")
                keyReturnList.append("G5")
                Keyboard.keyPlayed = "G5"

            controller.playKeyWithLight(Keyboard.keyPlayed, 0.1)
            #update previous input
            prev_KEY1 = KEY1
            prev_KEY2 = KEY2
            prev_KEY3 = KEY3
            prev_KEY4 = KEY4
            prev_KEY5 = KEY5
            controller.update()

    @staticmethod
    def learn(controller):
        keyReturnList = []
        #initialise a previous input variable to 0 (Assume no pressure applied)
        prev_KEY1 = 0
        prev_KEY2 = 0
        prev_KEY3 = 0
        prev_KEY4 = 0
        prev_KEY5 = 0
        while True:
            print(keyReturnList)
            if (len(keyReturnList) == 5):
                if (keyReturnList == Keyboard.RETURN_SEQUENCE):
                    break;
            if (len(keyReturnList) > 5):
                keyReturnList.pop(0)
            #take a reading
            KEY1 = GPIO.input(4)
            KEY2 = GPIO.input(14)
            KEY3 = GPIO.input(15)
            KEY4 = GPIO.input(17)
            KEY5 = GPIO.input(18)
            #if the last reading was low and this one high, alert us
            if ((not prev_KEY1) and KEY1):
                print("Played: C5")
                keyReturnList.append("C5")
                controller.playKeyWithLight("C5", 0.1)
            elif ((not prev_KEY2) and KEY2):
                print("Played: D5")
                keyReturnList.append("D5")
                controller.playKeyWithLight("D5", 0.1)
            elif ((not prev_KEY3) and KEY3):
                print("Played: E5")
                keyReturnList.append("E5")
                controller.playKeyWithLight("E5", 0.1)
            elif ((not prev_KEY4) and KEY4):
                print("Played: F5")
                keyReturnList.append("F5")
                controller.playKeyWithLight("F5", 0.1)
            elif ((not prev_KEY5) and KEY5):
                print("Played: G5")
                keyReturnList.append("G5")
                controller.playKeyWithLight("G5", 0.1)
            #update previous input
            prev_KEY1 = KEY1
            prev_KEY2 = KEY2
            prev_KEY3 = KEY3
            prev_KEY4 = KEY4
            prev_KEY5 = KEY5
