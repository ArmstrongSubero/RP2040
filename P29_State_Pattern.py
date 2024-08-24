# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P29_State_Pattern
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program demonstrates the State design pattern by
#                      creating an LED that changes behavior based on its state.
#                      The pattern allows an object to alter its behavior when its
#                      internal state changes.
# 
# Hardware Description: An LED is connected to pin 16.
#                       
# Created: August 23rd, 2024, 12:11 AM
# Last Updated: August 23rd, 2024, 12:11 AM

from machine import Pin
import utime

class LEDState:
    def on(self, led):
        pass
    
    def off(self, led):
        pass

class LEDOnState(LEDState):
    def on(self, led):
        print("LED is already ON")
    
    def off(self, led):
        print("Turning LED OFF")
        led.state = LEDOffState()
        led.led.value(0)

class LEDOffState(LEDState):
    def on(self, led):
        print("Turning LED ON")
        led.state = LEDOnState()
        led.led.value(1)
    
    def off(self, led):
        print("LED is already OFF")

class LED:
    def __init__(self, pin_number):
        self.led = Pin(pin_number, Pin.OUT)
        self.state = LEDOffState()  # Default to OFF state
    
    def on(self):
        self.state.on(self)
    
    def off(self):
        self.state.off(self)

# Usage
led = LED(16)

# Turn the LED on and off, changing its state
led.on()  # Outputs: "Turning LED ON"
utime.sleep(1)
led.off()  # Outputs: "Turning LED OFF"
utime.sleep(1)
led.off()  # Outputs: "LED is already OFF"
