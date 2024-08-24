# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S31_Emergency_Exception_Buffer
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      demonstrate superloop style round robin scheduling
#                      and the use of emergency exception buffer to
#                      handle exceptions without dynamic memory allocation
#                      problems
# 
# Hardware Description: LEDs are connected via 1k resistors to GP16 and GP17 
#                       
# Created: August 23rd, 2024, 11:05 AM
# Last Updated: August 23rd, 2024, 11:05 AM

import time
import micropython
from machine import Pin

# Define the GPIO pins for the LEDs
LED_ONE = 16
LED_TWO = 17

# Set up the LEDs as output pins
led1 = Pin(LED_ONE, Pin.OUT)
led2 = Pin(LED_TWO, Pin.OUT)

# Allocate emergency exception buffer to handle interrupts
micropython.alloc_emergency_exception_buf(100)

def task1():
    try:
        led1.toggle()
        # Intentionally cause an exception to demonstrate emergency exception buffer
        if time.ticks_ms() % 5 == 0:
            raise ValueError("Simulated error in task1")
    except Exception as e:
        print("Emergency Exception in task1:", e)

def task2():
    try:
        led2.toggle()
        # Intentionally cause an exception to demonstrate emergency exception buffer
        if time.ticks_ms() % 7 == 0:
            raise ValueError("Simulated error in task2")
    except Exception as e:
        print("Emergency Exception in task2:", e)

# Superloop for round-robin scheduling
time_start = time.ticks_ms()

while True:
    task1()  # Execute task1 (toggle LED1)
    time.sleep_ms(200)  # Delay for 200 ms
    
    task2()  # Execute task2 (toggle LED2)
    time.sleep_ms(200)  # Delay for 200 ms
    
    seconds_live = time.ticks_diff(time.ticks_ms(), time_start) / 1000
    print("Executing for", seconds_live, "seconds")
