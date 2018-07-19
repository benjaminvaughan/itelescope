#1/usr/bin/env python

import pigpio
import time

pi = pigpio.pi()
channel_a = 23
channel_b = 22

counter = 0
flag = 0
last_channel_b = 0
current_channel_b = 0

def setup():
    pi = pigpio.pi()
    pi.set_mode(channel_a, pigpio.INPUT)
    pi.set_mode(channel_b, pigpio.INPUT)

def rotary_deal():
    global flag
    global current_channel_b
    global counter
    last_channel_b = pi.read(channel_b)
    while(not pi.read(channel_b)):
        current_channel_b = pi.read(channel_b)
        flag = 1
    if flag == 1:
        flag = 0
        if (last_channel_b == 0) and (current_channel_b ==1):
            counter =+ 1
            print(counter)
        if (last_channel_b == 1) and (current_channel_b == 0):
            counter =- 1
            print(counter)

def clear(ev=None):
    counter = 0
    print(counter)
    time.sleep(1)

def loop():
        global counter
        while True:
            rotary_deal()
            print(counter)

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        print("\nCtrl-C presssed. Stopped pigpio and exiting...")
    
