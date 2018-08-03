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
    print('enter azimuth')
    line = input()
    degrees = float(line)
    print('you entered %f' % degrees)
    telescope.set_azimuth(degrees)
    print('enter azimuth')
    line = input()
    degrees = float(line)
    telescope.set_altitude(degrees)
    telescope.get_azimuth()
    telescope.get_altitude()

While True:
    telescope.update()
    time.sleep(1)
