from machine import Timer, Pin
import time

class Range_Finder:
    def __init__(self, trigger_pin, echo_pin):
        # Initialize the trigger and echo pins
        self.trig = Pin(trigger_pin, Pin.OUT, value=0)
        self.echo = Pin(echo_pin, Pin.IN)

        # Initialize pulse start time, duration, and a flag
        self.pulse_start = 0
        self.pulse_duration = 0
        self.flag = False

        # Create a timer to trigger the ultrasonic pulse periodically
        self.trigger_timer = Timer(freq=5, mode=Timer.PERIODIC, callback=self.trigger_isr)

        # Set up an interrupt for the echo pin to capture rising and falling edges
        self.echo.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=self.echo_isr)

    def echo_isr(self, pin):
        # Interrupt Service Routine for the echo pin
        if self.echo.value() == 1:  # Rising edge detected
            self.pulse_start = time.ticks_us()  # Record the start time
        else:  # Falling edge detected
            self.pulse_duration = time.ticks_diff(time.ticks_us(), self.pulse_start) 
            self.flag = True  # Set the flag indicating a measurement is ready
    
    def trigger_isr(self, t):
        # Timer callback function to trigger the ultrasonic pulse
        self.trig.value(1)
        time.sleep_us(10)  # Pulse the trigger for 10 microseconds
        self.trig.value(0)
        
    def distance(self):
        # Calculate the distance based on pulse duration
        self.flag = False  # Reset the flag
        return self.pulse_duration * 0.0343 / 2  # Convert time to distance in cm

# Define trigger and echo pin numbers
TRIGGER = 13
ECHO = 12

# Create an instance of the Range_Finder class
range_finder = Range_Finder(TRIGGER, ECHO)
        
while True:
    while not range_finder.flag:  # Wait until a measurement is ready
        pass
    
    # Print the measured distance
    print("{:.1f} cm".format(range_finder.distance()))
