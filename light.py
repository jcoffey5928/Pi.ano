from os import error
from gpiozero import RGBLED
from colorzero import Color
from time import sleep

class Light:

    # param in order: Red, Green, Blue
    def __init__(self, pin1, pin2, pin3):
        self.led = RGBLED(pin1, pin2, pin3)

    def onWithDelay(self, colStr, delay):
        if (delay > 0):
            self.led.color = Color(colStr)
            sleep(delay)
            self.turnOff()
        else:
            print(f'Invalid delay of {delay} seconds')

    # Default color will be white
    def turnOn(self):
        self.led.color = Color('white')

    def turnOff(self):
        self.led.off()
