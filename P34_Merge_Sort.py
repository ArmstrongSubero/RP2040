# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P34_Merge_Sort
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      demonstrate merge sort
#
# Notes:
# Time complexity of O(n log n) in the worst, best, and average cases
# Space complexity of O(n) because it requires extra space for the temporary arrays
# Stable sort, meaning it preserves the relative order of equal elements
# Efficient for large data sets but requires additional memory space
# Excellent for sorting linked lists and external sorting where data dosen't
# fit into memory

def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle point and divide the array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort the two halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0

        # Copy data to the temp arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left in left_half[]
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Checking if any element was left in right_half[]
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example array to be sorted
arr = [64, 34, 25, 12, 22, 11, 98]

# Call the merge sort function
merge_sort(arr)

# Print the sorted array
print("Sorted Array: ", arr)
