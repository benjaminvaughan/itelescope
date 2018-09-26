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
from telescope_calibration import Stars
from telescope_calibration import Matrices

if __name__ == '__main__':
    #sets up the functions, and builds the different classes
    telescope = Telescope()
    keyboard = Keyboard()
    angle_conversions = angle_conversions()
    two_star_calibration = Two_Star_Calibration(telescope)
    mode = 'manual'
    gps_parse = GPS_parse()
    telescope.get_gast()
    altitude_hall_effect = Hall_Effect_Sensors()
    azimuth_hall_effect = Hall_Effect_Sensors()
    azimuth_hall_effect.hall_effect_encoder_run()
    altitude_hall_effect.hall_effect_encoder_run()
    print(' AWSD or up, right, left, down for manual control, h to print longitude and latitude, C for callibration, l for manual input of longitude and latitude, g for goto mode and f for push to mode')
    while True:
        #while loop that runs the whole time checking for keyboard inputs
        if azimuth_hall_effect.hall_effect_encoder_run() == True:
            telescope.altitude_encoder.run_encoder()
        if altitude_hall_effect.hall_effect_encoder_run() == True:
            telescope.azimuth_encoder.run_altitude_encoder()        
        longlat = gps_parse.longitude_latitude()
        if not longlat is None:
            #if longlat isn't none then set the latitude and longitude to whatever the gps returns.
            (longitude, latitude) = longlat
            telescope.get_longitude(longitude)
            telescope.get_latitude(latitude)
        key = keyboard.getKey()
        #get key is from the keyboard class and gets the keyboard inputs
        if key is None: 
            if mode == 'goto':
                #checks to see if mode is in manual or go-to, if in go-to the telescope will start slewing to an object once the data for htat object is put in.
                telescope.run_go_to_star()
            elif mode == 'manual':
                #allows the user to change the telescope orientation manually
                pass
            elif mode == 'calibration':
                #if the mode is calibration the telescope will allow for you change its orientation manually.
                pass
            continue
        if telescope.AWSD_control(key):
            #this function checks to see if the keyboard inputs are true
            continue
        elif key == 'l':
            #function that allows the user to manually input a longitude and latitude if the gps is not working or connected.
            print('enter longitude')
            line = input()
            longitude = float(line)
            telescope.get_longitude(longitude)
            print('enter latitude')
            line = input()
            latitude = float(line)
            telescope.get_latitude(latitude)
        if key == 'q':
            #function that cleanly quits the program
            telescope.altitude_motor.stopping_motor()
            telescope.azimuth_motor.stopping_motor()
            break
        elif key == 'c':
            #this is the calibration mode for the telescope once in this mode the user points the telescope to a star and declares its position and then points it to another star and declares that stars position to the telescope.
            print('you are now in callibration mode')
            mode = 'calibration'
            print('enter declination of star in DD:MM:SS')
            line = input()
            star_declination = str(line)
            star_declination = angle_conversions.degrees_to_degrees(star_declination)
            print('enter right ascension of star in HH:MM:SS')
            line = input()
            star_right_ascension = str(line)
            star_right_ascension = angle_conversions.hours_to_degrees2(star_right_ascension)
            Stars.define_star_1(star_declination, star_right_ascension)
            print(Stars.star_1)
            telescope.get_gast()   
            telescope.set_star_declination(star_declination)
            telescope.star_LHA()
            telescope.set_star_azimuth()
            telescope.set_star_altitude()
            two_star_calibration.alt_offset_calibration()
            two_star_calibration.az_offset_calibration()
            two_star_calibration.add_az_alt_offset()
            print('enter declination of star 2 in DD:MM:SS')
            line = input()
            star_declination = str(line)
            star_declination = angle_conversions.degrees_to_degrees(star_declination)
            print('enter right ascension of star 2 in HH:MM:SS')
            line = input()
            star_right_ascension = str(line)
            star_right_ascension = angle_conversions.hours_to_degrees2(star_right_ascension)
            Stars.define_star_2(star_declination, star_right_ascension)
            print(Stars.star_2)
            telescope.star_LHA()
            telescope.set_star_altitude()
            telescope.set_star_azimuth()
            two_star_calibration.alt_offset_calibration()
            two_star_calibration.az_offset_calibration()
            two_star_calibration.add_az_alt_offset()
            
        elif key == 'f':
            #this allows the user to manually control the telescope, switches the mode at the beggining of the code to manual.
            print('you are now running manual mode')
            mode = 'manual'
        elif key == 'g':
            #this function allows the user to input data for the target object and then will have the telescope slew towards that objects poisition in the sky. 
            print('you are now running goto mode')
            mode = 'goto'
            print('enter right_ascension in dd:mm:ss')
            line = input()
            degrees = str(line)
            degrees = angle_conversions.hours_to_degrees2(degrees)
            telescope.set_right_ascension(degrees)
            print('enter declination in dd:mm:ss')
            line = input()
            degrees = str(line)
            degrees = angle_conversions.degrees_to_degrees(degrees)
            telescope.set_declination(degrees)
            telescope.get_gast()
            telescope.get_local_hour_angle()
            telescope.set_altitude()
            telescope.set_azimuth()
            telescope.get_azimuth()
            telescope.get_altitude()
        elif key == 'h':
            #function that prints the longitude and latitude that the gps recieves.
            print(longlat)
        else:
            #prints invalid key and the invalid key that was pressed if an invalid key was indeed pressed. 
            print('invalid key "%s"\r' % key)
    

