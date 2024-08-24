# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P28_Command_Pattern
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program demonstrates the Command design pattern by
#                      creating a set of commands that can be executed on an LED.
#                      The pattern encapsulates requests as objects, allowing for
#                      parameterization and queuing of requests. It also maintains
#                      a history of executed commands, enabling potential undo functionality.
# 
# Hardware Description: An LED is connected to pin 16.
#                       
# Created: August 25th, 2024, 12:15 AM
# Last Updated: August 25th, 2024, 12:15 AM

from machine import Pin
import utime

# Receiver: LED class
class LED:
    def __init__(self, pin_number):
        self.led = Pin(pin_number, Pin.OUT)

    def on(self):
        self.led.value(1)
        print("LED is ON")

    def off(self):
        self.led.value(0)
        print("LED is OFF")

# Command interface
class Command:
    def execute(self):
        pass

    def undo(self):
        pass

# Concrete command classes
class LEDOnCommand(Command):
    def __init__(self, led):
        self.led = led

    def execute(self):
        self.led.on()

    def undo(self):
        self.led.off()

class LEDOffCommand(Command):
    def __init__(self, led):
        self.led = led

    def execute(self):
        self.led.off()

    def undo(self):
        self.led.on()

# Invoker: Remote control that executes commands and keeps a history
class RemoteControl:
    def __init__(self):
        self.history = []

    def submit(self, command):
        command.execute()
        self.history.append(command)

    def undo_last(self):
        if self.history:
            last_command = self.history.pop()
            last_command.undo()
        else:
            print("No commands to undo")

# Usage
led = LED(16)
remote = RemoteControl()

on_command = LEDOnCommand(led)
off_command = LEDOffCommand(led)

# Turn the LED on and off using the remote control
remote.submit(on_command)
utime.sleep(1)
remote.submit(off_command)
utime.sleep(1)

# Undo the last command (turns the LED back on)
remote.undo_last()
