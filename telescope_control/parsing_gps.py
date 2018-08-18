#!/usr/bin/python3

#for calculating moving average of latitude and longitude as well as parsing the gps data
import serial




class GPS_parse(object):
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyACM0', 115200)
        self.longitude = 0
        self.longitude2 = 0 
        self.longitude3 = 0 
        self.latitude = 0 
        self.latitude2 = 0
        self.latitude3 = 0 

    def determining_name(self):
        """
        function that parses the GPS setences into usable data
        """
        self.line = self.ser.readline().decode()
        self.string = self.line.split(",")
        self.name = self.string[0]
        self.name_list = list(self.name)
        self.name_start = self.name_list[0]

        if self.name == '$GPGLL':
            if self.string[1] != '':
                self.latitude2 = float(self.string[1])
                self.NorS2 = self.string[2]
                self.longitude2 = float(self.string[3])
                self.EorW2 = self.string[4]
                self.UTC2 = self.string[5]
                VorNV = self.string[6] #stands for valid or not valid
            else:
                print('no longitude, latitude data')
        elif self.name_start == '$':
            pass
        else:
            print('no longitude, latitude data')

    def longitude_latitude(self):
        """ 
        function that calculates the moving average of the longitude and 
        latitude
        """ 
        self.determining_name()
        if self.longitude2 == 0 and self.latitude2 == 0:
            return None
        else:
            longitude = self.longitude2 / 100.0
            latitude = (self.latitude2 / 100.0)
        return longitude, latitude


if __name__ == '__main__':
     print('this is a test function')
     gps_parse = GPS_parse()
     while True:
         gps_parse.longitude_latitude()
