# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S21_Unique_Identifier
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      display the Unique Identifer for each board
# 
# Hardware Description: The PICO is connected to PC via USB
#                       
# Created: August 23rd, 2024, 10:57 AM
# Last Updated: August 23rd, 2024, 10:57 AM

import machine
import ubinascii

my_id = ubinascii.hexlify(machine.unique_id()).decode()
print(f"Unique ID: {my_id}")