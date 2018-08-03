from motor_class import Motor
from encoder_class import Encoder
from telescope_class import Telescope
import pigpio
import time
import datetime
import sys
from calculations import Calculations

if __name__ == '__main__':
    telescope = Telescope()
    print('enter latitude')
    line = input()
    latitude = float(line)
    telescope.get_latitude(latitude)
    print('enter right_ascension')
    line = input()
    degrees = float(line)
    print('you entered %f' % degrees)
    telescope.set_right_ascension(degrees)
    print('enter declination')
    line = input()
    degrees = float(line)
    telescope.set_declination(degrees)
    telescope.set_altitude()
    telescope.set_azimuth()
    telescope.get_azimuth()
    telescope.get_altitude()
    while True:
        telescope.update()
        time.sleep(1)
