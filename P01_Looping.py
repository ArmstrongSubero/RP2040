# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P01_Looping
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program demonstrates the aboslute basics of looping
#                      on the PICO, we use a for loop to read 10 numbers, average
#                      them then print the output 
# 
# Hardware Description: No special hardware. 
#                       
# Created: August 23rd, 2024, 6:00 PM
# Last Updated: August 27th, 2024, 09:50 PM
# Modified From example code by Dogan Ibrahim

print("Average of 10 numbers")
sum = 0

for n in range(10):
    print("Enter number", n + 1, ":", end='')
    m = float(input())
    sum = sum + m

average = sum / 10
print("Average= ", average)
