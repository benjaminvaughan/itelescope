from motor_class import Motor
from encoder_class import Encoder
from telescope_class import Telescope
import pigpio
import time
import datetime
import sys
from calculations import Calculations
import click

if __name__ == '__main__':
    telescope = Telescope()
    print('enter mode you would like to use')
    line = input()
    if line == 'mode2':
        print('you are now running manual mode')
        telescope.AWSD_control()
    if line == 'mode1':
        print('you are now running goto mode')
        print('enter longitude')
        line = input()
        longitude = float(line)
        telescope.get_longitude(longitude)
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
        telescope.get_gast()   
        telescope.set_declination(degrees)
        telescope.get_local_hour_angle()
        telescope.set_altitude()
        telescope.set_azimuth()
        telescope.get_azimuth()
        telescope.get_altitude()
        while True:
            telescope.update()
            time.sleep(1)
