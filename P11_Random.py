# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P11_Random
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program demonstrates a common use case of the
#                      random library on the Pico
#
# Hardware Description: No special hardware is required.
#
# Created: August 23rd, 2024, 6:28 PM
# Last Updated: August 27th, 2024, 10:08 PM
# Modified from example code by Dogan Ibrahim

import random

strt = 'a'

while True:
    strt = input("Press ENTER to start, X to exit ")
    if strt.upper() != 'X':
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        print("%d  %d" % (first, second))
    else:
        break