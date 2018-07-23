
from motor_class import Motor
import pigpio

import time
import click

motor1 = Motor(21, 20, 18, 15, 14)
print('Press an arrow key or q to quit')
motor2 = Motor(5 , 6, 13 , 19, 6)
timeout = 0.1
while True:
    key = click.getchar()
    if key == 'q': # quit
        break
    if key == 'a': 
        motor1.set_speed(128, 1000, 1)
    if key == 'd':
        motor1.set_speed(128, 1000, 0)
    if key == 'w':
        motor2.set_speed(128, 1000, 0)
    if key == 's':
        motor2.set_speed(128, 1000, 1)
    if key == 'k': # stop
        motor1.set_speed(0, 1000, 0)
        motor2.set_speed(0, 1000, 0)
    if len(key) == 3: # arrow key
        key = ord(key[2])
        if key == 66: # down arrow
            motor2.set_speed(128, 1000, 1)
            time.sleep(timeout)
            motor2.set_speed(0, 1000, 1)
            print('down')
        elif key == 67: # left arrow
            print('counter-clockwise')
            motor.set_speed(128, 1000, 1)
            time.sleep(timeout)
            motor.set_speed(0, 1000, 1)
        elif key == 68: # right arrow
            print('clockwise')
            motor.set_speed(128, 1000, 0)
            time.sleep(timeout)
            motor.set_speed(0, 1000, 1)
        elif key == 65: # up arrow
            print('up')
            motor2.set_speed(128, 1000, 0)
            time.sleep(timeout)
            motor2.set_speed(0, 1000, 0)

motor.stopping_motor()
