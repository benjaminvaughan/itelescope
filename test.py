#!/usr/bin/python3

"""
Test the motor
"""

from motor import Motor

motor = Motor()
input("Turning on 1")
motor.setstep(1,0,0,0)
input("Turning on 2")
motor.setstep(0,1,0,0)
input("Turning on 3")
motor.setstep(0,0,1,0)
input("Turning on 4")
motor.setstep(0,0,0,1)
