# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P40_Stack
# Interpreter: MicroPython (latest version)
# Program Version: 1.7
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      demonstrate stack operations using Python arrays.
#
# Notes:
# This program implements a stack data structure using Python arrays.
# The stack follows the Last-In-First-Out (LIFO) principle.

import array

class Stack:
    def __init__(self):
        # Initialize an empty array with typecode 'i' for integers
        self.stack = array.array('i')

    def push(self, value):
        # Push an element onto the stack (equivalent to append)
        self.stack.append(value)
        print(f"Pushed {value} to stack")

    def pop(self):
        # Pop the top element from the stack
        if len(self.stack) == 0:
            raise IndexError("pop from empty stack")
        popped_value, self.stack = array_pop(self.stack)
        print(f"Popped {popped_value} from stack")
        return popped_value

    def peek(self):
        # Return the top element without removing it
        if len(self.stack) == 0:
            raise IndexError("peek from empty stack")
        return self.stack[-1]

    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0

    def size(self):
        # Return the size of the stack
        return len(self.stack)

    def display(self):
        # Display the stack elements
        print("Stack:", self.stack)

# Custom function to mimic the pop operation
def array_pop(arr, index=-1):
    if len(arr) == 0:
        raise IndexError("pop from empty array")
    if index < 0:
        index += len(arr)
    if index < 0 or index >= len(arr):
        raise IndexError("pop index out of range")
    
    popped_value = arr[index]
    new_arr = array.array('i', [0] * (len(arr) - 1))
    
    for i in range(index):
        new_arr[i] = arr[i]
    
    for i in range(index + 1, len(arr)):
        new_arr[i - 1] = arr[i]
    
    return popped_value, new_arr

# Example usage of the stack
stack = Stack()

# Push elements onto the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Display the stack
stack.display()  # Output: Stack: array('i', [10, 20, 30])

# Peek at the top element
top_element = stack.peek()
print(f"Top element: {top_element}")  # Output: Top element: 30

# Pop elements from the stack
stack.pop()  # Output: Popped 30 from stack
stack.pop()  # Output: Popped 20 from stack

# Display the stack after popping elements
stack.display()  # Output: Stack: array('i', [10])

# Check if the stack is empty
is_empty = stack.is_empty()
print(f"Is the stack empty? {is_empty}")  # Output: Is the stack empty? False

# Get the size of the stack
stack_size = stack.size()
print(f"Stack size: {stack_size}")  # Output: Stack size: 1

# Pop the last element
stack.pop()  # Output: Popped 10 from stack

# Try to pop from an empty stack (this will raise an error)
# stack.pop()  # Uncommenting this will raise IndexError: pop from empty stack

# Check if the stack is empty after popping all elements
is_empty = stack.is_empty()
print(f"Is the stack empty? {is_empty}")  # Output: Is the stack empty? True
