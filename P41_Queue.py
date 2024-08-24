# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P41_Queue
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program allows the Raspberry Pi Pico to
#                      demonstrate queue operations using Python arrays.
#
# Notes:
# This program implements a queue data structure using Python arrays.
# The queue follows the First-In-First-Out (FIFO) principle.

import array

class Queue:
    def __init__(self):
        # Initialize an empty array with typecode 'i' for integers
        self.queue = array.array('i')

    def enqueue(self, value):
        # Enqueue (add) an element to the end of the queue
        self.queue.append(value)
        print(f"Enqueued {value} to queue")

    def dequeue(self):
        # Dequeue (remove) the front element from the queue
        if len(self.queue) == 0:
            raise IndexError("dequeue from empty queue")
        dequeued_value, self.queue = array_pop(self.queue, 0)
        print(f"Dequeued {dequeued_value} from queue")
        return dequeued_value

    def front(self):
        # Return the front element without removing it
        if len(self.queue) == 0:
            raise IndexError("front from empty queue")
        return self.queue[0]

    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0

    def size(self):
        # Return the size of the queue
        return len(self.queue)

    def display(self):
        # Display the queue elements
        print("Queue:", self.queue)

# Custom function to mimic the pop operation
def array_pop(arr, index=-1):
    if len(arr) == 0:
        raise IndexError("pop from empty array")
    if index < 0:
        index += len(arr)
    if index < 0 or index >= len(arr):
        raise IndexError("pop index out of range")
    
    popped_value = arr[index]
    new_arr = array.array('i', [0] * (len(arr) - 1))
    
    for i in range(index):
        new_arr[i] = arr[i]
    
    for i in range(index + 1, len(arr)):
        new_arr[i - 1] = arr[i]
    
    return popped_value, new_arr

# Example usage of the queue
queue = Queue()

# Enqueue elements into the queue
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

# Display the queue
queue.display()  # Output: Queue: array('i', [10, 20, 30])

# Peek at the front element
front_element = queue.front()
print(f"Front element: {front_element}")  # Output: Front element: 10

# Dequeue elements from the queue
queue.dequeue()  # Output: Dequeued 10 from queue
queue.dequeue()  # Output: Dequeued 20 from queue

# Display the queue after dequeuing elements
queue.display()  # Output: Queue: array('i', [30])

# Check if the queue is empty
is_empty = queue.is_empty()
print(f"Is the queue empty? {is_empty}")  # Output: Is the queue empty? False

# Get the size of the queue
queue_size = queue.size()
print(f"Queue size: {queue_size}")  # Output: Queue size: 1

# Dequeue the last element
queue.dequeue()  # Output: Dequeued 30 from queue

# Try to dequeue from an empty queue (this will raise an error)
# queue.dequeue()  # Uncommenting this will raise IndexError: dequeue from empty queue

# Check if the queue is empty after dequeuing all elements
is_empty = queue.is_empty()
print(f"Is the queue empty? {is_empty}")  # Output: Is the queue empty? True
