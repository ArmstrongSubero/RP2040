# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S50_Range_Finder
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program uses an HC-SR04 ultrasonic distance sensor
#                      to measure the distance to an object and display it in centimeters.
#                      The sensor is powered with 5V, and a voltage divider is used to
#                      safely connect the Echo pin to the Raspberry Pi Pico's GPIO pin.
#                      The program triggers the sensor at a regular interval using a timer,
#                      and calculates the distance based on the time it takes for the ultrasonic
#                      pulse to return after hitting an object.
# 
# Hardware Description:
#    HC-SR04 Ultrasonic Distance Sensor:
#       - TRIG pin connected to GPIO 13
#       - ECHO pin connected to GPIO 12 (via a voltage divider)
#       - VCC pin connected to 5V
#       - GND pin connected to GND
# 
# Created: August 28th, 2024, 2:00 PM
# Last Updated: August 28th, 2024, 2:00 PM

from machine import Timer, Pin
import time

class Range_Finder:
    def __init__(self, trigger_pin, echo_pin):
        # Initialize the trigger and echo pins
        self.trig = Pin(trigger_pin, Pin.OUT, value=0)
        self.echo = Pin(echo_pin, Pin.IN)

        # Initialize pulse start time, duration, and a flag
        self.pulse_start = 0
        self.pulse_duration = 0
        self.flag = False

        # Create a timer to trigger the ultrasonic pulse periodically
        self.trigger_timer = Timer(freq=5, mode=Timer.PERIODIC, callback=self.trigger_isr)

        # Set up an interrupt for the echo pin to capture rising and falling edges
        self.echo.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=self.echo_isr)

    def echo_isr(self, pin):
        # Interrupt Service Routine for the echo pin
        if self.echo.value() == 1:  # Rising edge detected
            self.pulse_start = time.ticks_us()  # Record the start time
        else:  # Falling edge detected
            self.pulse_duration = time.ticks_diff(time.ticks_us(), self.pulse_start) 
            self.flag = True  # Set the flag indicating a measurement is ready

    def trigger_isr(self, t):
        # Timer callback function to trigger the ultrasonic pulse
        self.trig.value(1)
        time.sleep_us(10)  # Pulse the trigger for 10 microseconds
        self.trig.value(0)
        
    def distance(self):
        # Reset the flag
        self.flag = False

        # Calculate the distance based on pulse duration
        distance_cm = (self.pulse_duration / 2) * 0.0343  # Convert time to distance in cm

        # Filter out unrealistic readings
        if distance_cm < 2 or distance_cm > 400:  # HC-SR04 range is 2 cm to 400 cm
            return "Out of range"  # Return a message for out-of-range values

        return distance_cm

# Define trigger and echo pin numbers
TRIGGER = 13
ECHO = 12

# Create an instance of the Range_Finder class
range_finder = Range_Finder(TRIGGER, ECHO)

while True:
    while not range_finder.flag:  # Wait until a measurement is ready
        pass
    
    # Get and print the measured distance
    result = range_finder.distance()
    if isinstance(result, str):
        print(result)
    else:
        print("{:.1f} cm".format(result))

    time.sleep(0.5)  # Add a delay between readings
