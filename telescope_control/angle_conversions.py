

#document to do angle conversions

import math

class angle_conversions():

    def __init__(self):
        self.radians = 0
        self.degrees = 0
        self.hours = 0
        self.arcseconds = 0

    def radians_to_degrees(self, radians):
        #function that converts radians to degrees
        degrees = math.degrees(radians)
        return degrees

    def degrees_to_radians(self, degrees):
        #function that converts degrees to radians
        radians = math.radians(degrees)
        return radians
 
    def hours_to_degrees(self, hours):
        #function that converts hours to degrees
        self.degrees = hours * 15.0
        return self.degrees

    def degrees_to_hours(self, degrees):
        #function that converts degrees to hours
        hours = degrees * 24.0 / 360.0
        return hours

    def degrees_to_arcseconds(self, degrees):
        #function that converts degrees to arcseconds
        arcseconds = degrees * 3600.0
        return arcseconds

    def arcseconds_to_degrees(self, arcseconds):
        #function that converts arcseconds to degrees
        degrees = arcseconds / 3600.0
        return degrees

    def hours_to_radians(self, hours):
        #function that converts hours to radians
        self.radians = self.degrees_to_radians(self.hours_to_degrees(hours))
        return self.radians

    def radians_to_hours(self, radians):
        #function that converts radians to hours
        hours = degrees_to_hours(radians_to_degrees(radians))
        return hours
        
    def arcseconds_to_radians(self,arcseconds):
        #function that converts arcseconds to radians
        radians = degrees_to_radians(arcseconds_to_degrees(arcseconds))
        return radians

    def radians_to_arcseconds(self, radians):
        #function that converts radians to arcseconds
        arcseconds = degrees_to_arcseconds(radians_to_degrees(radians))
        return arcseconds

    def arcseconds_to_hours(self, arcseconds):
        #function that converts arcseconds to hours
        hours = degrees_to_hours(arcseconds_to_degrees(arcseconds))
        return hours

    def hours_to_arcseconds(self, hours):
        #function that converts hours to arcseconds
        degrees_to_arcseconds(hours_to_degrees(hours))

    def degrees_to_degrees2(self, degrees):
        #function that converts decimal form of degrees into a string DD:MM:SS
        arc_minutes = degrees_to_arcminutes(degrees - int(degrees))
        arc_seconds = arcminutes_to_arcseconds(arc_minutes - int(arc_minutes))
        degrees_str = 'degrees + "'" + arc_minutes + '"' + arc_seconds'
        return degrees_str
    
    def degrees_to_arcminutes(self, degrees):
        #converts degrees to arcminutes
        arc_minutes = degrees / 60.0
        return arc_minutes

    def arcminutes_to_arcseconds(self, arc_minutes):
        #converts arcminutes to arcseconds
        arcseconds = arc_minutes / 60.0
        return arcseconds

    def hours_to_degrees2(self, hours):
        #function that converts a string of HH:MM:SS into decimal degrees
        hour_str = hours.split(':')
        while 1:
            if len(hour_str) == 3:
                   break
            else:
                   print('invalid input please use the correct format')
        Hours = hour_str[0]
        float_hours = float(Hours)
        Minutes = hour_str[1]
        float_min = float(Minutes)
        Seconds = hour_str[2]
        float_sec = float(Seconds)
        Minute_hours = self.minutes_to_hours(float(Minutes))
        Second_hours = self.seconds_to_hours(float(Seconds))
        Hours = float(Hours) + Minute_hours + Second_hours
        return Hours

    def minutes_to_hours(self, minutes):
        #function that converts minutes to hours
        hours = minutes /60.0
        return hours

    def seconds_to_hours(self, seconds):
        #function that converts seconds to hours
        hours = seconds / 3600.0
        return hours

    def degrees_to_degrees(self, degrees):
        #function that converts a string of degrees DD:MM:SS into decimal format
        degrees2 = degrees.split(':')
        while 1:
            if len(degrees2) != 3:
                print('invalid format, please use the correct format')
            if len(degrees2) == 3:
                break
        degrees_seconds = degrees2[2]
        degrees_minutes = degrees2[1]
        degrees_degrees = degrees2[0]
        degrees_minutes = float(degrees_minutes) / 60.0
        degrees_seconds = float(degrees_seconds) / 3600.0
        degrees2 = float(degrees_degrees) + degrees_minutes + degrees_seconds
        return degrees2


