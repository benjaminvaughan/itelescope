#!/usr/bin/python3

"""
This file contains the code for driving the motor
"""

import time
import pigpio
from time import sleep

class Motor:
        # GPIO pins used to drive the motor
        coilpin1a = 2
        coilpin1b = 3
        coilpin2a = 4
        coilpin2b = 17

        def __init__(self):
                self.pi = pigpio.pi()
                self.pi.set_mode(self.coilpin1a, pigpio.OUTPUT)
                self.pi.set_mode(self.coilpin1b, pigpio.OUTPUT)
                self.pi.set_mode(self.coilpin2a, pigpio.OUTPUT)
                self.pi.set_mode(self.coilpin2b, pigpio.OUTPUT)

        def forward(self, delay, steps):
                for i in range(0, steps):
                        self.setstep(1,0,1,0)
                        time.sleep(delay)
                        self.setstep(0,1,1,0)
                        time.sleep(delay)
                        self.setstep(0,1,0,1)
                        time.sleep(delay)
                        self.setstep(1,0,0,1)
                        time.sleep(delay)        

        def backward(self, delay, steps):
                for i in range(0,steps):
                        self.setstep(1,0,0,1)
                        time.sleep(delay)
                        self.setstep(0,1,0,1)
                        time.sleep(delay)
                        self.setstep(0,1,1,0)
                        time.sleep(delay)
                        self.setstep(1,0,1,0)
                        time.sleep(delay)

        def forward2(self, delay, steps):
                for i in range(steps):
                        self.setstep(1,0,0,0)
                        time.sleep(delay)
                        self.setstep(0,1,0,0)
                        time.sleep(delay)
                        self.setstep(0,0,1,0)
                        time.sleep(delay)
                        self.setstep(0,0,0,1)
                        time.sleep(delay)

        def backward2(self, delay,steps):
                for i in range(steps):
                        self.setstep(0,0,0,1)
                        time.sleep(delay)
                        self.setstep(0,0,1,0)
                        time.sleep(delay)
                        self.setstep(0,1,0,0)
                        time.sleep(delay)
                        self.setstep(1,0,0,0)

        def setstep(self, x1,x2,x3,x4):
                self.pi.write(self.coilpin1a,x1)
                self.pi.write(self.coilpin1b,x2)
                self.pi.write(self.coilpin2a,x3)
                self.pi.write(self.coilpin2b,x4)
        
        def run(self):
                while True:
                        delay = input("user inserts the delay")
                        steps = input("user inserts the number of steps forwards")
                        self.forward2(int(delay) / 1000.0, int(steps))
                        steps = input("user inserts the number of steps backwards")
                        self.backward2(int(delay) / 1000.0, int(steps))
        


if __name__ == "__main__":
        print("This is the motor file")
        motor = Motor()
        motor.run()
