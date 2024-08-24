# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P23_Aggregation
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program demonstrates aggregation by creating
#                      a 'Battery' class and a 'RemoteControl' class that 
#                      uses a Battery instance to control power functions,
#                      including simulating a draining battery.
#                      Aggregation is a form of association where one class
#                      is a part of another class but can exist independently.
# 
# Hardware Description: No hardware required for this example.
#                       
# Created: August 24th, 2024, 11:45 PM
# Last Updated: August 24th, 2024, 11:45 PM

class Battery:
    def __init__(self, level):
        self.level = level
    
    def charge(self):
        print("Charging battery...")
        self.level = 100  # Fully charge the battery
        print("Battery fully charged.")

    def drain(self, amount):
        self.level -= amount
        if self.level < 0:
            self.level = 0
        print(f"Battery level: {self.level}%")

class RemoteControl:
    def __init__(self, battery):
        self.battery = battery
    
    def press_power_button(self):
        if self.battery.level > 0:
            print("Powering on device...")
            self.battery.drain(10)  # Drains the battery by 10% each time the button is pressed
        else:
            print("Battery is dead! Please recharge.")

# Usage example
battery = Battery(50)  # Create a Battery object with an initial charge level of 50
remote = RemoteControl(battery)  # Create a RemoteControl object using the Battery object

# Simulate using the remote control until the battery drains
for _ in range(6):  # Press the power button multiple times to drain the battery
    remote.press_power_button()

# Recharge the battery and use the remote again
battery.charge()
remote.press_power_button()
