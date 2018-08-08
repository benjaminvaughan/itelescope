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
    while True:
        key = keyboard.getKey()
        if key is None: 
            if mode == 'goto':
                telescope.run_go_to_star()
            elif mode == 'manual':
                pass
            elif mode == 'calibration':
                pass
            continue
        if telescope.AWSD_control(key):
            continue
    
        if key == 'q':
            break
        elif key == 'c':
            print('you are now in callibration mode')
            mode = 'calibration'
            print('enter declination of star in DD:MM:SS')
            line = input()
            star_declination = str(line)
            star_declination = angle_conversions.degrees_to_degrees(star_declination)
            telescope.set_star_declination(star_declination)
            print(telescope.set_star_declination(star_declination))
            print('enter right ascension of star in HH:MM:SS')
            line = input()
            star_right_ascension = str(line)
            star_right_ascension = angle_conversions.hours_to_degrees2(star_right_ascension)
            telescope.set_star_right_ascension(star_right_ascension)
            print(star_right_ascension)
            print('enter longitude')
            line = input()
            longitude = float(line)
            telescope.get_longitude(longitude)
            print('enter latitude')
            line = input()
            latitude = float(line)
            telescope.get_latitude(latitude)
            telescope.get_gast()   
            telescope.set_star_declination(latitude)
            telescope.star_LHA()
            two_star_calibration.alt_offset()
            two_star_calibration.az_offset()
            two_star_calibration.add_az_alt_offset()
            print('enter declination of star 2 in DD:MM:SS')
            line = input()
            star_declination = str(line)
            star_declination = angle_conversions.degrees_to_degrees(star_declination)
            telescope.set_star_declination(star_declination)
            print('enter right ascension of star 2 in HH:MM:SS')
            line = input()
            star_right_ascension = str(line)
            star_right_ascension = angle_conversions.hours_to_Degrees2(star_Right_ascension)
            telescope.set_star_right_ascension(star_right_ascension)
            telescope.star_LHA()
            two_star_calibration.alt_offset()
            two_star_calibration.az_offset()
            two_star_calibration.add_az_alt_offset()
        elif key == 'f':
            print('you are now running manual mode')
            mode = 'manual'
        elif key == 'g':
            print('you are now running goto mode')
            mode = 'goto'
            print('enter right_ascension')
            line = input()
            degrees = float(line)
            telescope.set_right_ascension(degrees)
            print('enter declination')
            line = input()
            degrees = float(line)
            telescope.set_declination(degrees)
            telescope.get_local_hour_angle()
            telescope.set_altitude()
            telescope.set_azimuth()
            telescope.get_azimuth()
            telescope.get_altitude()
        else:
            print('invalid key "%s"\r' % key)
       

