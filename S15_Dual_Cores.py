# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S15_Dual_Cores
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      demonstrate dual core usage
# 
# Hardware Description: LEDs are connected to pins 16 and 17 
#                       
# Created: August 22nd, 2024, 11:30 PM
# Last Updated: August 22nd, 2024, 11:20 PM

from machine import Pin
import utime  # Access internal clock of Raspberry Pi Pico
import _thread  # To access threading function

# Declaring LED objects
led_0 = Pin(16, Pin.OUT)  # LED object for core_0
led_1 = Pin(17, Pin.OUT)  # LED object for core_1

# Creating semaphore lock
spLock = _thread.allocate_lock()

# Function to run on core 1
def core1_task():
    while True:
        spLock.acquire()  # Acquiring semaphore lock
        print("Message from core_1")
        led_1.value(1)  # Turn on LED on pin 17
        utime.sleep(0.5)  # 0.5 second delay
        led_1.value(0)  # Turn off LED on pin 17
        spLock.release()  # Release semaphore lock

# Start the core 1 task in a new thread
_thread.start_new_thread(core1_task, ())

# Main loop running on core 0
while True:
    spLock.acquire()  # Acquiring semaphore lock
    print("Message from core_0")
    led_0.value(1)  # Turn on LED on pin 16
    utime.sleep(0.5)  # 0.5 second delay
    led_0.value(0)  # Turn off LED on pin 16
    spLock.release()  # Release semaphore lock
