# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P61_Lazy_Loading
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program demonstrates the Lazy Loading pattern, where
#                      the initialization of a resource-intensive object is deferred
#                      until it is actually needed. This is useful for optimizing
#                      memory and performance in a resource-constrained environment.
# 
# Hardware Description: No hardware required for this example.
#                       
# Created: August 25th, 2024, 1:15 AM
# Last Updated: August 25th, 2024, 1:15 AM

import utime

class ExpensiveResource:
    def __init__(self):
        # Simulate an expensive operation (e.g., sensor initialization, file read)
        utime.sleep(2)  # Simulating delay
        self.data = "Expensive Data Loaded"
        print("ExpensiveResource initialized")

    def get_data(self):
        return self.data

class LazyLoader:
    def __init__(self):
        self._resource = None

    def get_resource(self):
        if self._resource is None:
            print("Lazy loading resource...")
            self._resource = ExpensiveResource()
        else:
            print("Resource already loaded")
        return self._resource

# Usage example
loader = LazyLoader()

# The resource is not loaded until it's actually needed
print("Accessing resource for the first time:")
resource = loader.get_resource()  # Resource is loaded here
print(resource.get_data())

print("\nAccessing resource again:")
resource = loader.get_resource()  # Resource is already loaded, no reinitialization
print(resource.get_data())
