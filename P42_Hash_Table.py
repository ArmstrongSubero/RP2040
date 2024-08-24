# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P42_HashTable
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      demonstrate a basic hash table implementation using Python arrays.
#
# Notes:
# This is a simplified implementation of a hash table using Python arrays.
# The hash table uses separate chaining to handle collisions.

import array

def array_remove(arr, value):
    new_arr = array.array('i', [0] * (len(arr) - 1))
    index_found = False
    j = 0
    for i in range(len(arr)):
        if arr[i] == value and not index_found:
            index_found = True
            continue
        new_arr[j] = arr[i]
        j += 1
    return new_arr


class HashTable:
    def __init__(self, size=10):
        # Initialize a hash table with an array of empty lists (separate chaining)
        self.size = size
        self.table = [array.array('i') for _ in range(self.size)]

    def hash_function(self, key):
        # Simple hash function: sum of the ASCII values of characters modulo the table size
        hash_value = sum(ord(char) for char in key) % self.size
        return hash_value

    def insert(self, key, value):
        # Insert key-value pair into the hash table
        index = self.hash_function(key)
        # Handle collision using separate chaining (append to the list at the index)
        self.table[index].append(value)
        print(f"Inserted key: {key} with value: {value} at index: {index}")

    def search(self, key):
        # Search for a value by key in the hash table
        index = self.hash_function(key)
        # Return all elements at the hash index (for simplicity, assuming no duplicates)
        if self.table[index]:
            return self.table[index]
        else:
            return None

    def delete(self, key, value):
        # Delete a key-value pair from the hash table
        index = self.hash_function(key)
        try:
            self.table[index].remove(value)
            print(f"Deleted key: {key} with value: {value} from index: {index}")
        except ValueError:
            print(f"Value {value} not found for key {key} in index {index}")

    def display(self):
        # Display the contents of the hash table
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {list(bucket)}")

# Example usage of the hash table
hash_table = HashTable()

# Insert key-value pairs
hash_table.insert("apple", 1)
hash_table.insert("banana", 2)
hash_table.insert("orange", 3)
hash_table.insert("grape", 4)

# Display the hash table
hash_table.display()

# Search for a value by key
search_result = hash_table.search("banana")
print(f"Search result for 'banana': {search_result}")

# Delete a key-value pair
hash_table.delete("orange", 3)

# Display the hash table after deletion
hash_table.display()

# Attempt to search for a deleted key
search_result = hash_table.search("orange")
print(f"Search result for 'orange': {search_result}")
