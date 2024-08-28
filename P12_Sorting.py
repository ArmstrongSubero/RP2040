# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P12_Sorting
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program demonstrates the use of the built in
#                      sorting function of Micropython. Being pre Python 3.11
#                      the expected algorithm will be Timsort as opposed to
#                      Powersort in later Python versions. 
#
# Hardware Description: No special hardware is required.
#
# Created: August 23rd, 2024, 6:28 PM
# Last Updated: August 27th, 2024, 10:08 PM
# Modified from example code by Dogan Ibrahim

MyList = ['italy', 'france', 'germany', 'india', 'china']
MyList.sort()

print("Sorted list: ", MyList)