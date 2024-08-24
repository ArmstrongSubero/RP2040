# File: main.py
# Author: Armstrong Subero
# Platform: MicroPython (Raspberry Pi Pico or similar)
# Program: P57_MPC_MultiVariableControl
# Interpreter: MicroPython
# Program Version: 1.4
#
# Program Description: This program demonstrates a Model Predictive Control (MPC) implementation in MicroPython
#                      for controlling both motor speed and temperature simultaneously while respecting constraints.
#                      The MPC controller adjusts the motor power to maintain the desired speed and keep the temperature
#                      within safe limits.

class SimplifiedMPC:
    def __init__(self, speed_setpoint, temp_setpoint, prediction_horizon, dt):
        self.speed_setpoint = speed_setpoint
        self.temp_setpoint = temp_setpoint
        self.prediction_horizon = prediction_horizon
        self.dt = dt
        self.u = 0  # Initial control input
        self.u_min = -10  # Minimum control signal
        self.u_max = 10   # Maximum control signal
        self.temp_max = 80  # Maximum allowable temperature
        self.temp_penalty_factor = 10  # How strongly to penalize temperature error

    def predict(self, current_speed, current_temp, u):
        future_speeds = []
        future_temps = []
        for i in range(self.prediction_horizon):
            # Predict next speed: current speed + control input * dt
            next_speed = current_speed + u * self.dt
            
            # Predict next temperature: current temp + speed contribution + control input contribution
            # Reduced influence of speed and control on temperature rise
            next_temp = current_temp + (next_speed * 0.05) + (u * 0.02)
            
            # Apply temperature constraint
            if next_temp > self.temp_max:
                next_temp = self.temp_max

            future_speeds.append(next_speed)
            future_temps.append(next_temp)
            
            current_speed = next_speed
            current_temp = next_temp
        return future_speeds, future_temps

    def compute_cost(self, future_speeds, future_temps):
        # Calculate the cost function as the sum of squared errors for speed and temperature
        speed_cost = sum([(self.speed_setpoint - speed)**2 for speed in future_speeds])
        temp_cost = sum([(self.temp_setpoint - temp)**2 for temp in future_temps])
        # Apply penalty factor to temperature cost to prioritize temperature control
        total_cost = speed_cost + self.temp_penalty_factor * temp_cost
        return total_cost

    def optimize_control(self, current_speed, current_temp):
        best_u = self.u
        best_cost = float('inf')

        # If the temperature is near or exceeds the maximum, reduce the control input directly
        if current_temp >= self.temp_max - 5:
            self.u -= 0.5  # Apply a significant reduction to control input
            return max(self.u_min, self.u)

        # Try different control inputs and select the one with the lowest cost
        for u_candidate in [self.u + i * 0.1 for i in range(-10, 11)]:
            # Clip control input candidate to prevent excessive values
            u_candidate = max(min(u_candidate, self.u_max), self.u_min)
            
            # Predict future speeds and temperatures with this candidate control input
            future_speeds, future_temps = self.predict(current_speed, current_temp, u_candidate)
            
            # Compute the cost for this candidate
            cost = self.compute_cost(future_speeds, future_temps)
            
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
target_temp = 70    # Target temperature (degrees Celsius)
prediction_horizon = 5  # How many steps into the future we predict
dt = 0.1  # 100 ms time step

# Initialize MPC controller
mpc = SimplifiedMPC(target_speed, target_temp, prediction_horizon, dt)

# Simulated measurement of motor speed and temperature
current_speed = 0
current_temp = 20  # Initial temperature

# Simulate MPC control loop
for i in range(5000):
    # Compute the MPC control output (this would typically adjust motor power)
    control_signal = mpc.optimize_control(current_speed, current_temp)

    # Simulate the effect of the control signal on motor speed and temperature
    current_speed += control_signal * dt  # Speed change based on control input
    current_temp += (current_speed * 0.05) + (control_signal * 0.02)  # Reduced temperature rise

    # Print the current status
    print(f"Time: {i*dt:.1f}s, Target Speed: {target_speed}, Current Speed: {current_speed:.2f}, Control Signal: {control_signal:.2f}, Current Temp: {current_temp:.2f}°C")

    # Wait for the next time step
    time.sleep(dt)
