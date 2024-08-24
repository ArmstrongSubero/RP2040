# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P17_Dual_Core_Class
# Interpreter: MicroPython (latest version)
# Program Version: 1.1
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      demonstrate dual core usage with OOP
# 
# Hardware Description: LEDs are connected to pins 16 and 17 
#                       
# Created: August 22nd, 2024, 11:30 PM
# Last Updated: August 22nd, 2024, 11:20 PM

from machine import Pin
import utime
import _thread

# LED class as defined earlier
class LED:
    def __init__(self, pin_number):
        self.led = Pin(pin_number, Pin.OUT)

    def on(self):
        self.led.value(1)

    def off(self):
        self.led.value(0)

    def blink(self, delay=0.5):
        self.on()
        utime.sleep(delay)
        self.off()
        utime.sleep(delay)

# Creating LED objects for both cores
led_0 = LED(16)  # LED for core 0
led_1 = LED(17)  # LED for core 1

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
