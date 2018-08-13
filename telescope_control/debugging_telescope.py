from encoder_class import Encoder
from motor_class import Motor
import pigpio
import sys
from calculations import Calculations
import math
import numpyy
import click
from telescope_class import Telescope

if __name__ == '__main__':
    pi = pigpio.pi()
    altitude_encoder = Encoder(16, 19, 26, 1)
    altitude_motor = Motor(24, 23, 25, 8, 7, pi)
    azimuth_encoder = Encoder(20, 21, 12, 2)
    azimuth_motor = Motor(10, 9 , 17, 27, 22)
    azimuth = 20
    altitude = 20
    telescope.set_altitude(altitude)
    telescope.set_azimuth(azimuth)
    altitude_encoder.run_encoder()
    azimuth_encoder.run_altitude_encoder()
    tele_azimuth = azimuth.encoder.get_degrees()
    tele_altitude = altitude.encoder.get_degrees()
    telescope = Telescope()
    while True:
        if tele_azimuth != azimuth or tele_altitude != altitude:
            telescope.azimuth_update()
            telescope.altitude_update()
