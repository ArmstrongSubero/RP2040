# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: S25_Simple_Music_Player
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program plays simple music using a buzzer connected
#                      to the Raspberry Pi Pico. It generates different tones
#                      by varying the frequency of the PWM signal sent to the buzzer.
# 
# Hardware Description:
#    Buzzer connected to GPIO 15 via a PWM-capable pin.
# 
# Created: August 28th, 2024, 1:14 PM
# Last Updated: August 28th, 2024, 1:14 PM

from machine import Pin, PWM
import utime

# Define the buzzer pin
buzzer = PWM(Pin(15))

# Define a dictionary of notes and their frequencies in Hertz (Hz)
notes = {
    'C4': 261,
    'D4': 294,
    'E4': 329,
    'F4': 349,
    'G4': 392,
    'A4': 440,
    'B4': 493,
    'C5': 523
}

# Define the melody to play (sequence of notes)
melody = [
    ('C4', 0.5),
    ('D4', 0.5),
    ('E4', 0.5),
    ('F4', 0.5),
    ('G4', 0.5),
    ('A4', 0.5),
    ('B4', 0.5),
    ('C5', 0.5)
]

def play_tone(note, duration):
    # Set the frequency of the buzzer to the note's frequency
    buzzer.freq(notes[note])
    buzzer.duty_u16(32768)  # Set duty cycle to 50% (middle of 0-65535 range)
    utime.sleep(duration)   # Play the note for the specified duration
    buzzer.duty_u16(0)      # Turn off the buzzer
    utime.sleep(0.1)        # Short delay between notes

def play_melody(melody):
    # Play each note in the melody
    for note, duration in melody:
        play_tone(note, duration)

while True:
    # Play the melody
    play_melody(melody)
