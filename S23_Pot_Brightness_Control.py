# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S23_Pot_Brightness_Control
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program reads the value from a potentiometer connected to
#                      an analog pin on the Raspberry Pi Pico. It adjusts the brightness
#                      of an LED connected to a PWM-capable pin based on the position
#                      of the potentiometer.
# 
# Hardware Description:
#    Potentiometer connected to ADC0 (GPIO 26) in a voltage divider configuration.
#    LED connected to GPIO 16 via a 1K resistor.
# 
# Created: August 28th, 2024, 12:34 PM
# Last Updated: August 28th, 2024, 12:34 PM

from machine import ADC, Pin, PWM
import utime

# Initialize the potentiometer on ADC0 (GPIO 26)
potentiometer = ADC(Pin(26))

# Initialize the LED on GPIO 16 with PWM
led = PWM(Pin(16))
led.freq(1000)  # Set the PWM frequency to 1 kHz

# Function to adjust LED brightness based on potentiometer position
def adjust_brightness():
    while True:
        # Read the potentiometer value (0-65535)
        pot_value = potentiometer.read_u16()
        
        # Convert the potentiometer value to a PWM duty cycle (0-65535)
        led.duty_u16(pot_value)
        
        # Print the potentiometer value and corresponding duty cycle for debugging
        print("Potentiometer Value:", pot_value, "Duty Cycle:", pot_value)
        
        # Sleep for a short time before reading again
        utime.sleep(0.1)

# Run the LED brightness control function
adjust_brightness()
