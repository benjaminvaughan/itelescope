from encoder_class import Encoder
import datetime
import math
import numpy as np
from angle_conversions import angle_conversions

class Calculations():
    def __init__(self):
        self.datetime = datetime
        self.current_time = datetime.datetime.now()
        self.year = self.current_time.year
        self.month = self.current_time.month
        self.day = self.current_time.day
        self.ut_current_time = self.datetime.datetime.utcnow()
        self.ut_hours = self.ut_current_time.hour
        self.ut_minutes = self.ut_current_time.minute
        self.ut_minutes_fraction = self.ut_minutes / 60.0
        self.UT = self.ut_hours + self.ut_minutes_fraction
        self.angle_conversions = angle_conversions()

    def get_julian_date(self):
       JD_midnight = 367*self.year - 7*(self.year+(self.month+9/12))*4 + 275*self.month/9 + 1721013.5 + self.UT/24
       self.D = JD_midnight - 2451545.0
       return self.D

    def get_GMST(self):
       GMST = 6.697374558 + 0.06570982441908 * self.D + 1.00273790935
       return GMST
   
    def GAST(self):
        self.get_julian_date()
        self.longitude_of_ascending_moon()
        self.mean_longitude_of_sun()
        self.obliquity()
        self.nutation()
        self.gast = self.get_GMST() + self.equation_of_equinoxes()
        return self.gast
   
    def obliquity(self):
        self.obliquity =  23.4393 - 0.0000004 * self.D
        return self.obliquity

    def nutation(self):
        self.n = -0.000319 * np.sin(self.moon) - 0.000024 * np.sin(2*self.sun)
        return self.n  
    def longitude_of_ascending_moon(self):
        self.moon = 125.04 - 0.052954 * self.D
        return self.moon

    def mean_longitude_of_sun(self):
        self.sun = 280.47 + 0.98565 * self.D
        return self.sun

    def equation_of_equinoxes(self):
        self.eqeq = self.n * np.cos(self.obliquity)
        return self.eqeq

    def G_M_S_T(self):
        self.gmst = 18.697374558 + 24.0657098244
        return self.gmst

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
        self.LHA = (self.gast - right_ascension)*15- longitude
        return self.LHA

    def convert_local_hour_angle(self):
        self.lha_rad = self.angle_conversions.degrees_to_radians(self.LHA)
        return self.lha_rad

    def convert_to_altitude(self, declination, right_ascension, latitude, LHA):
        """ 
        converts right ascension and declination into altitude
        arguments: floats
        returns: degrees as a float
        """
        self.convert_local_hour_angle()
        self.convert_latitude(latitude)
        self.convert_declination(declination)
        altitude1 = -1*np.sin(self.lha_rad)
        altitude2 = np.tan(self.declination_rad)*np.cos(self.lat_rad)
        altitude3 = np.sin(self.lat_rad)*np.cos(self.lha_rad)
        altitude4 = altitude2 - altitude3
        altitude5 = altitude1/altitude4
        target_altitude = math.atan2(altitude1,altitude4)
        target_altitude = self.angle_conversions.radians_to_degrees(target_altitude)
        return target_altitude

 
    def convert_latitude(self, latitude):          
        self.lat_rad = self.angle_conversions.degrees_to_radians(latitude)
        return self.lat_rad
    def convert_declination(self, declination):       
        self.declination_rad = self.angle_conversions.degrees_to_radians(declination)
        return self.declination_rad
   
    def convert_to_azimuth(self, declination, right_ascension, Latitude, LHA):
        """converts right ascension and declination into latitude
        arguments: floats
        returns: degrees as a float
        """
        self.convert_declination(declination)
        self.convert_latitude(Latitude)
        self.convert_local_hour_angle()
        azimuth1 = np.cos(self.lha_rad)*np.cos(self.declination_rad)*np.cos(self.lat_rad)
        azimuth2 = np.sin(self.declination_rad)*np.sin(self.lat_rad)
        target_azimuth = math.asin(azimuth1 + azimuth2)
        target_azimuth = float(target_azimuth)
        target_azimuth = self.angle_conversions.radians_to_degrees(target_azimuth)  
        return target_azimuth       
