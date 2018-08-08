
import serial




class GPS_parse(object):
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyUSB0', 4800)

    def global_positioning_system(self):
        self.line = self.ser.readline().decode()
        self.string = self.line.split(",")
        self.name = self.string[0]
        if self.name == '$GPGGA':
            print(self.line)
            print('elements:', len(self.string))
            Message_ID = self.string[0] #protocol header
            UTC_Position = self.string[1] #hhmmss.sss
            latitude = self.string[2] #dddmm.mmmm
            N_or_S_indicator = self.string[3] #N = north, S = South
            longitude = self.string[4] #dddmm.mmmm
            E_or_W_indicator = self.string[5] #E = east, W = West
            #return latitude
            #return longitude
            #return N_or_S_indicator
            #return E_or_W_indicator
            for i in range(0, len(self.string)):
                print('element',i, self.string[i])
            for part in self.string:
                print(part)
        if self.name == 'GPGSV':
            print('elements', len(self.string))

if __name__ == '__main__':
     gps_parse = GPS_parse()
     while True:
        gps_parse.global_positioning_system()
