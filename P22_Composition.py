# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P22_Composition
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program demonstrates composition by creating
#                      separate classes for LED control and timing, and 
#                      combining them using composition. The 'Timer' class 
#                      handles delays, and the 'LEDBlinker' class controls 
#                      the blinking of an LED using the 'LED' and 'Timer' 
#                      classes.
# 
# Hardware Description: An LED is connected to pin 16
#                       
# Created: August 24th, 2024, 11:15 PM
# Last Updated: August 24th, 2024, 11:15 PM

from machine import Pin
import utime

# Timer class to handle delays
class Timer:
    def delay(self, seconds):
        utime.sleep(seconds)

# LED class to control the LED
class LED:
    def __init__(self, pin_number):
        self.led = Pin(pin_number, Pin.OUT)

    def on(self):
        self.led.value(1)

    def off(self):
        self.led.value(0)

# LEDBlinker class to control LED blinking using composition
class LEDBlinker:
    def __init__(self, led, timer):
        self.led = led
        self.timer = timer

    def blink(self, delay=0.5):
        self.led.on()
        self.timer.delay(delay)
        self.led.off()
        self.timer.delay(delay)

# Usage example
led = LED(16)              # Create an LED object for pin 16
timer = Timer()            # Create a Timer object
blinker = LEDBlinker(led, timer)  # Create an LEDBlinker object using LED and Timer

while True:
    blinker.blink(1)  # Blink the LED with a 1-second delay
