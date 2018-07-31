

#file for attempting to learn how to parse

class Telescope:
    def __init__(self):
        pass

    def get_altitude(self):
        return "01* 02"

    def get_declination(self):
        target_ra = 0*2
        return "target_ra"

    def get_target_declination(self):
        return "01*02"

    def get_right_ascension(self):
        return "01*02"
    
    def 
    
import time
from datetime import datetime

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
telescope = Telescope()
while True:
    line = input()
    if line == ':Aa#':
        print('start telescope automatic align sequence')
    elif line == 'quit':
        break
    elif line == ':GA#': #returns sDD*MM# or sDD*MM'SS#
        print('get telescope altitude')
        print('s' + telescope.get_altitude() + '#')
    elif line == ':GD#': #returns sDD*MM# or sDD*MM'SS#
        print('get telescope declination')
        print('s' + telescope.get_declination() + '#')
    elif line == ':Gd':  #returns sDD*MM# or SDD*MM'SS#
        print('get target declination')
        print('s' + telescope.get_target_declination() + '#')
    elif line == ':GG#': #returns sHH# or sHH.H#
        print('get UTC offset time')
        print('s' + get_utc_offset_str() + '#")
    elif line == ':GR#': #returns HH:MM.T# or HH:MM:SS#
        print('get telescope RA')
        print('')
    elif line == ':Gr#': #returns HH:MM.T# or HH:MM:SS#
        print('get target RA')
        print('s' + telescope.get_right_ascension() + '#')
    elif line == ':GS#': #returns HH:MM:SS#
        print()
        print('get sidereal time')
    elif line == ':Gg#':
        print('get site longitude')
    elif line == ':Gt#':
        print('get site latitude')
    elif line == ':GZ#':
        print('get telescope azimuth')
    elif line == ':MS#':
        print('slew to target object')
    elif line == ':Q#':
        print('halt all movement')
