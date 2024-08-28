# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P10_Reverse_Words
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program demonstrates a common programming
#                      problem given to beginners, to reverse a string
#
# Hardware Description: No special hardware is required.
#
# Created: August 23rd, 2024, 6:27 PM
# Last Updated: August 27th, 2024, 10:07 PM
# Modified from example code by Dogan Ibrahim

word = input("Enter a word: ")
l = len(word)
k = 0

while l != 0:
    k = k - 1
    print(word[k])
    l = l - 1
    
    