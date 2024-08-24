# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S11_UART
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to use
#                      UART0
# 
# Hardware Description: An CP2012 USB-UART converter is connected to UART0
#                       
# Created: August 22nd, 2024, 10:40 PM
# Last Updated: August 22nd, 2024, 10:40 PM

from machine import UART
import utime

uart = UART(0, 9600)

temp = 0
while True:
    temp = temp + 1
    tempStr = str(temp)
    
    uart.write(tempStr)
    uart.write("\n")
    utime.sleep_ms(500)


