# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S37_Task_Management_System
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      demonstrate use of async and await simulate
#                      a basic task management system
#                      
# Hardware Description: LEDs are connected via 1k resistors to GP16,GP17 and GP18
#                       
# Created: August 23rd, 2024, 11:59 AM
# Last Updated: August 23rd, 2024, 11:59 AM
import uasyncio as asyncio
from machine import Pin

# Define GPIO pins for LEDs representing different tasks
LED_HIGH_PRIORITY = 16
LED_MEDIUM_PRIORITY = 17
LED_LOW_PRIORITY = 18

# Set up the LEDs as output pins
led_high = Pin(LED_HIGH_PRIORITY, Pin.OUT)
led_medium = Pin(LED_MEDIUM_PRIORITY, Pin.OUT)
led_low = Pin(LED_LOW_PRIORITY, Pin.OUT)

# Task definitions with priority
tasks = []

async def high_priority_task():
    led_high.toggle()  # Toggle the high-priority LED
    print("High-priority task: Running...")
    await asyncio.sleep(0)  # Immediate yield to allow high frequency

async def medium_priority_task():
    led_medium.toggle()  # Toggle the medium-priority LED
    print("Medium-priority task: Running...")
    await asyncio.sleep(0.1)

async def low_priority_task():
    led_low.toggle()  # Toggle the low-priority LED
    print("Low-priority task: Running...")
    await asyncio.sleep(0.1)

async def idle_task():
    print("Idle task: System is idle...")
    await asyncio.sleep(0.1)

async def custom_scheduler():
    while True:
        # Execute high-priority task more frequently, but not exclusively
        for priority, task in sorted(tasks, key=lambda x: x[0]):
            # Assign more execution slots to higher-priority tasks
            exec_slots = 10 if priority == 1 else 5 if priority == 2 else 2
            for _ in range(exec_slots):
                await task()
        await asyncio.sleep(0)  # Yield control to allow for other processing

def add_task(priority, task):
    tasks.append((priority, task))

async def main():
    # Add tasks with assigned priorities
    add_task(1, high_priority_task)    # Highest priority
    add_task(2, medium_priority_task)  # Medium priority
    add_task(3, low_priority_task)     # Lowest priority
    add_task(4, idle_task)             # Idle task

    # Run the custom scheduler
    await custom_scheduler()

# Run the main function
asyncio.run(main())
