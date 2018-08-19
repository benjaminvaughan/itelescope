from encoder_class import Encoder
from motor_class import Motor
#program for debugging the telescope_run application.
import pigpio
import sys
from calculations import Calculations
import math
import numpy
import click
from telescope_class import Telescope


telescope = Telescope()

if __name__ == '__main__':
    pi = pigpio.pi()
    altitude_encoder = Encoder(16, 19, 26, 1)
    altitude_motor = Motor(24, 23, 25, 8, 7, pi)
    azimuth_encoder = Encoder(20, 21, 12, 2)
    azimuth_motor = Motor(10, 9 , 17, 27, 22)
    longitude = 20
    latitude = 20
    telescope.get_longitude(longitude)
    telescope.get_latitude(latitude)
    telescope.set_right_ascension(20)
    telescope.set_declination(20)
    telescope.get_gast()
    telescope.get_local_hour_angle()
    telescope.set_altitude()
    telescope.set_azimuth()
    altitude_encoder.run_encoder()
    azimuth_encoder.run_altitude_encoder()
    tele_azimuth = azimuth_encoder.get_degrees()
    tele_altitude = altitude_encoder.get_degrees()
    telescope = Telescope()
    telescope.azimuth = 200
    telescope.altitude = 200
    while True:
        if tele_azimuth != 20 or tele_altitude != 20:
            telescope.azimuth_update()
            telescope.altitude_update() 
