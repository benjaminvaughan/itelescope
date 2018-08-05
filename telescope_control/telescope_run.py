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
    key = click.getchar()
    telescope.AWSD_control()
    
    if key == 'c':
        print('you are now in callibration mode')
        self.mode = callibration
        print('enter declination of star')
        line = input()
        star_declination = float(line)
        telescope.set_star_declination(star_declination)
        print('enter right ascension of star')
        line = input()
        star_right_ascension = float(line)
        telescope.set_star_right_ascension(star_right_ascension)
        print('enter longitude')
        line = input()
        longitude = float(line)
        telescope.get_longitude(longitude)
        print('enter latitude')
        line = input()
        latitude = float(line)
        telescope.get_latitude(latitude)
        telescope.get_gast()   
        telescope.set_declination(degrees)
        telescope.get_local_hour_angle()
        sudo_altitude_callibration()
        sudo_azimuth_callibration()
    if key == 'f':
        print('you are now running manual mode')
        self.mode = manual
    if key == 'g':
        print('you are now running goto mode')
        self.mode = goto
        print('enter right_ascension')
        line = input()
        degrees = float(line)
        telescope.set_right_ascension(degrees)
        print('enter declination')
        line = input()
        degrees = float(line)
        telescope.set_declination(degrees)
        telescope.set_altitude()
        telescope.set_azimuth()
        telescope.get_azimuth()
        telescope.get_altitude()

        if mode == goto:
            while True:
                telescope.run_go_to_star()
                time.sleep(0.1)
        elif mode == manual:
            pass
        elif mode == callibration:
            pass
       

