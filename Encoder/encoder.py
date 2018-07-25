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
position = 0
degrees = 0
def call_back_a(pin, level, tick):
        global a_state
        a_state = level

def call_back_b(pin, level, tick):
        global position
        global direction
        global degrees
        global constant
        if a_state:
                position += 1
                direction = 'clockwise'
               
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
               

if __name__ == '__main__':
        pi = pigpio.pi()
        pi.set_mode(pin_b, pigpio.INPUT)
        pi.set_mode(pin_a, pigpio.INPUT)
        pi.set_mode(pin_z, pigpio.INPUT)
        pi.callback(pin_a, 2, call_back_a)
        pi.callback(pin_b, 2, call_back_b)
        pi.callback(pin_z, 2, call_back_z)

        while True:
                print(direction)
                print('degrees',degrees)
                print('position', position)
                time.sleep(1)
        
