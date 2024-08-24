# File: main.py
# Author: Armstrong Subero
# Platform: MicroPython (Raspberry Pi Pico or similar)
# Program: P56_MPC
# Interpreter: MicroPython
# Program Version: 1.2
#
# Program Description: This program demonstrates an improved Model Predictive Control (MPC) 
#                      implementation in MicroPython with a basic optimization loop. The MPC controller
#                      adjusts the motor power to maintain a desired speed by predicting future states
#                      and minimizing the error.

class SimplifiedMPC:
    def __init__(self, setpoint, prediction_horizon, control_horizon, dt):
        self.setpoint = setpoint
        self.prediction_horizon = prediction_horizon
        self.control_horizon = control_horizon
        self.dt = dt
        self.u = 0  # Initial control input
        self.u_min = -10  # Minimum control signal
        self.u_max = 10   # Maximum control signal

    def predict(self, current_speed, u):
        future_speeds = []
        for i in range(self.prediction_horizon):
            # Simple model: next speed = current speed + control input * dt
            next_speed = current_speed + u * self.dt
            future_speeds.append(next_speed)
            current_speed = next_speed
        return future_speeds

    def compute_cost(self, future_speeds):
        # Calculate the cost function (sum of squared errors)
        return sum([(self.setpoint - speed)**2 for speed in future_speeds])

    def optimize_control(self, current_speed):
        best_u = self.u
        best_cost = float('inf')

        # Try different control inputs and select the one with the lowest cost
        for u_candidate in [self.u + i * 0.1 for i in range(-10, 11)]:
            # Clip control input candidate to prevent excessive values
            u_candidate = max(min(u_candidate, self.u_max), self.u_min)
            
            # Predict future speeds with this candidate control input
            future_speeds = self.predict(current_speed, u_candidate)
            
            # Compute the cost for this candidate
            cost = self.compute_cost(future_speeds)
            
            # If this is the best cost, update the best control input
            if cost < best_cost:
                best_cost = cost
                best_u = u_candidate

        # Set the control input to the optimized value
        self.u = best_u
        
        return self.u

# Example usage:
import time

# MPC parameters
target_speed = 100  # Target speed for the motor (e.g., RPM)
prediction_horizon = 5  # How many steps into the future we predict
control_horizon = 3  # How many control actions we optimize
dt = 0.1  # 100 ms time step

# Initialize MPC controller
mpc = SimplifiedMPC(target_speed, prediction_horizon, control_horizon, dt)

# Simulated measurement of motor speed
current_speed = 0

# Simulate MPC control loop
for i in range(5000):
    # Compute the MPC control output (this would typically adjust motor power)
    control_signal = mpc.optimize_control(current_speed)

    # Simulate the effect of the control signal on motor speed
    current_speed += control_signal * dt  # This is a simplification

    # Print the current status
    print(f"Time: {i*dt:.1f}s, Target Speed: {target_speed}, Current Speed: {current_speed:.2f}, Control Signal: {control_signal:.2f}")

    # Wait for the next time step
    time.sleep(dt)
