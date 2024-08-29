# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S19_Traffic_Light_Simulation
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program simulates a 4-way traffic light using
#                      LEDs connected to GPIO 16, 17, 18, 19, 20, and 21
#                      on the Raspberry Pi Pico.
#
#                      Turn on the North-South Green light and East-West Red light 
#                      for 5 seconds. Then, turn on the North-South Yellow light while
#                      keeping East-West Red on for 2 seconds. Both directions show 
#                      Red for 1 second (all stop). The East-West Green light turns on, 
#                      and the North-South Red light stays on for 5 seconds. The East-West 
#                      Yellow light turns on while keeping North-South Red on for 2 seconds.
#                      Finally, both directions show Red again for 1 second.
# 
# Hardware Description: 
#    North-South Red LED connected to GPIO 16
#    North-South Yellow LED connected to GPIO 17
#    North-South Green LED connected to GPIO 18
#    East-West Red LED connected to GPIO 19
#    East-West Yellow LED connected to GPIO 20
#    East-West Green LED connected to GPIO 21
#    Each LED should be connected to a 1K resistor
# 
# Created: August 28th, 2024, 12:04 AM
# Last Updated: August 28th, 2024, 12:04 AM

from machine import Pin
import utime

# Initialize the LEDs
ns_red_led = Pin(16, Pin.OUT)
ns_yellow_led = Pin(17, Pin.OUT)
ns_green_led = Pin(18, Pin.OUT)
ew_red_led = Pin(19, Pin.OUT)
ew_yellow_led = Pin(20, Pin.OUT)
ew_green_led = Pin(21, Pin.OUT)

# Function to simulate the 4-way traffic light sequence
def traffic_light():
    while True:
        # North-South Green, East-West Red
        ns_green_led.on()
        ew_red_led.on()
        utime.sleep(5)
        ns_green_led.off()
        
        # North-South Yellow, East-West Red
        ns_yellow_led.on()
        utime.sleep(2)
        ns_yellow_led.off()
        
        # North-South Red, East-West Red (all lights red)
        ns_red_led.on()
        utime.sleep(1)
        
        # North-South Red, East-West Green
        ew_green_led.on()
        ns_red_led.on()
        utime.sleep(5)
        ew_green_led.off()
        
        # North-South Red, East-West Yellow
        ew_yellow_led.on()
        utime.sleep(2)
        ew_yellow_led.off()
        
        # North-South Red, East-West Red (all lights red)
        utime.sleep(1)
        ns_red_led.off()
        ew_red_led.off()

# Run the 4-way traffic light simulation
traffic_light()
