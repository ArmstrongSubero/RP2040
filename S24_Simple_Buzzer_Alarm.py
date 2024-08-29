# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S24_Simple_Buzzer_Alarm_System
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program creates a simple buzzer alarm system. 
#                      The alarm is triggered when a digital input is activated,
#                      causing the buzzer to sound. We use a pushbutton here,
#                      but feel free to use any type of input device. Here a
#                      pushbutton is connected with an external pull-up resistor.
# 
# Hardware Description:
#    Buzzer connected to GPIO 15.
#    Pushbutton connected to GPIO 14 with an external 10k pull-up resistor.
# 
# Created: August 28th, 2024, 12:53 PM
# Last Updated: August 28th, 2024, 12:53 PM

from machine import Pin, PWM
import utime

# Initialize the trigger input on GPIO 14 with no internal pull (since external pull-up is used)
trigger = Pin(14, Pin.IN)

# Initialize the buzzer on GPIO 15 with PWM
buzzer = PWM(Pin(15))
buzzer.freq(1000)  # Set the frequency to 1 kHz (you can adjust this for different tones)

# Function to sound the buzzer
def sound_buzzer(duration):
    buzzer.duty_u16(32768)  # Set duty cycle to 50% (32768 out of 65535)
    utime.sleep(duration)
    buzzer.duty_u16(0)  # Turn off the buzzer

# Main loop to monitor the trigger and sound the alarm
def alarm_system():
    while True:
        # Check if the trigger input is activated (button pressed)
        if trigger.value() == 0:  # Active low due to external pull-up
            print("Alarm Triggered!")
            sound_buzzer(1)  # Sound the buzzer for 1 second
        else:
            buzzer.duty_u16(0)  # Ensure the buzzer is off if the trigger is not active

        # Short delay to avoid excessive polling
        utime.sleep(0.1)

# Run the alarm system
alarm_system()
