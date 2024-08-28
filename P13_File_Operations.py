# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P13_File_Operations
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program shows us file operations
#                      in Python. A common operation needed on the Pico
#                      we create a file, add some content then display
#                      the contents. (Trap for beginners, remember these
#                      programs are being run on the Pico, the file will
#                      be created on the Pico)
#
# Hardware Description: No special hardware is required.
#
# Created: August 23rd, 2024, 6:30 PM
# Last Updated: August 27th, 2024, 10:13 PM
# Modified from example code by Dogan Ibrahim
import os

# create file
print("Current Directory:", os.getcwd())
print("Opening file")
fp = open("MyFile.txt", "w")
fp.write("Hello")
fp.close()
print("Closing file")

# read created file
print("Open the file and read its contents")
fp = open("MyFile.txt", "r")
str = fp.read(80)
fp.close()
print(str)