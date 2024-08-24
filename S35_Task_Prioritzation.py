# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S35_Task_Prioritzation
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      demonstrate use of async and await simulate
#                      task prioritization
#                      
# Hardware Description: LEDs are connected via 1k resistors to GP16 and GP17
#                       
# Created: August 23rd, 2024, 11:59 AM
# Last Updated: August 23rd, 2024, 11:59 AM

import uasyncio as asyncio
from machine import Pin

# Define GPIO pins for LEDs
LED_HIGH_PRIORITY = 16
LED_LOW_PRIORITY = 17

# Set up the LEDs as output pins
led_high = Pin(LED_HIGH_PRIORITY, Pin.OUT)
led_low = Pin(LED_LOW_PRIORITY, Pin.OUT)

async def high_priority_task():
    while True:
        led_high.toggle()
        print("High-priority task: LED 1 toggled")
        await asyncio.sleep(0.01)  # Very short sleep to yield often

async def low_priority_task():
    while True:
        led_low.toggle()
        print("Low-priority task: LED 2 toggled")
        # Manually yield control more often but execute less frequently
        for _ in range(10):  # Yield control 10 times before actually running the task
            await asyncio.sleep(0)
        await asyncio.sleep(1)  # Sleep longer between executions

async def main():
    # Run both tasks concurrently
    await asyncio.gather(high_priority_task(), low_priority_task())

# Run the main function
asyncio.run(main())
