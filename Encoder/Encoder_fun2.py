#!/usr/bin/env python
#for quadrature encoder

pin_a = 23 # pin where encoder signal a is connected
pin_b = 22 # pin where encoder signal b is connected
position = 0
a_state = None

def call_back_a(pin,level,tick):
    global a_state
    print(pin, level, tick)
    a_state = level


def call_back_b(pin, level, tick):
    global position
    global direction
    if a_state:
        position += 1
        direction = 'clockwise'
    else:
        position -= 1
        direction = 'counter-clockwise'

if __name__ == "__main__":
    pi = pigpio.pi()
    import time
    import pigpio
    pi = pigpio.pi()
    pi.set_mode(pin_a, pigpio.INPUT)
    pi.set_mode(pin_b, pigpio.INPUT)
    pi.callback(pin_a, 2, call_back_a)
    pi.callback(pin_b, 1, call_back_b)
    
    while True:
        print('position')
        print(direction)
        time.sleep(1)
