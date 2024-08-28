# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P03_Conversion
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program gives you a bit more practice with pure Python
#                      on the Pico, we do a simple degrees celcius to farenheit conversion 
#
# Hardware Description: No special hardware. 
#                       
# Created: August 23rd, 2024, 6:04 PM
# Last Updated: August 27th, 2024, 09:53 PM
# Modified From example code by Dogan Ibrahim

print("Degrees C to Degrees F")
C = float(input("Enter C: "))
F = 1.8 * C + 32.0

print(C, "Degrees C = ", F, "Degrees F")