# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P16_Class
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      control an LED using OOP principles
# 
# Hardware Description: An LED is connected to pin 16
#                       
# Created: August 23rd, 2024, 10:26 PM
# Last Updated: August 23rd, 2024, 10:26 PM

from machine import Pin
import utime

# Step 1: Define the LED class
class LED:
    def __init__(self, pin_number):
        self.led = Pin(pin_number, Pin.OUT)  # Initialize the LED pin

    def on(self):
        self.led.value(1)  # Turn the LED on

    def off(self):
        self.led.value(0)  # Turn the LED off

    def blink(self, delay=0.5):
        self.on()
        utime.sleep(delay)
        self.off()
        utime.sleep(delay)

# Step 2: Create an object of the LED class
led = LED(16)  # Create an LED object for pin 16

# Step 3: Use the LED object in a loop
while True:
    led.blink(0.1)  # Blink the LED with a 0.5-second delay

