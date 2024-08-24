# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P35_Quick_Sort
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      demonstrate quicksort
#
# Notes:
# Time complexity of O(n log n) on average, but O(n^2) in the worst case
# Space complexity of O(log n) due to recursive function calls (in-place sort)
# Not stable, meaning it does not necessarily preserve the relative order of equal elements
# Very efficient for large datasets and commonly used in practice
# Overall best for general sorting with arerage case performance

def partition(arr, low, high):
    # Select the pivot element, typically the last element in the array
    pivot = arr[high]
    i = low - 1  # Index of the smaller element

    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    # Swap the pivot element with the element at i+1 position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return the partitioning index

def quick_sort(arr, low, high):
    if low < high:
        # pi is the partitioning index, arr[pi] is now at the right place
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Example array to be sorted
arr = [64, 34, 25, 12, 22, 11, 99]

# Call the quicksort function
quick_sort(arr, 0, len(arr) - 1)

# Print the sorted array
print("Sorted Array: ", arr)
