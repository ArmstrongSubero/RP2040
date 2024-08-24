# File: main.py
# Author: Armstrong Subero
# Platform: MicroPython (Raspberry Pi Pico)
# Program: P55_PID_Loop
# Interpreter: MicroPython
# Program Version: 1.0
#
# Program Description: This program demonstrates a simple PID control loop implementation
#                      in MicroPython. The PID controller adjusts the motor power to maintain
#                      a desired speed.

class PID:
    def __init__(self, Kp, Ki, Kd, setpoint):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.integral = 0
        self.previous_error = 0

    def compute(self, measurement, dt):
        # Calculate error
        error = self.setpoint - measurement

        # Proportional term
        P_out = self.Kp * error

        # Integral term
        self.integral += error * dt
        I_out = self.Ki * self.integral

        # Derivative term
        derivative = (error - self.previous_error) / dt
        D_out = self.Kd * derivative

        # Calculate total output
        output = P_out + I_out + D_out

        # Update previous error
        self.previous_error = error

        return output

# Example usage:
import time

# PID parameters
Kp = 1.0
Ki = 0.1
Kd = 0.05
target_speed = 100  # Target speed for the motor (e.g., RPM)

# Initialize PID controller
pid = PID(Kp, Ki, Kd, target_speed)

# Simulated measurement of motor speed
current_speed = 0

# Time step
dt = 0.1  # 100 ms time step

# Simulate PID control loop
i = 0
while True:
    # Compute the PID output (this would typically adjust motor power)
    control_signal = pid.compute(current_speed, dt)

    # Simulate the effect of the control signal on motor speed
    current_speed += control_signal * dt  # This is a simplification

    # Print the current status
    print(f"Time: {i*dt:.1f}s, Target Speed: {target_speed}, Current Speed: {current_speed:.2f}, Control Signal: {control_signal:.2f}")

    i = i + 1
    
    # Wait for the next time step
    time.sleep(dt)

