from motor_class import Motor
from encoder_class import Encoder
from telescope_class import Telescope
import pigpio
import time
import sys
from calculations import Calculations

class digital_setting_circle():
    def __init__(self):
        pi = pigpio.pi()
        altitude_encoder = Encoder(16, 19, 26, 1)
        azimuth_encoder = Encoder(20, 21, 12, 2)
        azimuth_motor = Motor(10, 9, 17, 27, 22, pi)
        altitude_motor = Motor(24, 23, 25, 8 ,7, pi)
        self.az_degrees = azimuth_encoder.get_degrees()
        self.alt_degrees = altitude_encoder.get_degrees()
        self.target_az = 0
        self.target_alt = 0
        self.alt_error = 0
        self.az_error = 0
        calculations = Calculations()        

    def setting_target(azimuth, altitude):
        self.az_error = self.target_az - self.az_degrees
        self.alt_error = self.target_alt - self.alt_degrees
        print( az_error, alt_error)

    def setting_alt_az(declination, right_ascension):
        telescope.get_gast()
        telescope.set_declination(declination)
        telescope.set_right_ascension(right_ascension):
        telescope.get_local_hour_angle()
        self.target_alt = telescope.set_altitude()
        self.target_az = telescope.set_azimuth()

    def running_DSC():
        self.setting_target()
        if self.az_error != 0 or self.alt_error != 0:
            print(self.setting_target)
            time.sleep(1)
