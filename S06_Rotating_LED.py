# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S06_Rotating_LED
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to 
#                      rotate 4 LEDs left
# 
# Hardware Description: LEDs are connected to pins 16, 17, 18 and 19
#                       
# Created: August 22nd, 2024, 8:22 PM
# Last Updated: August 22nd, 2024, 8:22 PM

from machine import Pin
import utime


LEDS = [16, 17, 18, 19]
L = [0, 0, 0, 0]

for i in range(4):
    L[i] = Pin(LEDS[i], Pin.OUT)

while True: 
    for i in range(4):
        L[i].value(1)
        utime.sleep(0.5)
        L[i].value(0)