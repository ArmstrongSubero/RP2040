# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S01_Blink
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to turn on the onboard
#                       LED on GP25 which is flashed every second
# 
# Hardware Description: Uses onboard LED
#                       
# Created: August 22nd, 2024, 7:35 PM
# Last Updated: August 22nd, 2024, 7:35 PM

import machine
import utime

LED = machine.Pin(25, machine.Pin.OUT)

while True:
    LED.value(1)
    utime.sleep(1)
    LED.value(0)
    utime.sleep(1)
