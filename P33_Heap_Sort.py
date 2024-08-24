# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P33_Heap_Sort
# Interpreter: MicroPython (latest version)
# Program Version: 1.3
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      demonstrate heap sort
#
# Notes:
# Time complexity of O(n log n) in the worst, best, and average cases
# Space complexity of O(1) because it is an in-place algorithm
# Efficient for large data sets but is not a stable sort
# Good for memory-constrained enviroments with guranteed performance 

def heapify(arr, n, i):
    # Assume the largest element is at the root
    largest = i
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # If the left child exists and is greater than the root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If the right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest element is not the root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected subtree

def heap_sort(arr):
    n = len(arr)

    # Build a maxheap from the array
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements from the heap
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the current root to the end
        heapify(arr, i, 0)  # Heapify the reduced heap

# Example array to be sorted
arr = [64, 34, 25, 12, 22, 11, 95]

# Call the heap sort function
heap_sort(arr)

# Print the sorted array
print("Sorted Array: ", arr)
