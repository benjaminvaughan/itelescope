gfrom motor_class import Motor
from encoder_class import Encoder
from telescope_class import Telescope
import pigpio
import time
import datetime
import sys
from calculations import Calculations

if __name__ == '__main__':
    print('enter mode you would like to use')
    line = input()
    if line == 'mode2':
        print('you are now running manual mode')
        speed = 0
        while True:
            key = click.getchar()
            if len(key) == 1:
                if key >= '1' and key <= '9':
                    speed = int(key)
                    print('speed %d %d' % (speed, ord(key)))
                if key == 'q':
                    motor1.stopping_motor()
                    motor2.stopping_motor()
                    break
                if key == 'a':
                    motor1.set_direction(1)
                    motor1.set_speed(speed)
                if key == 'd':
                    motor1.set_direction(0)
                    motor1.set_speed(speed)
                if key == 'w':
                    motor2.set_direction(1)
                    motor2.set_speed(speed)
                if key == 's':
                    motor2.set_direction(0)
                    motor2.set_speed(speed)
    if line == 'mode1':
        print('you are now running goto mode')
        telescope = Telescope()
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
