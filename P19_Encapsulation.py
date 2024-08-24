# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P19_Encapsulation
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program demonstrates encapsulation by
#                      controlling access to the LED state.
# 
# Hardware Description: LEDs are connected to pins 16 and 17 
#                       
# Created: August 23rd, 2024, 11:00 PM
# Last Updated: August 23rd, 2024, 11:00 PM

from machine import Pin
import utime
import _thread

class LED:
    def __init__(self, pin_number):
        self.__led = Pin(pin_number, Pin.OUT)  # Private attribute for LED pin

    def on(self):
        self.__led.value(1)

    def off(self):
        self.__led.value(0)

    def blink(self, delay=0.5):
        self.on()
        utime.sleep(delay)
        self.off()
        utime.sleep(delay)

    def get_state(self):
        return self.__led.value()

# Inherited class with extended functionality
class BlinkingLED(LED):
    def __init__(self, pin_number, blink_times=3):
        super().__init__(pin_number)
        self.blink_times = blink_times

    def blink(self, delay=0.5):
        for _ in range(self.blink_times):
            super().blink(delay)

# Creating objects using the new BlinkingLED class
led_0 = BlinkingLED(16, blink_times=3)
led_1 = BlinkingLED(17, blink_times=5)

# Semaphore lock
spLock = _thread.allocate_lock()

# Core 1 task function
def core1_task():
    while True:
        spLock.acquire()
        print("Message from core_1")
        led_1.blink(0.1)
        spLock.release()

# Start the core 1 task in a new thread
_thread.start_new_thread(core1_task, ())

# Core 0 main loop
while True:
    spLock.acquire()
    print("Message from core_0")
    led_0.blink(0.5)
    spLock.release()
