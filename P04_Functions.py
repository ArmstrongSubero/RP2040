# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P04_Functions
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program demonstrates using functions in pure
#                      Python on the Pico. In this case we create a
#                      function to calculate surface area and volume of a
#                      cylinder. 
#
# Hardware Description: No special hardware. 
#                       
# Created: August 23rd, 2024, 6:00 PM
# Last Updated: August 27th, 2024, 09:52 PM
# Modified From example code by Dogan Ibrahim

import math

print("Surface area and volume of a cylinder")

def Calc(r, h):
    area = 2 * math.pi * r * h
    volume = math.pi * r * r * h
    return(area, volume)

radius = float(input("Enter radius: "))
height = float(input("Enter height: "))

area, vol = Calc(radius, height)
print("Surface area = ",area," Volume= ", vol)