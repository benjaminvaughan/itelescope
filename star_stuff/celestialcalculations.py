import math
from math import sin,cos,pi

"""
code translated from https://www.codeproject.com/Articles/836784/Motorizing-a-Telescope-Part (source code) 
"""

def compute_alt_alzimuth(date_time,local_sidereal_date_time):
    right_ascension_hours = 0.0
    declination_degrees = 0.0 
    latitude_degrees = 0.0
    local_sidereal_degrees = degrees_from_date_time(local_sidereal_date_time)
    right_ascention_degrees = h2d(right_ascention)
    hours_angle_degrees = local_sidereal_degrees - right_ascension_degrees 
    if hours_angles_degrees < 0:
        hour_angle_degrees += 360
    hour_angle_radians = d2r(hour_angle_degrees)
    declination_radians = d2r(declination_degrees)
    latitude_radians = radians_from_degrees(latitude_degrees)
    #altitude = asin( sin(dec) * sin(lat) + cos(dec) *cos(lat) * cos(ha)
    azimuth_radians = acos(sin(declination_radians)-sin(altitude_radians)*sin(latitude_radians)) / (cos(altitude_radians)*cos(latitude_radians))
    altitude_degrees = r2d(altitude_radians)
    azimuth_degrees = r2d(azimuth_radians)
    if sin(hour_angle_radians) > 0:
        azimuth_degrees = 360 - azimuth_degrees
    return azimuth_degrees, altitude_degrees

def degrees_from_date_time(date_time):
    return date_time,time_of_day,total_hours * 360 / 24

def compute_right_ascention_declination(local_sidereal_degrees,
                                        azimuth_degrees,
                                        altitude_degrees,
                                        latitude_degrees,
                                        right_ascention_hours,
                                        declination_degrees):
    latitude_radians = radians_from_degrees(latitude_degrees)
    altitude_radians = radians_from_degrees(altitude_degrees)
    azimuth_radians = radians_from_degrees(azimuth_degrees)
    declination_radians = asin(cos(azimuth_radians*cos(altitude_radians)*sin(latitude_radians))) + pi
    declination_degrees = degrees_from_radians(declination_radians)
    right_ascention_hours = 0.0
    # FIXME: this does not return anything. local_sidereal_degrees is not used

def date_time_calculate_local_sidereal_time(longitude,date_time_utc_now):
    """
    epoch = new date_time(2000,1,1,12,0,0,date_time_kind.Utc)
    since_epoch = utc_now - epoch
    hours = (18.697374558 + 24.06570982441908 * since_epoch.total_days) 24 + longitude / 15.0
    while hours < 0:
        hours += 24
    while hours > 0:
        hours -= 24
    local_sidereal_time_spam = time_span.from_hours(hours)
    return utc_now.date + local_sidereal_time_span
    """
    pass

if __name__ == "__main__":
    """
    Some tests
    """
    angle_deg = 73.0
    angle_rad = radians_from_degrees(angle_deg)
    print("angle_deg", angle_deg, "angle_rad", angle_rad)
    angle_deg = degrees_from_radians(angle_rad)
    print("angle_deg", angle_deg, "angle_rad", angle_rad)
