# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P07_Trig_Functions
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program takes things a step further, and we
#                      look at conditional statments in Python. 
#
# Hardware Description: No special hardware. 
#                       
# Created: August 23rd, 2024, 6:20 PM
# Last Updated: August 27th, 2024, 10:04 PM
# Modified From example code by Dogan Ibrahim

import math

angle = float(input("Enter angle in degrees: "))
trig = input("sine (s), cosine (c), tangent(t): ")
rad = math.radians(angle)

if trig == "s":
    print(math.sin(rad))

elif trig == "c":
    print(math.cos(rad))

elif trig == "t":
    print(math.tan(rad))

else:
    print("Error in input")