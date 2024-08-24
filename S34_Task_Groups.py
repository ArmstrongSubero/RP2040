# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S34_Task_Groups
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      demonstrate use of async and await to create
#                      a taskgroup, we mimic the behavior of a cancellation
#                      by using another coroutine 
#                      
# Hardware Description: LEDs are connected via 1k resistors to GP16 and GP17
#                       
# Created: August 23rd, 2024, 11:36 AM
# Last Updated: August 23rd, 2024, 11:36 AM

import uasyncio as asyncio
from machine import Pin

# Define GPIO pins for LEDs
LED_ONE = 16
LED_TWO = 17

# Set up the LEDs as output pins
led1 = Pin(LED_ONE, Pin.OUT)
led2 = Pin(LED_TWO, Pin.OUT)

async def blink_led1():
    try:
        while True:
            led1.toggle()
            print("LED 1 toggled")
            await asyncio.sleep(1)  # Blink every 1 second
    except asyncio.CancelledError:
        print("blink_led1 was cancelled")
        raise  # Re-raise the exception if you want to propagate the cancellation

async def blink_led2():
    try:
        while True:
            led2.toggle()
            print("LED 2 toggled")
            await asyncio.sleep(2)  # Blink every 2 seconds
    except asyncio.CancelledError:
        print("blink_led2 was cancelled")
        raise  # Re-raise the exception if you want to propagate the cancellation

async def cancel_task(task, delay):
    """Cancel a given task after a delay."""
    await asyncio.sleep(delay)
    print(f"Cancelling task after {delay} seconds")
    task.cancel()  # Cancel the task

async def main():
    # Create tasks manually
    task1 = asyncio.create_task(blink_led1())
    task2 = asyncio.create_task(blink_led2())

    # Simulate cancellation of task1 after 5 seconds
    asyncio.create_task(cancel_task(task1, 5))

    try:
        await asyncio.sleep(10)  # Run for 10 seconds
    except asyncio.CancelledError:
        print("main was cancelled")
    finally:
        task1.cancel()  # Ensure task 1 is canceled if not already
        task2.cancel()  # Cancel task 2
        await asyncio.gather(task1, task2, return_exceptions=True)
        print("Tasks were cancelled")

# Run the main function
asyncio.run(main())
