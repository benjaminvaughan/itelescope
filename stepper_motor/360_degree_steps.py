#script for motor moving 360 degrees

from motor_class import Motor

motor = Motor(21, 20, 25, 8, 7)
steps = 360/0.5*32*3.6
stepcount = 0
for i in range(0, steps):
    stepcount += 1
    if stepcount > 1:
        motor.one_step()
