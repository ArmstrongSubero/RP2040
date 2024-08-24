# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S02_External_LED
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to flash the external
#                       LED on GP6 which is flashed every second
# 
# Hardware Description: An LED is connected through a 1k resistor to GP6
#                       
# Created: August 22nd, 2024, 7:41 PM
# Last Updated: August 22nd, 2024, 7:41 PM

import machine
import utime

LED = machine.Pin(6, machine.Pin.OUT)

while True:
    LED.value(1)
    utime.sleep(1)
    LED.value(0)
    utime.sleep(1)
