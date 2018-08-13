from encoder_class import Encoder
from motor_class import Motor
import pigpio
import sys
from calculations import Calculations
import math
import numpy
import click
from telescope_class import Telescope
pi = pigpio.pi()
telescope = Telescope()
altitude_encoder = Encoder(16, 19, 26, 1)
altitude_motor = Motor(24, 23, 25, 8, 7, pi)
azimuth_encoder = Encoder(20, 21, 12, 2)
azimuth_motor = Motor(10, 9 , 17, 27, 22)
declination = "20:20:20"
right_ascension = "20:20:20"
telescope.set_declination(declination)
telescope.set_right_ascension(right_ascension)
telescope.get_latitude(20)
telescope.get_longitude(20)
telescope.get_gast()
telescope.get_local_hour_angle()
telescope.set_azimuth()
 
if __name__ == '__main__':
    altitude_encoder.run_encoder()
    telescope.set_altitude()
    azimuth_encoder.run_altitude_encoder()
    tele_azimuth = azimuth_encoder.get_degrees()
    tele_altitude = altitude_encoder.get_degrees()
    while True:
        if tele_azimuth != azimuth or tele_altitude != altitude:
            telescope.azimuth_update()
            telescope.altitude_update()
