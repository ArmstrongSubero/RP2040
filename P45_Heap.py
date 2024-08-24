# File: main.py
# Author: Armstrong Subero
# Platform: Python (Standard or MicroPython with limited capabilities)
# Program: P45_Heap_Custom
# Interpreter: Python 3.x / MicroPython
# Program Version: 1.1
#
# Program Description: This program demonstrates the use of heaps in Python
#                      with custom implementations for finding the smallest and largest elements.
#
# Notes:
# Custom implementations are provided for finding the smallest and largest elements
# in environments where heapq's nsmallest and nlargest are unavailable.

import heapq

# 1. Creating a Heap
numbers = [20, 5, 15, 22, 30, 10, 25]
heapq.heapify(numbers)
print("Heap Example (after heapify):", numbers)
# Output: Heap Example (after heapify): [5, 20, 10, 22, 30, 15, 25]

# 2. Adding Elements to the Heap
heapq.heappush(numbers, 3)
print("Heap Example (after heappush):", numbers)
# Output: Heap Example (after heappush): [3, 5, 10, 20, 30, 15, 25, 22]

# 3. Removing the Smallest Element
smallest = heapq.heappop(numbers)
print("Popped Smallest Element:", smallest)
print("Heap Example (after heappop):", numbers)
# Output: Popped Smallest Element: 3
# Output: Heap Example (after heappop): [5, 20, 10, 22, 30, 15, 25]

# 4. Peek at the Smallest Element
smallest_peek = numbers[0]
print("Peek Smallest Element:", smallest_peek)
# Output: Peek Smallest Element: 5

# 5. Custom Implementation to Find the 3 Smallest Elements
def find_n_smallest(heap, n):
    # Make a copy of the heap so we don't modify the original
    heap_copy = list(heap)
    heapq.heapify(heap_copy)
    smallest_elements = [heapq.heappop(heap_copy) for _ in range(min(n, len(heap_copy)))]
    return smallest_elements

three_smallest = find_n_smallest(numbers, 3)
print("Three Smallest Elements:", three_smallest)
# Output: Three Smallest Elements: [5, 10, 15]

# 6. Custom Implementation to Find the 3 Largest Elements
def find_n_largest(heap, n):
    # Sort the heap and return the last n elements
    sorted_heap = sorted(heap, reverse=True)
    return sorted_heap[:n]

three_largest = find_n_largest(numbers, 3)
print("Three Largest Elements:", three_largest)
# Output: Three Largest Elements: [30, 25, 22]

# 7. Converting a Min-Heap to a Max-Heap
max_heap = [-x for x in numbers]
heapq.heapify(max_heap)
print("Max-Heap Example (simulated with negative values):", max_heap)
largest = -heapq.heappop(max_heap)
print("Popped Largest Element:", largest)
# Output: Popped Largest Element: 30
