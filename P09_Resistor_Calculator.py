# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P09_Resistor Calculator
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program calculates the total resistance of 
#                      multiple resistors either in series or parallel. 
#                      It prompts the user to input the number of resistors
#                      and whether they are connected in series or parallel.
#                      Based on the input, the program computes and displays
#                      the total resistance.
#
# Hardware Description: No special hardware is required.
#
# Created: August 23rd, 2024, 6:25 PM
# Last Updated: August 27th, 2024, 10:06 PM
# Modified from example code by Dogan Ibrahim

print("RESISTORS IN SERIES OR PARALLEL")
print("===============================")
yn = "y"
while yn == 'y':
    N = int(input("\nHow many resistors are there?: "))
    mode = input("Are the resistors series (s) or parallel (p)?: ")
    mode = mode.lower()
    
    # read resistor values and calculate total
    resistor = 0.0

    if mode == 's':
        for n in range(0, N):
            s = "Enter resistor " + str(n+1) + " value in Ohms: "
            r = int(input(s))
            resistor = resistor + r
        print("Total resistance = %d Ohms" % (resistor))
    elif mode == 'p':
        for n in range (0, N):
            s = "Enter resistor " + str(n + 1) + " value in Ohms: "
            r = float(input(s))
            resistor = resistor + 1/r
        print("Total resistance = %.3f Ohms" % (1 / resistor))
    
    # check if user wants to exit
    yn = input("\nDo you want to continue?: ")
    yn = yn.lower()
    