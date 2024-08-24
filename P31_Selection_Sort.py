# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P31_Selection_Sort
# Interpreter: MicroPython (latest version)
# Program Version: 1.1
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      demonstrate selection sort
#
# Notes:
# Time complexity of O(n^2) for both worst and best cases
# Space complexity of O(1) because it requires constant space
# Inefficient on large data sets, but performs fewer swaps than bubble sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the first element of the unsorted part is the smallest
        min_idx = i
        for j in range(i+1, n):
            # Find the smallest element in the unsorted part
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Example array to be sorted
arr = [64, 34, 25, 12, 22, 11, 90]

# Call the selection sort function
selection_sort(arr)

# Print the sorted array
print("Sorted Array: ", arr)
