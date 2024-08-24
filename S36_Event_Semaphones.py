# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S36_Event_Semaphore
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      demonstrate use of async and await simulate
#                      semaphore like control for event handling
#                      using eventflags 
#                      
# Hardware Description: LEDs are connected via 1k resistors to GP16 and GP17
#                       
# Created: August 23rd, 2024, 11:59 AM
# Last Updated: August 23rd, 2024, 11:59 AM

import uasyncio as asyncio
from machine import Pin

# Define GPIO pins for LEDs
LED_EVENT = 16

# Set up the LED as an output pin
led_event = Pin(LED_EVENT, Pin.OUT)

# Create an event object
event = asyncio.Event()

async def event_listener():
    """Task that waits for an event to be triggered."""
    while True:
        print("Listener: Waiting for event...")
        await event.wait()  # Wait for the event to be set
        led_event.toggle()  # Toggle the LED when event is set
        print("Listener: Event detected! Toggling LED.")
        event.clear()  # Reset the event for the next iteration

async def event_trigger():
    """Task that triggers an event after a delay."""
    while True:
        await asyncio.sleep(5)  # Wait 5 seconds before triggering the event
        print("Trigger: Setting event.")
        event.set()  # Set the event to notify the listener

async def main():
    # Run both tasks concurrently
    await asyncio.gather(event_listener(), event_trigger())

# Run the main function
asyncio.run(main())
