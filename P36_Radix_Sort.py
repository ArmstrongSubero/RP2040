# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P36_Radix_Sort
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      demonstrate radix sort
#
# Notes:
# Time complexity of O(nk), where n is the number of elements and k is the number of digits in the largest number
# Space complexity of O(n + k), as it requires extra space for the counting sort used in each digit pass
# Stable sort, meaning it preserves the relative order of equal elements
# Efficient for sorting large numbers of integers or fixed-length strings with a limited range of values
# Dates in YYYYMMDD for example

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # Output array to store sorted elements
    count = [0] * 10  # Initialize count array with zeros for base 10

    # Store count of occurrences in count[]
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Change count[i] so that it contains the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the output array to arr[], so that arr[] contains sorted numbers according to the current digit
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Find the maximum number to determine the number of digits
    max_val = max(arr)

    # Do counting sort for every digit. exp is 10^i where i is the current digit number
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Example array to be sorted
arr = [170, 45, 75, 90, 802, 24, 2, 66]

# Call the radix sort function
radix_sort(arr)

# Print the sorted array
print("Sorted Array: ", arr)
