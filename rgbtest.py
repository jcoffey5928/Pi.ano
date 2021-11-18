from gpiozero import LED
from time import sleep

red = LED(12)
green = LED(19)
blue = LED(13)

def purple():
    red.on()
    green.off()
    blue.on()

def yellow():
    red.on()
    green.on()
    blue.off()

def cyan():
    red.off()
    green.on()
    blue.on()

purple()
sleep(1)
yellow()
sleep(1)
cyan()
sleep(1)
