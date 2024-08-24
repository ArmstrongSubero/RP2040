# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P37_Bucket_Sort
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      demonstrate bucket sort
#
# Notes:
# Time complexity of O(n + k), where n is the number of elements and k is the number of buckets
# Space complexity of O(n + k), as it requires additional space for the buckets
# Stable sort when using a stable sort for individual buckets
# Particularly efficient for sorting floating-point numbers uniformly distributed across a range

def insertion_sort(arr):
    # Simple insertion sort used to sort individual buckets
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bucket_sort(arr):
    n = len(arr)
    if n == 0:
        return

    # Create empty buckets
    buckets = [[] for _ in range(n)]

    # Put array elements in different buckets
    for i in range(n):
        index = int(arr[i] * n)  # Assuming arr[i] is in the range [0, 1)
        buckets[index].append(arr[i])

    # Sort individual buckets and concatenate the results
    for i in range(n):
        insertion_sort(buckets[i])

    k = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1

# Example array to be sorted
arr = [0.897, 0.565, 0.656, 0.123, 0.665, 0.343]

# Call the bucket sort function
bucket_sort(arr)

# Print the sorted array
print("Sorted Array: ", arr)
