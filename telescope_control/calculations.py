from encoder_class import Encoder
import datetime
import math
import numpy as np
class Calculations():
    def __init__(self):
        self.LHA = LHA = 40.0  
#   current_time = datetime.datetime.now()
 #   year = current_time.year
 #   month = current_time.month
 #   day = current_time.day
 #   ut_current_time = datetime.datetime.utcnow()
 #   ut_hours = ut_current_time.hours
 #   ut_minutes = ut_current_time.minutes
 #   ut_minutes_fraction = ut_minutes / 60.0
 #   UT = ut_hours + ut_minutes_fraction
 #   JD_midnight = 367*year - 7*(year+(month+9/12))*4 + 275*month/9 + 1721013.5 + UT/24
 #   D = JD_mightnit - 2451545.0


    def get_julian_date(self):
       JD_midnight = 367*year - 7*(year+(month+9/12))*4 + 275*month/9 + 1721013.5 + UT/24
    def get_GMST(self):
       GMST = 6.697374558 + 0.06570982441908 * D + 1.00273790935
    
    def GAST(self):
        gast = self.GMST + self.eqeq

    def nutation(self):
        n = -0.000319 * sin(moon) - 0.000024 * sin(2*sun)
    def longitude_of_ascending_moon(self):
        moon = 125.04 - 0.052954 * D

    def mean_longitude_of_sun(self):
        sun = 280.47 + 0.98565 * D

    def equation_of_equinoxes(self):
        eqeq = self.nutation *cos(self.obliquity)

    def G_M_S_T(self):
        gmst = 18.697374558 + 24.0657098244


    def convert_degrees(self, degrees):
        """
        Convert degrees into a string DD*MM'SS
        Arguments: degrees float
        Returns string
        """
        arcminutes = degrees - int(degrees)
        arcminutes = arcminutes / 60.0
        arcseconds = arcminutes - int(arcminutes)
        arcseconds = arcseconds / 60.0
        result = ( 'degrees' + '*' + 'arcminutes' + "'" + 'arcseconds')
        return result

    def local_hour_angle(self, right_ascension, longitude):
        LHA = (self.gast - right_ascension)*15- longitude
        return LHA
    def convert_to_altitude(self, declination, right_ascension, latitude):
        """ 
        converts right ascension and declination into altitude
        arguments: floats
        returns: degrees as a float
        """
        target_altitude = np.arcsin(np.cos(40)*np.cos(declination)*np.cos(latitude)+ np.sin(declination)*np.cos(40))
        target_altitude = float(target_altitude)
        return target_altitude
    def convert_to_azimuth(self, declination, right_ascension, latitude):
        """converts right ascension and declination into latitude
        arguments: floats
        returns: degrees as a float
        """

        target_azimuth = np.arctan((-1*np.sin(40))/(np.tan(declination)*np.cos(latitude)-np.sin(latitude)*np.cos(40)))
        target_azimuth = float(target_azimuth)
        return target_azimuth       
