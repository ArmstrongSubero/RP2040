# File: main.py
# Author: Armstrong Subero
# Platform: MicroPython (Raspberry Pi Pico or similar)
# Program: P58_MPC_Robot
# Interpreter: MicroPython
# Program Version: 1.0
#
# Program Description: This program demonstrates a Model Predictive Control (MPC) implementation
#                      for a mobile patrol robot that must follow a predefined path while avoiding obstacles
#                      and respecting constraints on speed and position.

import math
import time

class PatrolRobotMPC:
    def __init__(self, path, speed_setpoint, prediction_horizon, dt):
        self.path = path  # List of waypoints [(x1, y1), (x2, y2), ...]
        self.speed_setpoint = speed_setpoint
        self.prediction_horizon = prediction_horizon
        self.dt = dt
        self.u_x = 0  # Control input in x direction
        self.u_y = 0  # Control input in y direction
        self.u_max = 1.0  # Maximum control signal
        self.v_max = 2.0  # Maximum velocity
        self.position = [0, 0]  # Initial position [x, y]
        self.velocity = [0, 0]  # Initial velocity [v_x, v_y]
        self.obstacles = [(5, 5), (10, 10)]  # List of obstacle positions

    def predict(self, position, velocity, u_x, u_y):
        future_positions = []
        future_velocities = []
        for i in range(self.prediction_horizon):
            # Update position based on velocity
            next_x = position[0] + velocity[0] * self.dt
            next_y = position[1] + velocity[1] * self.dt
            future_positions.append((next_x, next_y))
            
            # Update velocity based on control inputs
            next_v_x = velocity[0] + u_x * self.dt
            next_v_y = velocity[1] + u_y * self.dt

            # Limit velocity to maximum allowable speed
            speed = math.sqrt(next_v_x**2 + next_v_y**2)
            if speed > self.v_max:
                factor = self.v_max / speed
                next_v_x *= factor
                next_v_y *= factor
            
            future_velocities.append((next_v_x, next_v_y))
            
            position = [next_x, next_y]
            velocity = [next_v_x, next_v_y]
        return future_positions, future_velocities

    def compute_cost(self, future_positions, future_velocities):
        path_cost = 0
        for position in future_positions:
            # Calculate distance to the nearest waypoint
            min_dist = min([math.sqrt((position[0] - wp[0])**2 + (position[1] - wp[1])**2) for wp in self.path])
            path_cost += min_dist**2

        obstacle_cost = 0
        for position in future_positions:
            for obs in self.obstacles:
                dist_to_obs = math.sqrt((position[0] - obs[0])**2 + (position[1] - obs[1])**2)
                if dist_to_obs < 2.0:  # Penalize positions too close to obstacles
                    obstacle_cost += (2.0 - dist_to_obs)**2

        speed_cost = 0
        for velocity in future_velocities:
            speed = math.sqrt(velocity[0]**2 + velocity[1]**2)
            speed_cost += (self.speed_setpoint - speed)**2

        total_cost = path_cost + obstacle_cost + speed_cost
        return total_cost

    def optimize_control(self):
        best_u_x = self.u_x
        best_u_y = self.u_y
        best_cost = float('inf')

        # Try different control inputs and select the one with the lowest cost
        for delta_u_x in [-0.1, 0, 0.1]:
            for delta_u_y in [-0.1, 0, 0.1]:
                u_x_candidate = self.u_x + delta_u_x
                u_y_candidate = self.u_y + delta_u_y

                # Clip control inputs to allowable range
                u_x_candidate = max(min(u_x_candidate, self.u_max), -self.u_max)
                u_y_candidate = max(min(u_y_candidate, self.u_max), -self.u_max)

                # Predict future states with this candidate control input
                future_positions, future_velocities = self.predict(self.position, self.velocity, u_x_candidate, u_y_candidate)

                # Compute the cost for this candidate
                cost = self.compute_cost(future_positions, future_velocities)

                # If this is the best cost, update the best control input
                if cost < best_cost:
                    best_cost = cost
                    best_u_x = u_x_candidate
                    best_u_y = u_y_candidate

        # Set the control inputs to the optimized values
        self.u_x = best_u_x
        self.u_y = best_u_y

    def update(self):
        # Optimize control inputs based on current state
        self.optimize_control()

        # Update position and velocity based on optimized control inputs
        self.position[0] += self.velocity[0] * self.dt
        self.position[1] += self.velocity[1] * self.dt
        self.velocity[0] += self.u_x * self.dt
        self.velocity[1] += self.u_y * self.dt

        # Limit velocity to maximum allowable speed
        speed = math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)
        if speed > self.v_max:
            factor = self.v_max / speed
            self.velocity[0] *= factor
            self.velocity[1] *= factor

        print(f"Position: ({self.position[0]:.2f}, {self.position[1]:.2f}), Velocity: ({self.velocity[0]:.2f}, {self.velocity[1]:.2f})")

# Define a patrol path
path = [(2, 2), (8, 2), (8, 8), (2, 8)]  # A square path

# Initialize MPC controller for the patrol robot
mpc_robot = PatrolRobotMPC(path, speed_setpoint=1.0, prediction_horizon=5, dt=0.1)

# Simulate the patrol
for i in range(5000):
    mpc_robot.update()
    time.sleep(0.1)
