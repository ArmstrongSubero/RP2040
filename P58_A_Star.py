# File: main.py
# Author: Armstrong Subero
# Platform: MicroPython (Raspberry Pi Pico or similar)
# Program: P60_AStar_Pathfinding
# Interpreter: MicroPython
# Program Version: 1.0
#
# Program Description: This program demonstrates the implementation of the A* algorithm
#                      for pathfinding on a 2D grid. The robot must find the shortest path
#                      from a start position to a goal position while avoiding obstacles.
#                      The A* algorithm efficiently finds the optimal path by considering
#                      both the cost to reach a node and the estimated cost to reach the goal.

import heapq

class Node:
    def __init__(self, position, parent=None):
        """
        Initialize a new node.

        :param position: Tuple (x, y) representing the node's position on the grid.
        :param parent: The parent node from which this node was generated.
        """
        self.position = position  # Node's position on the grid
        self.parent = parent      # Parent node, used to trace the path back
        self.g = 0                # Cost from start to this node
        self.h = 0                # Heuristic cost estimate from this node to the goal
        self.f = 0                # Total cost (g + h)

    def __lt__(self, other):
        """
        Comparison method for priority queue.
        
        :param other: Another node to compare with.
        :return: True if this node's f score is less than the other node's f score.
        """
        return self.f < other.f

def heuristic(current, goal):
    """
    Calculate the heuristic cost estimate (H) from the current node to the goal.

    :param current: Tuple (x, y) representing the current node's position.
    :param goal: Tuple (x, y) representing the goal node's position.
    :return: The Manhattan distance between the current node and the goal.
    """
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def a_star(grid, start, goal):
    """
    Perform A* pathfinding algorithm to find the shortest path from start to goal.

    :param grid: 2D list representing the grid (0 = free space, 1 = obstacle).
    :param start: Tuple (x, y) representing the starting position.
    :param goal: Tuple (x, y) representing the goal position.
    :return: List of tuples representing the path from start to goal, or None if no path found.
    """
    # Create start and goal nodes
    start_node = Node(start)
    goal_node = Node(goal)
    
    # Initialize open and closed lists
    open_list = []
    closed_list = set()
    
    # Add the start node to the open list
    heapq.heappush(open_list, start_node)
    
    while open_list:
        # Get the node with the lowest f score
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)
        
        # Check if we've reached the goal
        if current_node.position == goal_node.position:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        # Generate children (neighboring nodes)
        neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # 4 directions (up, down, left, right)
        for new_position in neighbors:
            node_position = (current_node.position[0] + new_position[0],
                             current_node.position[1] + new_position[1])

            # Make sure the node is within bounds and not an obstacle
            if (0 <= node_position[0] < len(grid) and
                0 <= node_position[1] < len(grid[0]) and
                grid[node_position[0]][node_position[1]] == 0 and
                node_position not in closed_list):

                # Create new node
                child_node = Node(node_position, current_node)
                child_node.g = current_node.g + 1
                child_node.h = heuristic(child_node.position, goal_node.position)
                child_node.f = child_node.g + child_node.h

                # Check if this node is already in the open list with a lower f value
                if any(open_node.position == child_node.position and open_node.f <= child_node.f for open_node in open_list):
                    continue

                # Add the child node to the open list
                heapq.heappush(open_list, child_node)
    
    return None  # No path found

# Example usage:
grid = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0]
]

start = (0, 0)  # Starting point
goal = (5, 5)   # Goal point

path = a_star(grid, start, goal)
print("Path:", path)
