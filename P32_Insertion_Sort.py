# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P30_Insertion_Sort
# Interpreter: MicroPython (latest version)
# Program Version: 1.2
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      demonstrate insertion sort
#
# Notes:
# Time complexity of O(n^2) in the worst case and O(n) in the best case
# Space complexity of O(1) because it requires constant space
# Efficient for small data sets and partially sorted arrays
# Preferred over selection sort for stability 

def insertion_sort(arr):
    n = len(arr)
    # Start from the second element as the first element is trivially sorted
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1] that are greater than key to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Place the key in its correct location
        arr[j + 1] = key

# Example array to be sorted
arr = [64, 34, 25, 12, 22, 11, 90]

# Call the insertion sort function
insertion_sort(arr)

# Print the sorted array
print("Sorted Array: ", arr)
