# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S30_Round_Robin_Scheduling
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      demonstrate superloop style round robin scheduing
# 
# Hardware Description: LEDs are connected via 1k resistors to GP16 and GP17 
#                       
# Created: August 23rd, 2024, 11:05 AM
# Last Updated: August 23rd, 2024, 11:05 AM
import time
from machine import Pin

# Define the GPIO pins for the LEDs
LED_ONE = 16
LED_TWO = 17

# Set up the LEDs as output pins
led1 = Pin(LED_ONE, Pin.OUT)
led2 = Pin(LED_TWO, Pin.OUT)

def task1():
    led1.toggle()

def task2():
    led2.toggle()

while True:
    task1()
    task2()
    time.sleep(0.5)  # Add a small delay to make the toggling visible
