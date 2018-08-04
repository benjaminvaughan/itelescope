

#document to do angle conversions

import math

class angle_conversions():

    def __init__(self):
        self.radians = 0
        self.degrees = 0
        self.hours = 0
        self.arcseconds = 0

    def radians_to_degrees(self, radians):
        degrees = math.degrees(radians)
        return degrees

    def degrees_to_radians(self, degrees):
        radians = math.radians(degrees)
        return radians
 
    def hours_to_degrees(self, hours):
        self.degrees = hours * 15.0
        return self.degrees

    def degrees_to_hours(self, degrees):
        hours = degrees * 24.0 / 360.0

    def degrees_to_arcseconds(self, degrees):
        arcseconds = degrees * 3600.0

    def arcseconds_to_degrees(self, arcseconds):
        degrees = arcseconds / 3600.0

    def hours_to_radians(self, hours):
        self.radians = self.degrees_to_radians(self.hours_to_degrees(hours))
        return self.radians

    def radians_to_hours(self, radians):
        hours = degrees_to_hours(radians_to_degrees(radians))
        
    def arcseconds_to_radians(self,arcseconds):
        radians = degrees_to_radians(arcseconds_to_degrees(arcseconds))

    def radians_to_arcseconds(self, radians):
        arcseconds = degrees_to_arcseconds(radians_to_degrees(radians))

    def arcseconds_to_hours(self, arcseconds):
        hours = degrees_to_hours(arcseconds_to_degrees(arcseconds))

    def hours_to_arcseconds(self, hours):
        degrees_to_arcseconds(hours_to_degrees(hours))

