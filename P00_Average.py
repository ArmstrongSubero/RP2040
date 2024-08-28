# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P00_Average
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program demonstrates the aboslute basics of Pure Python
#                      on the PICO, reading an input, processing and output with Python
#                      use this program to get a hang of how python handles input and output 
# 
# Hardware Description: No special hardware. 
#                       
# Created: August 23rd, 2024, 6:00 PM
# Last Updated: August 27th, 2024, 09:47 PM
# Modified From example code by Dogan Ibrahim

print("Average of two numbers")
n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))

average = (n1 + n2) / 2
print("Average = ", average)
