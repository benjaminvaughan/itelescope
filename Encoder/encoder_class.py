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
        pi.set_mode(pin_a, pigpio.INPUT)
        pi.set_mode(pin_b, pigpio.INPUT)
        pi.set_mode(pin_z, pigpio.INPUT)
        self.a_state = None
        self.z_state = None
        self.degree = 0
        self.position = 0
        self.constant = 360.0 / 5000

    def call_back_a(self, pin, level, tick):
        self.a_state = level

    def call_back_b(self, pin, level, tick):
        if self.a_state:
            self.position += 1
        else:
            self.position -= 1
        self.degree = self.position * self.constant

    def call_back_z(self, pin, level, tick):
        if self.z_state:
            self.position = 0

    def print_degrees(self):
        print(degree)   
    def run_encoder(self):
        self.pi.callback(self.pin_a, 2, self.call_back_a)
        self.pi.callback(self.pin_b, 2, self.call_back_b)
        self.pi.callback(self.pin_z, 2, self.call_back_z)
        
