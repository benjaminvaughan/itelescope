#script for motor moving 360 degrees
import pigpio
from motor_class import Motor

motor = Motor(21, 20, 25, 8, 7)
steps = 360/0.5*32*3.6
stepcount = 0

Motor.creating_wave(1000, 1000)
for i in range(0, int(steps)):
    stepcount += 1
    if stepcount > 1:
        motor.one_step()
