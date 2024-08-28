# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P14_Casting
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program demonstrates type casting in Python by
#                      converting a user-provided decimal number into its
#                      binary, octal, and hexadecimal representations. 
#                      It showcases how Python can easily cast between 
#                      different number systems.
#
# Hardware Description: No special hardware is required.
#
# Created: August 23rd, 2024, 6:30 PM
# Last Updated: August 27th, 2024, 10:13 PM
# Modified from example code by Dogan Ibrahim


dec = int(input("Enter a number: "))
print("Decimal: ", dec)
print("Binary:  ", bin(dec))
print("Octal:   ", oct(dec))
print("Hex:     ", hex(dec))