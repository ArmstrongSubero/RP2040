# File: main.py
# Author: Armstrong Subero
# Platform: Python (Standard or MicroPython with limited capabilities)
# Program: P46_PriorityQueue
# Interpreter: Python 3.x / MicroPython
# Program Version: 1.0
#
# Program Description: This program demonstrates the use of a priority queue in Python.
#                      The priority queue is implemented using the heapq module.
#                      Tasks are added with priorities, and the task with the highest priority
#                      (lowest priority number) is executed first.
#
# Notes:
# Priority queues are useful when tasks or data need to be processed in an order
# based on priority rather than the order of arrival.

import heapq

# Define a list to represent the priority queue
priority_queue = []

# Define a function to add tasks to the priority queue
def add_task(priority, task):
    # Use heapq to push the task into the queue
    heapq.heappush(priority_queue, (priority, task))
    print(f"Added task: '{task}' with priority {priority}")

# Define a function to execute tasks from the priority queue
def execute_task():
    if priority_queue:
        # Use heapq to pop the task with the highest priority (lowest number)
        priority, task = heapq.heappop(priority_queue)
        print(f"Executing task: '{task}' with priority {priority}")
    else:
        print("No tasks in the priority queue")

# Add tasks to the priority queue with different priorities
add_task(3, "Low priority task")
add_task(1, "High priority task")
add_task(2, "Medium priority task")

# Execute tasks in the order of their priority
execute_task()  # Should execute the "High priority task"
execute_task()  # Should execute the "Medium priority task"
execute_task()  # Should execute the "Low priority task"

# Try to execute a task when the queue is empty
execute_task()  # Should indicate no tasks are available
