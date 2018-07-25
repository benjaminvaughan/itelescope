#recovered from swap file
from motor_class import Motor
import pigpio

import time
import click

motor2 = Motor(21, 20, 25, 8, 7)
motor1 = Motor(24, 23, 17, 27, 22)

print('Press an arrow key or q to quit')
timeout = 0.1
while True:
    key = click.getchar()
    if key == 'q': # quit
        break
    if key == 'a': 
        motor1.set_speed(128, 1000, 1)
    if key == 'd':
        motor1.set_speed(128, 1000, 0)
    if key == 's':
        motor2.set_speed(128, 1000, 0)
    if key == 'w':
        motor2.set_speed(128, 1000, 0)
    if key == 'k':
        motor2.set_speed(0, 1000, 0)
    if len(key) == 3: # arrow key
        key = ord(key[2])
        if key == 66: # down arrow
            motor2.set_speed(128, 1000, 1)
            time.sleep(timeout)
            motor2.set_speed(0, 1000, 1)
            print('down')
            motor2.set_speed(128, 1000, 1)
            time.sleep(timeout)
            motor2.set_speed(0, 1000, 1)
        elif key == 67: # left arrow
            print('counter-clockwise')
            motor1.set_speed(128, 1000, 1)
            time.sleep(timeout)
            motor1.set_speed(0, 1000, 1)
        elif key == 68: # right arrow
            print('clockwise')
            motor1.set_speed(128, 1000, 0)
            time.sleep(timeout)
            motor1.set_speed(0, 1000, 1)
        elif key == 65: # up arrow
            print('up')
            motor2.set_speed(128, 1000, 0)
            time.sleep(timeout)
            motor2.set_speed(0, 1000, 0)

motor1.stopping_motor()
motor2.stopping_motor()
