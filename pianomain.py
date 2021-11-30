#!/usr/bin/env python3
#Name: pianomain.py
#Purpose: Entry point to the program.
#Developer: Jonathan Coffey

from pianoapp import PianoApp
import RPi.GPIO as GPIO

def main():
    app = PianoApp()
    try:
        app.run()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

if __name__ == "__main__": main()
