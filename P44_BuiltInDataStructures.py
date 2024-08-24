# File: main.py
# Author: Armstrong Subero
# Platform: Python (Standard or MicroPython with limited capabilities)
# Program: P44_BuiltInDataStructures
# Interpreter: Python 3.x / MicroPython
# Program Version: 1.0
#
# Program Description: This program demonstrates various built-in data structures in Python,
#                      including lists, tuples, sets, dictionaries, strings, bytearray, bytes,
#                      range, frozenset, deque, namedtuple, defaultdict, Counter, and OrderedDict.
#
# Notes:
# Each section of the program includes a description of the data structure, use cases,
# and a short example of how to use it in Python.

from collections import deque, namedtuple, OrderedDict

# 1. List
# Description: An ordered collection of elements that can hold items of different types. Lists are mutable.
# Use Cases: Storing sequences of items, managing queues or stacks.
my_list = [1, 2, 3, "apple", True]
my_list.append("banana")
print("List Example:", my_list)  # Output: [1, 2, 3, 'apple', True, 'banana']

# 2. Tuple
# Description: Similar to a list but immutable. Tuples are used to group related data.
# Use Cases: Storing fixed collections, returning multiple values from a function.
my_tuple = (1, 2, 3, "apple", True)
print("Tuple Example:", my_tuple)  # Output: (1, 2, 3, 'apple', True)

# 3. Set
# Description: An unordered collection of unique elements. Sets are mutable and do not allow duplicates.
# Use Cases: Removing duplicates, performing set operations, membership testing.
my_set = {1, 2, 3, "apple"}
my_set.add("banana")
print("Set Example:", my_set)  # Output: {1, 2, 3, 'banana', 'apple'}

# 4. Dictionary
# Description: An unordered collection of key-value pairs. Keys must be unique and immutable.
# Use Cases: Storing and retrieving data by key, managing configurations.
my_dict = {"apple": 1, "banana": 2, "orange": 3}
my_dict["grape"] = 4
print("Dictionary Example:", my_dict)  # Output: {'apple': 1, 'banana': 2, 'orange': 3, 'grape': 4}

# 5. String
# Description: An immutable sequence of characters used to represent text.
# Use Cases: Storing and manipulating text, formatting output.
my_string = "Hello, World!"
print("String Example:", my_string)  # Output: Hello, World!

# 6. Bytearray
# Description: A mutable sequence of bytes. Useful for working with binary data.
# Use Cases: Working with binary data, modifying bytes in place.
my_bytearray = bytearray("ABC", "utf-8")
my_bytearray[0] = 68  # 'D'
print("Bytearray Example:", my_bytearray)  # Output: bytearray(b'DBC')

# 7. Bytes
# Description: An immutable sequence of bytes. Often used for binary data like images or files.
# Use Cases: Handling raw binary data, network protocols.
my_bytes = b"Hello"
print("Bytes Example:", my_bytes)  # Output: b'Hello'

# 8. Range
# Description: An immutable sequence of numbers, typically used for looping.
# Use Cases: Iterating over a sequence of numbers.
my_range = range(1, 10, 2)
print("Range Example:", list(my_range))  # Output: [1, 3, 5, 7, 9]

# 9. Frozenset
# Description: An immutable version of a set.
# Use Cases: Working with sets that should not change, using sets as keys in dictionaries.
my_frozenset = frozenset([1, 2, 3, "apple"])
print("Frozenset Example:", my_frozenset)  # Output: frozenset({1, 2, 3, 'apple'})

# 10. Namedtuple (from collections module)
# Description: A subclass of tuples with named fields.
# Use Cases: Storing related data with meaningful names, making code more readable.
Point = namedtuple("Point", "x y")
p = Point(1, 2)
print("Namedtuple Example:", p)  # Output: Point(x=1, y=2)

# 11. OrderedDict (from collections module)
# Description: A dictionary that maintains the order of keys based on insertion order.
# Use Cases: Maintaining insertion order, structured output, LRU caches.
my_ordered_dict = OrderedDict()
my_ordered_dict["apple"] = 1
my_ordered_dict["banana"] = 2
my_ordered_dict["orange"] = 3
print("OrderedDict Example:", my_ordered_dict)  # Output: OrderedDict([('apple', 1), ('banana', 2), ('orange', 3)])
