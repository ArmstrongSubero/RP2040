# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P07_Trigonometry
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program seeks to get you more acquanited with
#                      Python. Here we combine formatted output with the
#                      math library combining two concepts you learnt before.
#                      In this case we create a formatted table of Trignometric sin. 
#
# Hardware Description: No special hardware. 
#                       
# Created: August 23rd, 2024, 6:18 PM
# Last Updated: August 27th, 2024, 10:02 PM
# Modified From example code by Dogan Ibrahim

import math

print("TABLE OF TRIGNONOMETRIC SIN")
print("==========================")

print("N               Sin")

for i in range(0, 50, 5):
    d = math.radians(i)
    print(i, "\t", math.sin(d))
