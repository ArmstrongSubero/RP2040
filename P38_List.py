# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P38_List
# Interpreter: MicroPython (latest version)
# Program Version: 1.1
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      demonstrate various operations on Python lists.
#
# Notes:
# Python lists are versatile, mutable, and ordered collections of items.
# They can store elements of different data types and can be modified after creation.
# Lists are a fundamental data structure in Python.

# 1. Creating a List
# Creating a list of integers
numbers = [1, 2, 3, 4, 5]

# Creating a list of strings
fruits = ["apple", "banana", "cherry"]

# Creating a mixed list with different data types
mixed_list = [1, "apple", 3.14, True]

# 2. Accessing Elements
# Accessing elements by index
print(numbers[0])  # Output: 1
print(fruits[1])   # Output: banana

# Accessing the last element using negative indexing
print(numbers[-1])  # Output: 5
print(fruits[-2])   # Output: banana

# 3. Modifying Elements
# Modifying elements by index
numbers[0] = 10
print(numbers)  # Output: [10, 2, 3, 4, 5]

# 4. Adding Elements
# Appending an element to the end of the list
numbers.append(6)
print(numbers)  # Output: [10, 2, 3, 4, 5, 6]

# Inserting an element at a specific position
numbers.insert(1, 15)
print(numbers)  # Output: [10, 15, 2, 3, 4, 5, 6]

# Extending the list by another list
numbers.extend([7, 8, 9])
print(numbers)  # Output: [10, 15, 2, 3, 4, 5, 6, 7, 8, 9]

# 5. Removing Elements
# Removing a specific element by value
numbers.remove(15)
print(numbers)  # Output: [10, 2, 3, 4, 5, 6, 7, 8, 9]

# Removing an element by index using pop()
numbers.pop(0)
print(numbers)  # Output: [2, 3, 4, 5, 6, 7, 8, 9]

# Removing an element by index using del
del numbers[1]
print(numbers)  # Output: [2, 4, 5, 6, 7, 8, 9]

# 6. Slicing a List
# Slicing from index 1 to 4 (excluding 4)
sublist = numbers[1:4]
print(sublist)  # Output: [4, 5, 6]

# Slicing with a step
sublist_with_step = numbers[::2]
print(sublist_with_step)  # Output: [2, 5, 7, 9]

# 7. Looping Through a List
# Looping through a list using a for loop
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry

# 8. List Comprehension
# Creating a list of squares using list comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

# Creating a list of even numbers using list comprehension
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

# 9. Common List Methods
# Length of the list
print("Length of numbers list:", len(numbers))  # Output: 7

# Append: Adding an element to the end of the list
numbers.append(10)
print("After append:", numbers)  # Output: [2, 4, 5, 6, 7, 8, 9, 10]

# Insert: Inserting an element at a specific position
numbers.insert(3, 11)
print("After insert:", numbers)  # Output: [2, 4, 5, 11, 6, 7, 8, 9, 10]

# Remove: Removing the first occurrence of an element
numbers.remove(11)
print("After remove:", numbers)  # Output: [2, 4, 5, 6, 7, 8, 9, 10]

# Pop: Removing and returning an element from a specific index (default is the last element)
popped_element = numbers.pop()
print("Popped element:", popped_element)  # Output: 10
print("After pop:", numbers)  # Output: [2, 4, 5, 6, 7, 8, 9]

# Index: Finding the index of the first occurrence of an element
index_of_7 = numbers.index(7)
print("Index of 7:", index_of_7)  # Output: 4

# Count: Counting the number of occurrences of an element
count_of_4 = numbers.count(4)
print("Count of 4:", count_of_4)  # Output: 1

# Sort: Sorting the list in ascending order
numbers.sort()
print("Sorted numbers list:", numbers)  # Output: [2, 4, 5, 6, 7, 8, 9]

# Reverse: Reversing the elements of the list
numbers.reverse()
print("Reversed numbers list:", numbers)  # Output: [9, 8, 7, 6, 5, 4, 2]

# Copy: Creating a shallow copy of the list
numbers_copy = numbers.copy()
print("Copy of numbers list:", numbers_copy)  # Output: [9, 8, 7, 6, 5, 4, 2]

# Clear: Removing all elements from the list
numbers.clear()
print("After clear:", numbers)  # Output: []

# 10. Example: Using Lists in a Program
# Create a list of student names
students = ["Alice", "Bob", "Charlie", "David"]

# Add a new student
students.append("Eve")

# Sort the list
students.sort()

# Print the sorted list
print("Sorted students:", students)
# Output: Sorted students: ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
