

#document to do angle conversions

import math

class angle_conversions(self):

    def __init__(self):
        self.radians = 0
        self.degrees = 0
        self.hours = 0
        self.arcseconds = 0

    def radians_to_degrees(radians):
        degrees = math.degrees(radians)

    def degrees_to_radians(degrees):
        radians = math.radians(degrees)

    def hours_to_degrees(hours):
        degrees = hours * 15.0

    def degrees_to_hours(degrees):
        hours = degrees * 24.0 / 360.0

    def degrees_to_arcseconds(degrees):
        arcseconds = degrees * 3600.0

    def arcseconds_to_degrees(arcseconds):
        degrees = arcseconds / 3600.0

    def hours_to_radians(hours):
        radians = degrees_radians(hours_to_degrees(hours))

    def radians_to_hours(radians):
        hours = degrees_to_hours(radians_to_degrees(radians))
        
    def arcseconds_to_radians(arcseconds):
        radians = degrees_to_radians(arcseconds_to_degrees(arcseconds))

    def radians_to_arcseconds(radians):
        arcseconds = degrees_to_arcseconds(radians_to_degrees(radians))

    def arcseconds_to_hours(arcseconds):
        hours = degrees_to_hours(arcseconds_to_degrees(arcseconds))

    def hours_to_arcseconds(hours):
        degrees_to_arcseconds(hours_to_degrees(hours))

