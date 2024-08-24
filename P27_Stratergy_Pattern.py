# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P28_Strategy_Pattern
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program demonstrates the Strategy design pattern by
#                      allowing different algorithms (strategies) for controlling
#                      an LED's blinking pattern. Using this we can allow an algorithm
#                      to vary independently from the clients that use it. In this
#                      exmaple we can switch between two different blinking algorithms
#                      without changing its own logic. Each one is encapsulated and
#                      interchangeable 
# 
# Hardware Description: An LED is connected to pin 16.
#                       
# Created: August 25th, 2024, 12:10 AM
# Last Updated: August 25th, 2024, 12:10 AM

from machine import Pin
import utime

class LED:
    def __init__(self, pin_number):
        self.led = Pin(pin_number, Pin.OUT)

    def on(self):
        self.led.value(1)

    def off(self):
        self.led.value(0)

class BlinkingStrategy:
    def blink(self, led):
        pass

class FastBlinkStrategy(BlinkingStrategy):
    def blink(self, led):
        for _ in range(3):
            led.on()
            utime.sleep(0.2)
            led.off()
            utime.sleep(0.2)

class SlowBlinkStrategy(BlinkingStrategy):
    def blink(self, led):
        for _ in range(3):
            led.on()
            utime.sleep(1)
            led.off()
            utime.sleep(1)

class LEDBlinker:
    def __init__(self, led, strategy):
        self.led = led
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def blink(self):
        self.strategy.blink(self.led)

# Usage
led = LED(16)
fast_strategy = FastBlinkStrategy()
slow_strategy = SlowBlinkStrategy()

blinker = LEDBlinker(led, fast_strategy)
blinker.blink()  # Fast blink

blinker.set_strategy(slow_strategy)
blinker.blink()  # Slow blink
