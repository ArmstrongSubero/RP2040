# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P24_Singleton
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program demonstrates the Singleton design pattern by
#                      creating a single instance of a configuration class that can
#                      be accessed globally.
# 
# Hardware Description: No hardware required for this example.
#                       
# Created: August 24th, 2024, 11:55 PM
# Last Updated: August 24th, 2024, 11:55 PM

class Configuration:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Configuration, cls).__new__(cls)
            cls._instance.settings = {}
        return cls._instance
    
    def set(self, key, value):
        self.settings[key] = value
    
    def get(self, key):
        return self.settings.get(key, None)

# Usage
config1 = Configuration()
config2 = Configuration()

config1.set('volume', 70)
print(config2.get('volume'))  # Outputs: 70, showing that config1 and config2 are the same instance
