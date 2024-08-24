# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P43_Dictionary
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      demonstrate the usage of dictionaries in MicroPython.
#
# Notes:
# This program shows how to use dictionaries in MicroPython to store and retrieve key-value pairs.

# 1. Creating a Dictionary
my_dict = {
    "apple": 1,
    "banana": 2,
    "orange": 3
}

# 2. Accessing Elements
print("Apple quantity:", my_dict["apple"])  # Output: Apple quantity: 1

# 3. Modifying Elements
my_dict["apple"] = 10
print("Updated apple quantity:", my_dict["apple"])  # Output: Updated apple quantity: 10

# 4. Adding New Elements
my_dict["grape"] = 4
print("Grape quantity:", my_dict["grape"])  # Output: Grape quantity: 4

# 5. Removing Elements
del my_dict["banana"]
print("After removing banana:", my_dict)  # Output: After removing banana: {'apple': 10, 'orange': 3, 'grape': 4}

# 6. Checking for Key Existence
if "orange" in my_dict:
    print("Orange is in the dictionary")  # Output: Orange is in the dictionary

# 7. Iterating Over Dictionary Keys
print("Keys in dictionary:")
for key in my_dict:
    print(key)
# Output:
# Keys in dictionary:
# apple
# orange
# grape

# 8. Iterating Over Dictionary Values
print("Values in dictionary:")
for value in my_dict.values():
    print(value)
# Output:
# Values in dictionary:
# 10
# 3
# 4

# 9. Iterating Over Key-Value Pairs
print("Key-Value pairs in dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# Key-Value pairs in dictionary:
# apple: 10
# orange: 3
# grape: 4

# 10. Clearing the Dictionary
my_dict.clear()
print("Dictionary after clearing:", my_dict)  # Output: Dictionary after clearing: {}

# 11. Deleting the Dictionary
del my_dict
# print(my_dict)  # Uncommenting this will raise a NameError because the dictionary no longer exists
