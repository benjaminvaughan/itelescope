
import pigpio
from motor_class import Motor
import time
import click

motor1 = Motor(21, 20, 25, 8 ,7)
motor2 = Motor(24, 23, 17, 27, 22)
pin_a = 16
pin_b = 19
pin_z = 26
a_state = None
direction = 'string'
constant = 360.0/5000
z_state = None
degrees = None
timeout = 0.1

def call_back_a(pin, level, tick):
    global a_state
    a_state = level

def call_back_b(pin, level, tick):
    global position
    global direction
    global degrees
    if a_state:
        position += 1
        direction = 'clockwise'
        return position
    else:
        position -= 1
        direction = 'counter-clockwise'
    degrees = position * constant
    return degrees
def call_back_z(pin, level, tick):
    global z_state
    z_state = level
    if z_state:
        position = 0
        return position

if __name__ == "__main__":
    pi = pigpio.pi()
    pi.set_mode(pin_b, pigpio.INPUT)
    pi.set_mode(pin_a, pigpio.INPUT)
    pi.callback(pin_a, 2, call_back_a)
    pi.callback(pin_b, 1, call_back_b)
    pi.callback(pin_z, 2, call_back_z)
    print('press q to quit, k to kill or awsd to move')

    while True:
        key = click.getchar()
        if key == 'q': # quit
            break
        if key == 'a': #left
            motor1.set_speed(128, 1000, 1)
        if key == 'd': #right
            motor1.set_speed(128, 1000, 1)
        if key == 's': #down
            motor2.set_speed(128, 1000, 0)
        if key == 'w': #up
            motor2.set_speed(128, 1000, 0)
        if key == 'k': #KILL
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

        print(degrees)
        print(direction)
        time.sleep(0.1)


