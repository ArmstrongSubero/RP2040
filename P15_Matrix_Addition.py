# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P15_Matrix_Addition
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program demonstrates matrix addition in Python.
#                      It adds two 3x3 matrices and outputs the result. The
#                      program uses nested loops to iterate through the
#                      matrices, element by element, performing the addition
#                      and storing the result in a new matrix. We get a
#                      taste for nested looping. 
#
# Hardware Description: No special hardware is required.
#
# Created: August 23rd, 2024, 6:35 PM
# Last Updated: August 27th, 2024, 10:15 PM

# matrix A
A = [[5, 4, 2],
     [6, 3, 1],
     [2, 8, 3]]

# matrix B
B = [[2, 4, 2],
     [0, 4, 10],
     [8, 2, 8]]

# result matrix
res = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]

# Matrix addition
for i in range(len(A)):
    for j in range(len(A[0])):
        res[i][j] = A[i][j] + B[i][j]

# Print the result
for i in res:
    print(i)
