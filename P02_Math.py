# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P02_Math
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program demonstrates using the math library on the PICO,
#                      we use the 'pi' method of the math library to calculate the
#                      surface area of a cylinder on the Pico
# Hardware Description: No special hardware. 
#                       
# Created: August 23rd, 2024, 6:02 PM
# Last Updated: August 27th, 2024, 09:52 PM
# Modified From example code by Dogan Ibrahim

import math

print("Surface area of a cylinder")
r = float(input("Enter radius: "))
h = float(input("Enter height: "))

area = 2 * math.pi * r * h
print("Surface area = ", area)
