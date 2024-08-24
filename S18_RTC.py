# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S18_RTC
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      use the onboard RTC
# 
# Hardware Description: The PICO is connected to PC via USB
#                       
# Created: August 23rd, 2024, 12:04 AM
# Last Updated: August 23rd, 2024, 12:04 AM

from machine import RTC
import utime

# Initialize the RTC (Real-Time Clock)
rtc = RTC()

# Set a specific date and time: (year, month, day, weekday, hours, minutes, seconds, subseconds)
rtc.datetime((2017, 8, 23, 2, 12, 48, 0, 0))

while True:
    # Get the current date and time from the RTC
    current_time = rtc.datetime()
    
    # Print the current date and time
    print(current_time)
    
    # Sleep for 1 second before repeating
    utime.sleep(1)
