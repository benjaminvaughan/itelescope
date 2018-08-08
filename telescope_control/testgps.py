
import serial


ser = serial.Serial('/dev/ttyUSB0', 4800)
while 1:
    line = ser.readline()
    parts = line.split(b',')
    print(parts)
