# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S03_Timer
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to flash the external
#                       LED on GP6 which is flashed every second using a Timer
# 
# Hardware Description: An LED is connected through a 1k resistor to GP6
#                       
# Created: August 22nd, 2024, 7:47 PM
# Last Updated: August 22nd, 2024, 7:47 PM

from machine import Pin, Timer

LED = Pin(6, Pin.OUT)

tim = Timer()

def Flash_LED(timer):
    global LED
    LED.toggle()

tim.init(freq = 2.0, mode = Timer.PERIODIC, callback = Flash_LED)
