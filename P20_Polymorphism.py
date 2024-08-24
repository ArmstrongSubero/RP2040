# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P20_Polymorphism
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program demonstrates polymorphism by creating
#                      multiple LED behaviors using OOP. In this case the
#                      FastBlinkingLED class overrides the blink method from
#                      the 'LED' class demonstrating polymorphism 
# 
# Hardware Description: LEDs are connected to pins 16 and 17 
#                       
# Created: August 23rd, 2024, 11:30 PM
# Last Updated: August 23rd, 2024, 11:30 PM

from machine import Pin
import utime
import _thread

class LED:
    def __init__(self, pin_number):
        self.led = Pin(pin_number, Pin.OUT)

    def blink(self, delay=0.5):
        self.led.value(1)
        utime.sleep(delay)
        self.led.value(0)
        utime.sleep(delay)

class FastBlinkingLED(LED):
    def blink(self, delay=0.2):  # Overriding the blink method
        for _ in range(5):
            self.led.value(1)
            utime.sleep(delay)
            self.led.value(0)
            utime.sleep(delay)

# Creating objects of different types
led_0 = LED(16)
led_1 = FastBlinkingLED(17)

# Semaphore lock
spLock = _thread.allocate_lock()

# Core 1 task function
def core1_task():
    while True:
        spLock.acquire()
        print("Message from core_1")
        led_1.blink()  # Fast blink on core 1
        spLock.release()

# Start the core 1 task in a new thread
_thread.start_new_thread(core1_task, ())

# Core 0 main loop
while True:
    spLock.acquire()
    print("Message from core_0")
    led_0.blink()  # Regular blink on core 0
    spLock.release()
