# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S03_Timer
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to blink
#                      an LED faster or slower using external interrupts with
#                      pushubttons
# 
# Hardware Description: An LED is connected through a 1k resistor to GP6 and two
#                       pushbuttons are connected to GP14 and GP15 
#                       
# Created: August 22nd, 2024, 8:09 PM
# Last Updated: August 22nd, 2024, 8:09 PM

from machine import Pin
import utime

LED = Pin(6, Pin.OUT)

Faster = Pin(14, Pin.IN)
Slower = Pin(15, Pin.IN)

# default delay
dly = 1.0

# Faster ISR
def Flash_Faster(Faster):
    global dly
    dly = dly - 0.1


# Slower ISR
def Flash_Slower(Slower):
    global dly
    dly = dly + 0.1

# configure external interrupts
Faster.irq(handler = Flash_Faster, trigger = Faster.IRQ_FALLING)
Slower.irq(handler = Flash_Slower, trigger = Slower.IRQ_FALLING)

# main loop
while True:
    LED.value(1)
    utime.sleep(dly)
    LED.value(0)
    utime.sleep(dly)