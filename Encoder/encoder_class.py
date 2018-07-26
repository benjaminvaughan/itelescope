import pigpio
import time

class Encoder():
    def __init__(self, pin_a, pin_b, pin_z, pi = None):
        if pi is None:
            pi = pigpio.pi()
        self.pi = pi
        self.pin_a = pin_a
        self.pin_b = pin_b
        self.pin_z = pin_z
        self.pi.set_mode(pin_a, pigpio.INPUT)
        self.pi.set_mode(pin_b, pigpio.INPUT)
        self.pi.set_mode(pin_z, pigpio.INPUT)
        a_state = None
        constant = 360.0 / 5000
        z_state = None
        position = 0
        degrees = 0

    def call_back_a(self, pin, level, tick):
        global a_state
        a_state = level

    def call_back_b(self, pin, level, tick):
        global position
        global degrees
        global constant
        if a_state:
            position += 1
        else:
            position -= 1
        degrees = position * constant

    def call_back_z(self, pin, level, tick):
        global z_state
        if z_state:
            position = 0

    def print_degrees(self):
        print('degrees', degrees)
    
        
