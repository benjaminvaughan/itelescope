import time
import pigpio
from time import sleep
channel_a = 22
channel_b = 23

pi = pigpio.pi()
pi.set_mode(channel_a, pigpio.INPUT)
pi.set_mode(channel_b, pigpio.INPUT)
pi.set_pull_up_down(channel_a, pigpio.PUD_DOWN)
pi.set_pull_up_down(channel_b, pigpio.PUD_DOWN)

counter = 0
clklaststate = pi.read(clk) 
try:

        while True:
                clkstate = pi.read(channel_a)
                dtstate = pi.read(channel_b)
                if clkstate != clklaststate:
                        if dtstate != clkstate:
                                counter += 1
                        else:
                                counter -= 1
                                
                        print counter
                clklaststate = clkstate
                sleep(.1)
except KeyboardInterrupt Ctrl-C:
        print('program stopped by keyboard interrupt')

finally:
        pigpio.stop()  #replace this with pigpio equivalent.

