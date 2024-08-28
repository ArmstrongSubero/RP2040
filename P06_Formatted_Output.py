# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P06_Formatted_Output
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program demonstrates using formatted output
#                      simply in Python using a combination of spaces
#                      and tabs, useful for printing things like sensor
#                      output and the sorts.
#
# Hardware Description: No special hardware. 
#                       
# Created: August 23rd, 2024, 6:07 PM
# Last Updated: August 27th, 2024, 10:00 PM
# Modified From example code by Dogan Ibrahim

print("TABLE OF SUQARES")
print("================")
print("N      Square")

for i in range(11):
    n = i + 1
    print(n, "\t", n * n)
    