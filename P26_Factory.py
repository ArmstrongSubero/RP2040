# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P26_Factory_Pattern
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program demonstrates the Factory design pattern by
#                      creating different types of LED objects through a factory
#                      method. In this way we abstract away the creation logic.
# 
# Hardware Description: LEDs are connected to various pins.
#                       
# Created: August 25th, 2024, 12:00 AM
# Last Updated: August 25th, 2024, 12:00 AM

class LED:
    def __init__(self, pin_number):
        self.pin_number = pin_number

class LEDFactory:
    def create_led(self, pin_number):
        return LED(pin_number)

# Usage
factory = LEDFactory()
led1 = factory.create_led(16)
led2 = factory.create_led(17)

print(f"LED1 is on pin {led1.pin_number}")
print(f"LED2 is on pin {led2.pin_number}")
