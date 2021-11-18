from gpiozero import RGBLED
from time import sleep

class Light:
    light = RGBLED(12, 19, 13)

    def setColor(self, color, delay):
        self.light.on(color)
        if (delay > 0):
            sleep(delay)
        self.light.off

    def turnOff(self):
        self.light.off()
