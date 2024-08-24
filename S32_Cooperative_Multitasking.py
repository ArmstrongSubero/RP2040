# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S32_Cooperative_Multitasking
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      demonstrate use of async and await for
#                      cooperative multitasking 
# 
# Hardware Description: LEDs are connected via 1k resistors to GP16 and GP17 
#                       
# Created: August 23rd, 2024, 11:28 AM
# Last Updated: August 23rd, 2024, 11:28 AM

import uasyncio as asyncio
from machine import Pin

# Define GPIO pins for LEDs
LED_ONE = 16
LED_TWO = 17

# Set up the LEDs as output pins
led1 = Pin(LED_ONE, Pin.OUT)
led2 = Pin(LED_TWO, Pin.OUT)

async def task1():
    while True:
        led1.toggle()
        print("Task 1: Toggled LED 1")
        await asyncio.sleep(0.5)  # Yield control and sleep for 0.5 seconds

async def task2():
    while True:
        led2.toggle()
        print("Task 2: Toggled LED 2")
        await asyncio.sleep(1)  # Yield control and sleep for 1 second

async def main():
    # Schedule both tasks to run concurrently
    await asyncio.gather(task1(), task2())

# Run the main function, which schedules the tasks
asyncio.run(main())
