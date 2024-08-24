# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S17_Sharing_Data
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      share data between cores
# 
# Hardware Description: The PICO is connected to PC via USB
#                       
# Created: August 22nd, 2024, 11:50 PM
# Last Updated: August 22nd, 2024, 11:50 PM

from machine import Pin
import utime
import _thread

# Initialize shared data and lock
shared_counter = 0
data_lock = _thread.allocate_lock()
last_read_counter = -1  # Track the last counter value read by core 1

# Function to run on core 1 to read and print the shared counter
def core1_task():
    global shared_counter, last_read_counter
    while True:
        data_lock.acquire()  # Acquire the lock to access shared data
        if shared_counter != last_read_counter:
            print(f"Core 1 reads counter: {shared_counter}")
            last_read_counter = shared_counter
        data_lock.release()  # Release the lock after reading
        utime.sleep(0.1)  # Small delay to avoid busy-waiting

# Start the core 1 task in a new thread
_thread.start_new_thread(core1_task, ())

# Main loop running on core 0 to increment the counter
while True:
    data_lock.acquire()  # Acquire the lock to access shared data
    shared_counter += 1  # Increment the shared counter
    print(f"Core 0 increments counter to: {shared_counter}")
    data_lock.release()  # Release the lock after incrementing
    utime.sleep(2)  # Sleep for 2 seconds
