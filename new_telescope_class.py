from encoder_class import Encoder
from motor_class import Motor
import datetime
import pigpio
import sys

#used for talking with meadle LX200 Protocol

class Telescope():
    def __init__(self):
        self.altitude_encoder = Encoder()
        self.altitide_motor = Motor()
        self.azimuth_encoder = Encoder()
        self.azimuth_motor = Motor()
        pass

    def 
    
    def set_azimuth(self, target_azimuth):
        azimuth = Calculations.convert_to_azimuth(self.declination, self.right_ascension, self.latitude)
        
    
    def set_altitude(self, target_altitude):
        altitude = Calculations.convert_to_altitude(self.declination, self.right_ascension, self.latitude)
    
    
    def get_gast(self):
        gast = Calculations.GAST()
        return gast
    
    def get_altitude(self):
        degrees = altitude_encoder.get_degrees()
        tele_altitude = calculations.convert_degrees(degrees)
        return tele_altitude


    def get_azimuth(self):
        degrees = azimuth_encoder.get_degrees()
        tele_azimuth = calculations.convert_degrees(degrees)
        return tele_azimuth
        
    def update(self):
        self.current_altitude = self.altitude_encoder.print_degrees()
        altitude_error = self.target_altitude - self.current_altitude
        self.current_azimuth = self.azimuth_encoder.print_degrees()
        azimuth_error = self.target_azimuth - self.current_azimuth
        if azimuth_error >0:
            print('positive azimuth')
            azimuth_motor.set_direction(1)
        elif azimuth_error >0:
            print('negative azimuth')
            azimuth_motor.set_direction(0)
        if altitude_error >= 0:
            print('positive altitude')
            self.altitude_motor.set_direction(1)
        if altitude_error < 0:
            print('this is a negative number')
            self.altitude_motor.set_direction(0)
        altitude_error = abs(altitude_error)
        azimuth_error = abs(azimuth_error)
        if azimuth_error >= 0:
            azimuth_motor.set_speed(6)
        if azimuth_error >= 200:
            azimuth_motor.set_speed(5)
        if azimuth_error >= 400:
            azimuth_motor.set_speed(4)
        if azimuth_error >= 500:
            azimuth_motor.set_speed(3)
        if azimuth_error >= 600:
            azimuth_motor.set_speed(2)
        if azimuth_error >= 700:
            azimuth_motor.set_speed(1)
        if altitude_error >= 0:
            altitude_motor.set_speed(6)
        if altitude_error >= 200:
            altitude_motor.set_speed(5)
        if altitude_error >= 400:
            altitude_motor.set_speed(4)
        if altitude_error >= 500:
            altitude_motor.set_speed(3)
        if altitude_error >= 600:
            altitude_motor.set_speed(2)
        if altitude_error >= 700:
            altitude_motor.set_speed(1)

    def run_go_to_star():
        if altitude != tele_altitude:
            self.update()
        elif azimuth !- tele_azimuth:
            self.update()

    def AWSD_control():
        key == click.getchar()
         if key == 'a':
             motor1.set_direction(1)
             motor1.set_speed(1)
        if key == 'd':
            motor1.set_direction(0)
            motor1.set_speed(1)
        if key == 'w':
            motor2.set_direction(1)
            motor2.set_speed(1)
        if key -- 's':
            motor2.set_direction(0)
            motor2.set_speed(1)

        if len(key) == 3:
            key = ord(key[2])
            if key == 66: #down
                motor1.stopping_motor()
                motor1.set_direction(0)
                motor1.one_step()
            if key == 65: #up
                motor1.stopping_motor()
                motor1.set_direction(1)
                motor1.one_step
            if key == 68: #right
                motor2.stopping_motor()
                motor2.set_direction(0)
                motor2.one_step
            if key == 67: #left
                motor2.stopping_motor()
                motor2.set_direction(1)
                motor2.one_step
            
        
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
        telescope.update()
        
