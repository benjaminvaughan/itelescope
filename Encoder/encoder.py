#program to test encoder

import pigpio
import time
import click

pin_a = 16
pin_b = 19
pin_z = 26
a_state = None
direction = 'string'
constant = 360.0 / 5000
z_state = None

def call_back_a(pin, level, tick):
        global a_state
        a_state = level

def call_back_b(pin, level, tick):
        global position
        global direction
        if a_state:
                position += 1
                direction = 'clockwise'
                return position
        else:
                position -= 1
                direction = 'counter-clockwise'
                return position
        degrees = position * constant
        return degrees

def call_back_z(pin, level, tick):
        global z_state
        z_state = level
        if z_state:
                position = 0
                return position

if __name__ = "__main__":
        pi = pigpio.pi()
        pi.set_mode(pin_b, pigpio.INPUT)
        pi.set_mode(pin_a, pigpio.INPUT)
        pi.set_mode(pin_z, pigpio.INPUT)
        pi.callback(pin_a, 2, call_back_a)
        pi.callback(pin_b, 1, call_back_b)
        pi.callback(pin_z, 2, call_back_z)

        while True:
                print(position)
                print(direction)
                print(degrees)
                time.sleep(0.1)
        
