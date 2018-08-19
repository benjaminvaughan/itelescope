#!/usr/bin/python3
#file for stringing together everything and running the telescope
from parsing_gps import GPS_parse
from motor_class import Motor
from encoder_class import Encoder
from telescope_class import Telescope
import pigpio
import time
import datetime
import sys
from calculations import Calculations
import click
from angle_conversions import angle_conversions
from keys import Keyboard
from two_star_calibration import Two_Star_Calibration

if __name__ == '__main__':
    telescope = Telescope()
    keyboard = Keyboard()
    angle_conversions = angle_conversions()
    two_star_calibration = Two_Star_Calibration(telescope)
    mode = 'manual'
    telescope.azimuth_encoder.run_altitude_encoder()
    telescope.altitude_encoder.run_encoder()
    gps_parse = GPS_parse()
    telescope.get_gast()
    telescope.get_longitude(40)
    telescope.get_latitude(40)
    while True:   
        mode = 'goto'
        line = '200:200:200'
        degrees = (line)
        degrees = angle_conversions.hours_to_degrees2(degrees)
        telescope.set_right_ascension(degrees)
        line = '200:200:200'
        degrees = (line)
        degrees = angle_conversions.degrees_to_degrees(degrees)
        telescope.set_declination(degrees)
        telescope.get_gast()
        telescope.get_local_hour_angle()
        telescope.set_altitude()
        telescope.set_azimuth()
        telescope.get_azimuth()
        telescope.get_altitude()
        telescope.run_go_to_star()

