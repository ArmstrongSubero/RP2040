# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S22_Light_Dependent_Resistor
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program reads the value from a Light Dependent Resistor (LDR)
#                      connected to an analog pin on the Raspberry Pi Pico. It turns an LED
#                      on or off based on the light intensity detected by the LDR.
# 
# Hardware Description:
#    LDR connected to ADC0 (GPIO 26) in a voltage divider configuration with a resistor.
#    LED connected to GPIO 16 via a 1K resistor.
# 
# Created: August 28th, 2024, 12:22 PM
# Last Updated: August 28th, 2024, 12:22 PM

from machine import ADC, Pin
import utime

# Initialize the LDR on ADC0 (GPIO 26)
ldr = ADC(Pin(26))

# Initialize the LED on GPIO 16
led = Pin(16, Pin.OUT)

# Set a threshold value for light intensity (adjust this value based on your setup)
threshold = 20000

# Function to read the LDR value and control the LED
def control_led():
    while True:
        # Read the LDR value (0-65535)
        light_value = ldr.read_u16()
        
        # Print the light value for debugging
        print("Light Value:", light_value)
        
        # Turn the LED on if the light intensity is below the threshold
        if light_value < threshold:
            led.on()
        else:
            led.off()
        
        # Sleep for a short time before reading again
        utime.sleep(0.5)

# Run the LED control function
control_led()
