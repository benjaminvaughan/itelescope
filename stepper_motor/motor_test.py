
from motor_class import Motor
import pigpio

import click
import time

motor = Motor(20, 21, 14, 15, 18)
print('Press an arrow key or q to quit')
while True:
    key = click.getchar()
    if key == 'q':
        break
    if len(key) == 3: # arrow key
        code = ord(key[2])
        if code == 66:
            print('down')
        elif code == 67:
            motor.set_speed(128, 1000, 1)
            print('counter-clockwise')
            try:
                while True:
                    motor.write_to_motor(1)
            except code!= 67:
                print(stopping motion)
            finally:
                motor.stopping_motor()
        elif code == 68:
            print('clockwise')
            motor.set_speed(128, 1000, 0)
            try:
                while True:
                    motor.write_to_motor(0)
            except code != 68:
                print(stopping motion)
            finally:
                motor.stopping_motor()
        elif code == 65:
            print('up')
        else:
            motor.set_speed(0, 1000, 0)
            print(code)


