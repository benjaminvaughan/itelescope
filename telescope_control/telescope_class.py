#**telescope class for control of the telescope **
from encoder_class import Encoder
from motor_class import Motor
import datetime
import pigpio
import sys
from calculations import Calculations
import math
import numpy
import click
#used for talking with meadle LX200 Protocol

class Telescope():
    def __init__(self):
        pi = pigpio.pi()
        self.altitude_encoder = Encoder(16, 19, 26, 1)
        self.altitude_motor = Motor(24, 23, 25, 8, 7, pi)
        self.azimuth_encoder = Encoder(20, 21, 12, 2)
        self.azimuth_motor = Motor(10, 9 , 17, 27, 22, pi)
        self.Calculations = Calculations()
        self.speed = 0
         
    def set_azimuth(self):
        """
        sets the target azimuth after converting from right_ascension and 
        declination, returns in degrees right now
        """
        self.azimuth = self.Calculations.convert_to_azimuth( self.declination, self.right_ascension, self.Latitude, self.LHA)
        if self.azimuth < 0:
            self.azimuth = self.azimuth + 360.0
            return self.azimuth
        else:
            pass
        return self.azimuth
        print('azimuth set to', self.azimuth)

    def set_right_ascension(self, target_right_ascension):
        """
        sets the target_right_ascension in terms of degrees
        """
        self.right_ascension = target_right_ascension
        return self.right_ascension

    def set_declination(self, target_declination):
        """
        sets the target_declination in terms of degrees
        """
        self.declination = target_declination
        return self.declination

    def set_star_right_ascension(self, star_right_ascension):
        """
        used for callibration, sets the right ascension of the star in the scope
        """
        self.s_right_ascension = star_right_ascension
        return self.s_right_ascension

    def set_star_declination(self, star_declination):
        """
        used for callibration, sets the declination of the star in the scope
        """
        print('set_star_declination', self)
        self.s_declination = star_declination
        return self.s_declination

    def set_star_azimuth(self):
        print('set_star_azimuth', self)
        s_azimuth = self.s_azimuth = self.Calculations.convert_to_azimuth(self.s_declination, self.s_right_ascension, self.Latitude, self.star_LHA)
        print("star azimuth is", self.s_azimuth)
        return self.s_azimuth

    def set_star_altitude(self):
        print('set_star_altitude', self)
        s_altitude = self.s_altitude = self.Calculations.convert_to_altitude(self.s_declination, self.s_right_ascension, self.Latitude, self.star_LHA)
        print("star altitude is", self.s_altitude)
        return self.s_altitude

    def star_LHA(self):
        star_lha = self.Calculations.local_hour_angle(self.Longitude, self.s_right_ascension)
        self.star_lha = star_lha
        return self.star_lha   
    def set_altitude(self):
        """
        sets the target altitude of the telescope, takes an input from 
        set_declination and set_right_ascension returns in degrees
        """
        self.altitude = self.Calculations.convert_to_altitude( self.declination, self.right_ascension, self.Latitude, self.LHA)
        print('altitude set to', self.altitude)
        if self.altitude < 0:
            self.altitude = self.altitude + 360.0
            return self.altitude 
        else: 
            pass
        return self.altitude

    def get_latitude(self, latitude):
        """
        gets the current latitude of the telescope in degrees
        """
        self.Latitude = latitude
        return self.Latitude

    def get_longitude(self, longitude):
        """
        gets the current longitude of the telescope in degrees
        """
        self.Longitude = longitude
        return self.Longitude

    def get_gast(self):
        """
        function for parsing the greenwich average sidereal time
        """
        gast = self.Calculations.GAST()
        return gast

    def get_local_hour_angle(self):
        """
        function for parsing the local hour angle
        """
        LHA = self.Calculations.local_hour_angle(self.Longitude, self.right_ascension)
        self.LHA = LHA
        return LHA 
 
    def get_altitude(self):
        """
        function for finding the current altitude of the telescope
        """
        self.degrees = self.altitude_encoder.get_degrees()
        self.tele_altitude = self.Calculations.convert_degrees( self.degrees)
        return self.tele_altitude


    def get_azimuth(self):
        """
        function for finding the current azimuth of the telescope
        """
        self.degrees = self.azimuth_encoder.get_degrees()
        self.tele_azimuth = self.Calculations.convert_degrees( self.degrees)
        return self.tele_azimuth

    def azimuth_update(self):
        """
        function that calculates the difference between the current
        and target azimuth/altitude and sets a speed accordingly
        """
        self.azimuth_encoder.altitude_restart()
        self.current_azimuth = self.azimuth_encoder.get_degrees()
        azimuth_error = self.azimuth  - float(self.current_azimuth)
    #    print('goal azimuth', self.azimuth, 'current azimuth', self.azimuth_encoder.get_degrees(), 'difference in azimuth', azimuth_error)
        if azimuth_error >0:
    #        print('positive azimuth')
            self.azimuth_motor.set_direction(1)
        elif azimuth_error > 0:
    #        print('negative azimuth')
            self.azimuth_motor.set_direction(0)
        azimuth_error = abs(azimuth_error)
        self.azimuth_error = azimuth_error
        if azimuth_error >= 0:
            self.azimuth_motor.stopping_motor()
        if azimuth_error >= 20:
            self.azimuth_motor.set_speed(1)
        if azimuth_error >= 40:
            self.azimuth_motor.set_speed(2)
        if azimuth_error >= 80:
            self.azimuth_motor.set_speed(3)
        if azimuth_error >= 160:
            self.azimuth_motor.set_speed(4)
        if azimuth_error >= 280:
            self.azimuth_motor.set_speed(5)
        self.azimuth_error = azimuth_error
        print('debug azimuth', self.current_azimuth, self.azimuth_error, self.azimuth_motor.speed)
        return self.azimuth_error

    def altitude_update(self):
        self.current_altitude = self.altitude_encoder.get_degrees()
        altitude_error = self.altitude - float(self.current_altitude)
        altitude_error = abs(altitude_error)
        self.altitude_error = altitude_error
     #   print('goal altitude:',  self.altitude, 'current altitude:', self.current_altitude, 'difference:', altitude_error)
        if altitude_error >= 0:
     #       print('positive altitude')
            self.altitude_motor.set_direction(0)
        if altitude_error < 0:
     #       print('negative altitude')
            self.altitude_motor.set_direction(1)
        if altitude_error >= 0:
            self.altitude_motor.stopping_motor()
        if altitude_error >= 20:
            self.altitude_motor.set_speed(1)
        if altitude_error >= 40:
            self.altitude_motor.set_speed(2)
        if altitude_error >= 80:
            self.altitude_motor.set_speed(3)
        if altitude_error >= 160:
            self.altitude_motor.set_speed(4)
        print('debug altitude', self.current_altitude, self.altitude_error, self.altitude_motor.speed)
        return self.altitude_error

    def azimuth_direction(self):
        self.azimuth_encoder.altitude_restart()
        self.current_azimuth = self.azimuth_encoder.get_degrees()
        self.azimuth_error = self.azimuth  - float(self.current_azimuth)
        if self.azimuth_error >0:
            print('positive azimuth')
            self.azimuth_motor.set_direction(1)
        elif self.azimuth_error > 0:
            print('negative azimuth')
            self.azimuth_motor.set_direction(0)
        return self.azimuth_error

    def altitude_direction(self):
        self.current_altitude = self.altitude_encoder.get_degrees()
        self.altitude_error = self.altitude - float(self.current_altitude)
        if self.altitude_error >= 0:
            print('positive altitude')
            self.altitude_motor.set_direction(1)
        if self.altitude_error < 0:
            print('negative altitude')
            self.altitude_motor.set_direction(0)
        return self.altitude_error
    
    def diff_of_errors(self):
        """
        function that calculates the difference between the azimuth error and
        the altitude error
        """
        self.e_of_e = self.azimuth_error - self.altitude_error
        return self.e_of_e
    
    def run_go_to_star(self):
        """
        telescope that calls the update function if the altitude of the 
        telescope is not the same as the target altitude and if the azimuth
        is not the same as the target azimuth
        """
        if self.altitude != self.tele_altitude or self.azimuth != self.tele_azimuth:
           self.azimuth_update()
           self.altitude_update() 
                

    def AWSD_control(self, key):
        """
        function that defines the interface for the manual control option
        """
        if len(key) == 1:
            if key >= '1' and key <= '9':
                self.speed = int(key)
                print(self.speed, '\r')
            elif key == 'a':
                self.altitude_motor.set_direction(1)
                self.altitude_motor.set_speed(self.speed)
                print('moving telescope left')
            elif key == 'd':
                self.altitude_motor.set_direction(0)
                self.altitude_motor.set_speed(self.speed)
                print('moving telescope right')
            elif key == 'w':
                self.azimuth_motor.set_direction(1)
                self.azimuth_motor.set_speed(self.speed)
                print('moving telescope up')
            elif key == 's':
                self.azimuth_motor.set_direction(0)
                self.azimuth_motor.set_speed(self.speed) 
                print('moving telescope down')
            else:

                return False

        elif len(key) == 3:
            key = ord(key[2])
            if key == 66: #down
                motor1.stopping_motor()
                motor1.set_direction(0)
                motor1.one_step()
            elif key == 65: #up
                motor1.stopping_motor()
                motor1.set_direction(1)
                motor1.one_step
            elif key == 68: #right
                motor2.stopping_motor()
                motor2.set_direction(0)
                motor2.one_step
            elif key == 67: #left
                motor2.stopping_motor()
                motor2.set_direction(1)
                motor2.one_step
            else:
                return False
        return True

 
    def get_utc_offset_str():
        """
    Returns a UTC offset string of the current time suitable for use in the
    most widely used timestamps (i.e. ISO 8601, RFC 3339). For example:
    10 hours ahead, 5 hours behind, and time is UTC: +10:00, -05:00, +00:00
        """
        # Calculate the UTC time difference in seconds.

        timestamp = time.time()
        time_now = datetime.fromtimestamp(timestamp)
        time_utc = datetime.utcfromtimestamp(timestamp)
        utc_offset_secs = (time_now - time_utc).total_seconds()

        # Flag variable to hold if the current time is behind UTC.
        is_behind_utc = False

        # If the current time is behind UTC convert the offset
        # seconds to a positive value and set the flag variable.
        if utc_offset_secs < 0:
            is_behind_utc = True
            utc_offset_secs *= -1

        # Build a UTC offset string suitable for use in a timestamp.

        if is_behind_utc:
            pos_neg_prefix = "-"
        else:
            pos_neg_prefix = "+"

        utc_offset = time.gmtime(utc_offset_secs)
        utc_offset_fmt = time.strftime("%H", utc_offset)
        utc_offset_str = pos_neg_prefix + utc_offset_fmt

        return utc_offset_str

if __name__ == "__main__":
    telescope = Telescope()
    telescope.get_gast()
    sys.exit(1)
    while True:
        time.sleep(1)
