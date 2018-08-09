
import serial




class GPS_parse(object):
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyUSB0', 4800)

    def determining_name(self):
        self.line = self.ser.readline().decode()
        self.string = self.line.split(",")
        self.name = self.string[0]
        if self.name == '$GPGGA':
            print(self.name)
            Message_ID = self.string[0] #protocol header
            UTC_Position = self.string[1] #hhmmss.sss
            latitude = self.string[2] #dddmm.mmmm
            N_or_S_indicator = self.string[3] #N = north, S = South
            longitude = self.string[4] #dddmm.mmmm
            E_or_W_indicator = self.string[5] #E = east, W = West
            return latitude, longitude, E_or_W_indicator, N_or_S_indicator, UTC_Position
        elif self.name == '$GPGSV':
            print(self.name)
            satellites = self.string[3] #finds the number of satellites
            return satellites
        elif self.name == '$GPRMC':
            print(self.name)
            UTC3 = self.string[1] 
            validity = self.string[2] #checks the validity of the data
            if validity == 'V':
                return False
            elif validity == 'A':
                pass
            else:
                return False
            latitude3 = self.string[3] 
            NorS3 = self.string[4]
            longitude3 = self.string[5]
            EorW3 = self.string[6]
            date = self.string[9]  
        elif self.name == '$GPGLL':
            print(self.name)
            latitude2 = self.string[1]
            NorS2 = self.string[2]
            longitude2 = self.string[3]
            EorW2 = self.string[4]
            UTC2 = self.string[5]
            VorNV = self.string[6] #stands for valid or not valid
            return latitude2, NorS2, longitude2, EorW2, UTC2, VorNV
        elif self.name == '$GPGSA':
            print(self.name)
            if self.line == self.name:
                return False
                mode = self.string[2] #another check to see if data is valid
                if mode == '1':
                    return False
                elif mode == '2' or '3':
                    return True
                else:
                    return False 
        else:
            return False          
  
if __name__ == '__main__':
     gps_parse = GPS_parse()
     while True:
        print(gps_parse.determining_name())
