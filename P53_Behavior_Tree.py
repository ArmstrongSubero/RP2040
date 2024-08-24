# File: main.py
# Author: Armstrong Subero
# Platform: MicroPython (Raspberry Pi Pico or similar)
# Program: P53_BehaviorTree
# Interpreter: MicroPython
# Program Version: 1.0
#
# Program Description: This program demonstrates a behavior tree implementation for a patrol robot
#                      in MicroPython. The robot will decide whether to patrol, engage an enemy, 
#                      or retreat to a charging station based on the conditions.

class NodeStatus:
    SUCCESS = 1
    FAILURE = 0
    RUNNING = -1

class Node:
    def run(self):
        raise NotImplementedError("Must be implemented by subclass.")

class ActionNode(Node):
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def run(self):
        print(f"Running Action: {self.name}")
        return self.action()

class ConditionNode(Node):
    def __init__(self, name, condition):
        self.name = name
        self.condition = condition

    def run(self):
        print(f"Checking Condition: {self.name}")
        return NodeStatus.SUCCESS if self.condition() else NodeStatus.FAILURE

class SequenceNode(Node):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def run(self):
        print(f"Running Sequence: {self.name}")
        for child in self.children:
            status = child.run()
            if status != NodeStatus.SUCCESS:
                return status
        return NodeStatus.SUCCESS

class SelectorNode(Node):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def run(self):
        print(f"Running Selector: {self.name}")
        for child in self.children:
            status = child.run()
            if status == NodeStatus.SUCCESS:
                return status
        return NodeStatus.FAILURE

# Define conditions and actions for the patrol robot
def is_battery_low():
    print("Condition: Is battery low?")
    return battery_level < 20  # Battery is considered low if below 20%

def is_enemy_nearby():
    print("Condition: Is enemy nearby?")
    return enemy_detected  # Return True if enemy is detected

def retreat_to_charging_station():
    print("Action: Retreating to charging station.")
    return NodeStatus.SUCCESS

def attack_enemy():
    print("Action: Attacking enemy.")
    return NodeStatus.SUCCESS

def patrol_area():
    print("Action: Patrolling the area.")
    return NodeStatus.SUCCESS

# Build the behavior tree for the patrol robot
root = SelectorNode("Root")
low_battery_sequence = SequenceNode("Low Battery Sequence")
low_battery_sequence.add_child(ConditionNode("Check Battery Level", is_battery_low))
low_battery_sequence.add_child(ActionNode("Retreat to Charging Station", retreat_to_charging_station))

engage_enemy_sequence = SequenceNode("Engage Enemy Sequence")
engage_enemy_sequence.add_child(ConditionNode("Check if Enemy Nearby", is_enemy_nearby))
engage_enemy_sequence.add_child(ActionNode("Attack Enemy", attack_enemy))

root.add_child(low_battery_sequence)
root.add_child(engage_enemy_sequence)
root.add_child(ActionNode("Patrol Area", patrol_area))

# Scenario 1: Battery is low, robot should retreat to charging station
battery_level = 15  # Set battery level low to trigger retreat
enemy_detected = False  # No enemy detected

print("=== Scenario 1: Battery Low ===")
status = root.run()
print("Behavior Tree Execution Status:", "SUCCESS" if status == NodeStatus.SUCCESS else "FAILURE")
print()

# Scenario 2: Enemy is nearby, battery is sufficient, robot should engage enemy
battery_level = 30  # Set battery level sufficient
enemy_detected = True  # Enemy detected

print("=== Scenario 2: Enemy Nearby, Battery Not Low ===")
status = root.run()
print("Behavior Tree Execution Status:", "SUCCESS" if status == NodeStatus.SUCCESS else "FAILURE")
print()

# Scenario 3: No enemy nearby, battery is sufficient, robot should patrol area
battery_level = 30  # Set battery level sufficient
enemy_detected = False  # No enemy detected

print("=== Scenario 3: No Enemy Nearby, Battery Not Low ===")
status = root.run()
print("Behavior Tree Execution Status:", "SUCCESS" if status == NodeStatus.SUCCESS else "FAILURE")
print()
