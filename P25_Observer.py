# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P25_Observer
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program demonstrates the Observer design pattern by
#                      allowing different display elements to be updated when 
#                      a data source (subject) changes. Useful for implementing
#                      distributed event-handling systems. Essentially a one to many
#                      dependency between objects
# 
# Hardware Description: No hardware required for this example.
#                       
# Created: August 25th, 2024, 12:05 AM
# Last Updated: August 25th, 2024, 12:05 AM

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        for observer in self._observers:
            observer.update(self)

class DataSource(Subject):
    def __init__(self):
        super().__init__()
        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()

class Display:
    def update(self, subject):
        print(f"Display updated with new data: {subject.data}")

# Usage
data_source = DataSource()
display1 = Display()
display2 = Display()

data_source.attach(display1)
data_source.attach(display2)

data_source.data = 42  # This will trigger the update in all attached observers
