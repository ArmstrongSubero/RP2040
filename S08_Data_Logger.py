# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S08_DataLogger
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to read
#                      ADC values and store them in a text file onboard
#                      the device 
# 
# Hardware Description: A potentiometer is connected to ADC Channel0
#                       
# Created: August 22nd, 2024, 10:13 PM
# Last Updated: August 22nd, 2024, 10:13 PM

from machine import ADC
import utime

AnalogIn = ADC(0)
Conv = 3300 / 65535

file = open("Temp.txt", "w")
file.write("Ambient Temperature\n")

for secs in range(30):
    V = AnalogIn.read_u16()
    mV = V * Conv
    Temp = (mV - 500.0) / 10.0
    Tempstr = str(Temp)[:5]
    data = str(secs+1) + "   " + Tempstr + "\n"
    file.write(data)
    utime.sleep(1)

file.close()
print("Data has been written to file...")