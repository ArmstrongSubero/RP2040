# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P51_LRU_Cache
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program demonstrates the LRU (Least Recently Used)
#                      caching pattern in a memory-constrained environment like
#                      the Raspberry Pi Pico. The LRU cache stores a fixed number
#                      of items and evicts the least recently used item when the cache
#                      reaches its capacity.
# 
# Hardware Description: No hardware required for this example.
#                       
# Created: August 25th, 2024, 1:00 AM
# Last Updated: August 25th, 2024, 1:00 AM

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value  # Move to end to indicate it was recently used
            print(f"Cache hit: {key} -> {value}")
            return value
        else:
            print(f"Cache miss: {key}")
            return -1  # Indicates a cache miss

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            # Manually pop the first item to simulate `last=False` behavior
            first_key = next(iter(self.cache))
            self.cache.pop(first_key)
        self.cache[key] = value


# Usage example
cache = LRUCache(3)  # Create an LRU cache with a capacity of 3 items

# Add some items to the cache
cache.put(1, 'A')
cache.put(2, 'B')
cache.put(3, 'C')

# Access some items
cache.get(1)  # Accessing item 1 should make it most recently used
cache.get(4)  # This will be a cache miss

# Add a new item, causing the least recently used (key 2) to be evicted
cache.put(4, 'D')

# At this point, the cache contains keys 1, 3, and 4
cache.get(2)  # Accessing item 2 should show a cache miss since it was evicted
