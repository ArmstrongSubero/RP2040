# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P21_Abstraction_Simulated
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program demonstrates a simulated abstraction 
#                      by defining a base class 'LEDController' with methods 
#                      'on', 'off', and 'blink'. The 'SimpleLED' class 
#                      implements these methods. 
#                      This simulation is used as MicroPython does not support 
#                      abstract base classes like in standard Python.
# 
# Hardware Description: An LED is connected to pin 16
#                       
# Created: August 24th, 2024, 11:00 PM
# Last Updated: August 24th, 2024, 11:00 PM

from machine import Pin
import utime

# Simulating an abstract base class
class LEDController:
    
    def on(self):
        raise NotImplementedError("Subclasses should implement this method")

    def off(self):
        raise NotImplementedError("Subclasses should implement this method")

    def blink(self, delay):
        raise NotImplementedError("Subclasses should implement this method")

# Concrete class that implements the abstract methods
class SimpleLED(LEDController):
    def __init__(self, pin_number):
        self.led = Pin(pin_number, Pin.OUT)
    
    def on(self):
        self.led.value(1)
    
    def off(self):
        self.led.value(0)
    
    def blink(self, delay):
        self.on()
        utime.sleep(delay)
        self.off()
        utime.sleep(delay)

# Usage
led = SimpleLED(16)
led.blink(1)
