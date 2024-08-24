# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S10_Fading_LED
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to use
#                      PWM to fade and LED
# 
# Hardware Description: An LED is connected via a 1k resistor to PIN21 (GPIO16)
#                       
# Created: August 22nd, 2024, 10:23 PM
# Last Updated: August 22nd, 2024, 10:23 PM

from machine import Pin, PWM
import utime

ch = PWM(Pin(16))
ch.freq(1000)

i = 0
while True:
    ch.duty_u16(i)
    utime.sleep_ms(300)
    i = i + 5000
    if i > 65535:
        i = 0
