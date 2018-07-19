#1/usr/bin/env python
#for quadrature encoder

import pigpio
import time

channel_a = 23
channel_b = 22

def setup():
    global counter
    global last_channel_b, current_channel_b
    pi = pigpio.pi()
    pi.set_mode(channel_a, pigpio.INPUT)
    pi.set_mode(channel_b, pigpio.INPUT)
    counter = 0
    last_channel_b = 0
    current_channel_b = 0

def rotary_deal():
    global counter
    global last_channel_b, current_channel_b
    flag = 0
    last_channel_b = pi.read(channel_b)
    while(not pi.read(channel_b):
          current_channel_b = pi.read(channel_b)
          flag = 1
    if flag == 1:
          flag = 0
          if (last_channel_b == 0) and (current_channel_b == 1):
        counter = counter + 1
          if (last_channel_b == 1) and (current_channel_b == 0):
        counter = counter - 1

def main():
          print_message()
          while True:
        rotary)deal()

if __name__ == '__main__':
    setup()
    try:
        main()

    except KeyboardInterrupt:
        print(program was interrupted by user)
    
