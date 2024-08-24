# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S16_Different_Blink_Rates
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      blink 2 LEDs at different rates using the
#                      separate cores 
# 
# Hardware Description: LEDs are connected to pins 16 and 17 
#                       
# Created: August 22nd, 2024, 11:45 PM
# Last Updated: August 22nd, 2024, 11:45 PM

from machine import Pin
import utime
import _thread

# Initialize LED objects
led_0 = Pin(16, Pin.OUT)  # LED controlled by core 0
led_1 = Pin(17, Pin.OUT)  # LED controlled by core 1

# Function to blink LED on core 1 at a specific rate
def core1_task():
    while True:
        led_1.toggle()  # Toggle the state of LED on pin 17
        utime.sleep(0.1)  # 300 ms delay (3.33 Hz blink rate)

# Start the core 1 task in a new thread
_thread.start_new_thread(core1_task, ())

# Main loop running on core 0 to blink LED at a different rate
while True:
    led_0.toggle()  # Toggle the state of LED on pin 16
    utime.sleep(0.5)  # 500 ms delay (2 Hz blink rate)
