# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S09_PWM
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to use
#                      Pulse Width Modulation (PWM) produces a 1kHz waveform
#                      at 50% duty cycle 
# 
# Hardware Description: An oscilloscope probe is connected to PIN21 (GPIO16)
#                       
# Created: August 22nd, 2024, 10:23 PM
# Last Updated: August 22nd, 2024, 10:23 PM

from machine import Pin, PWM

ch = PWM(Pin(16))
ch.freq(1000)
ch.duty_u16(32767)

while True:
    pass