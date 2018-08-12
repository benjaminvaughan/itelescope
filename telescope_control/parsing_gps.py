#for calculating moving average of latitude and longitude as well as parsing the gps data
import serial




class GPS_parse(object):
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyUSB0', 4800)
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
        if self.name == '$GPGGA':
            valid_or_invalid = self.string[7]
            if float(valid_or_invalid) > 3:
                Message_ID = self.string[0] #protocol header
                self.UTC_Position = self.string[1] #hhmmss.sss
                self.latitude = float(self.string[2]) #dddmm.mmmm
                self.N_or_S_indicator = self.string[3] #N = north, S = South
                self.longitude = float(self.string[4]) #dddmm.mmmm
                self.E_or_W_indicator = self.string[5] #E = east, W = West
            else:
                return False
        elif self.name == '$GPGSV':
            self.satellites = self.string[3] #finds the number of satellites
            if float(self.satellites) < 3:
                return False
            else:
                return self.satellites
        elif self.name == '$GPRMC':
            self.UTC3 = self.string[1] 
            validity = self.string[2] #checks the validity of the data
            if validity == 'V':
                return False
            elif validity == 'A':
                pass
            else:
                return False
            self.latitude3 = float(self.string[3]) 
            self.NorS3 = self.string[4]
            self.longitude3 = float(self.string[5])
            self.EorW3 = self.string[6]
            self.date = self.string[9]
        elif self.name == '$GPGLL':
            self.latitude2 = float(self.string[1])
            self.NorS2 = self.string[2]
            self.longitude2 = float(self.string[3])
            self.EorW2 = self.string[4]
            self.UTC2 = self.string[5]
            VorNV = self.string[6] #stands for valid or not valid
        elif self.name == '$GPGSA':
            if self.line == self.name:
                return False
                mode = self.string[2] #another check to see if data is valid
                if mode == '1':
                    return False
                elif mode == '2' or '3':
                    return True
                    print(mode)
                else:
                    return False 
        else:
            return False          

    def longitude_latitude(self):
        """ 
        function that calculates the moving average of the longitude and 
        latitude
        """ 
        self.determining_name()
        if not self.determining_name():
            pass
        else:
            longitude = (self.longitude2 + self.longitude3 + self.longitude) / 3.0
            latitude = (self.latitude2 + self.latitude3 + self.latitude) / 3.0
            return longitude, latitude


if __name__ == '__main__':
     #this is a test function
     gps_parse = GPS_parse()
     while True:
        if gps_parse.determining_name():
            print(gps_parse.longitude_latitude())
        else: 
            print('this data is invalid')
