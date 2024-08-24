# File: main.py
# Author: Armstrong Subero
# Platform: MicroPython (Raspberry Pi Pico or similar)
# Program: P54_RobotStateMachine
# Interpreter: MicroPython
# Program Version: 1.0
#
# Program Description: This program demonstrates a simple state machine implementation
#                      for a patrol robot in MicroPython. The robot transitions between 
#                      patrol, engage, and retreat states based on conditions.

class State:
    def __init__(self, name, on_enter=None, on_exit=None):
        self.name = name
        self.on_enter = on_enter
        self.on_exit = on_exit

    def enter(self):
        if self.on_enter:
            self.on_enter()

    def exit(self):
        if self.on_exit:
            self.on_exit()

class StateMachine:
    def __init__(self, initial_state):
        self.current_state = initial_state
        self.current_state.enter()

    def transition_to(self, new_state):
        self.current_state.exit()
        self.current_state = new_state
        self.current_state.enter()

# Example conditions and actions for the patrol robot
battery_level = 30  # Example battery level (0-100)
enemy_detected = False  # Example enemy detection status

def is_battery_low():
    return battery_level < 20  # Battery is considered low if below 20%

def is_enemy_nearby():
    return enemy_detected  # Return True if enemy is detected

def patrol_area():
    print("State: Patrolling the area.")

def engage_enemy():
    print("State: Engaging enemy.")

def retreat_to_charging_station():
    print("State: Retreating to charging station.")

# Define states
patrol_state = State("Patrol", on_enter=patrol_area)
engage_state = State("Engage", on_enter=engage_enemy)
retreat_state = State("Retreat", on_enter=retreat_to_charging_station)

# Initialize state machine
robot_state_machine = StateMachine(patrol_state)

# Simulate robot behavior
def update_robot_state():
    global battery_level, enemy_detected

    if is_battery_low():
        robot_state_machine.transition_to(retreat_state)
    elif is_enemy_nearby():
        robot_state_machine.transition_to(engage_state)
    else:
        robot_state_machine.transition_to(patrol_state)

# Scenario 1: Battery is low
battery_level = 15  # Low battery
enemy_detected = False  # No enemy
print("=== Scenario 1: Battery Low ===")
update_robot_state()
print()

# Scenario 2: Enemy nearby, battery sufficient
battery_level = 30  # Sufficient battery
enemy_detected = True  # Enemy detected
print("=== Scenario 2: Enemy Nearby, Battery Sufficient ===")
update_robot_state()
print()

# Scenario 3: No enemy, battery sufficient
battery_level = 30  # Sufficient battery
enemy_detected = False  # No enemy
print("=== Scenario 3: No Enemy, Battery Sufficient ===")
update_robot_state()
print()
