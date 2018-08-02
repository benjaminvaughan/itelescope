#from encoder_class import Encoder
#from motor_class import Motor
import datetime
#import pigpio
import sys

#used for talking with meadle LX200 Protocol

class Telescope():
    def __init__(self):
        #self.altitude_encoder = Encoder()
        #self.altitide_motor = Motor()
        #self.azimuth_encoder = Encoder()
        #self.azimuth_motor = Motor()
        pass
    
    def set_azimuth(self, target_azimuth):
        self.target_azimuth = target_azimuth
        target_azimuth = "01*02"
        print('testing set azimuth')
        return target_azimuth
    
    def set_altitude(self, target_altitude):
        self.target_altitude = target_altitude
        target_altitude = "01*02"
        print('testing set altitude')
        return target_altitude
    
    def get_gast(self):
        fmt =
        year =
        month =
        day =
        day = day - 1
        UT =
        JD_midnight = 367*year - 7(K+(M+9/12))4 + 275*month/9 + 1721013.5 + UT/24
        D = JD_mightnit - 2451545.0
        GMST = 6.697374558 + 0.06570982441908 * D + 1.00273790935
        moon = 125.04 - 0.052954
        sun = 280.47 + 0.98565
        obliquity = 23.4393 - 0.0000004
        nutation = 0.000319*sin(moon) - 0.000024* sin(2*sun)
        eqeq = nutation * cos(obliquity)
        gast = GMST + eqeq
        
    def get_altitude(self):
        altitude = self.altitude_encoder.print_degrees()
        altitude = altitude.split(".")
        arcminutes = int(altitude[1]) // 60.0
        arcminutes = arcminutes.split(".")
        arcseconds = int(arcminutes[1]) // 60.0
        
        return "01*02"

    def get_azimuth(self):
        azimuth = self.azimuth_encoder.print_degrees()
        azimuth = azimuth.split(".")
        arcminutes = int(azimuth[1]) // 60.0
        arcminutes = arcminutes.split(".")
        arcseconds = int(arcminutes[1]) // 60.0
        arcseconds = 
        return "01*02"
    
        
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
        
