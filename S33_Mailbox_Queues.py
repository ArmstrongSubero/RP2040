# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S33_Mailbox_Queue
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      demonstrate use of async and await with a
#                      message Queue "mailbox", we use a list and
#                      asyncio.Lock to manage access to do intertask
#                      communication 
#                      
# Hardware Description: An LED is connected via 1k resistors to GP16 
#                       
# Created: August 23rd, 2024, 11:36 AM
# Last Updated: August 23rd, 2024, 11:36 AM

import uasyncio as asyncio
from machine import Pin

# Define GPIO pins for LEDs
LED_PIN = 16

# Set up the LED as an output pin
led = Pin(LED_PIN, Pin.OUT)

class SimpleQueue:
    def __init__(self):
        self._queue = []
        self._lock = asyncio.Lock()

    async def put(self, item):
        async with self._lock:
            self._queue.append(item)

    async def get(self):
        async with self._lock:
            if not self._queue:
                await asyncio.sleep(0)  # Yield control to allow other tasks to run
            return self._queue.pop(0) if self._queue else None

async def producer(queue):
    """Coroutine that sends messages (commands) to the mailbox (queue)."""
    while True:
        await asyncio.sleep(2)  # Simulate some work
        command = "toggle"
        print("Producer: Sending command to toggle LED.")
        await queue.put(command)  # Send a message (command) to the mailbox

async def consumer(queue):
    """Coroutine that receives messages (commands) from the mailbox (queue)."""
    while True:
        command = await queue.get()  # Wait for a message from the mailbox
        if command == "toggle":
            led.toggle()  # Perform the action (toggle the LED)
            print("Consumer: Toggled LED.")
        await asyncio.sleep(0)  # Yield control

async def main():
    # Create a simple queue (mailbox)
    mailbox = SimpleQueue()

    # Run the producer and consumer coroutines
    await asyncio.gather(producer(mailbox), consumer(mailbox))

# Run the main function
asyncio.run(main())
