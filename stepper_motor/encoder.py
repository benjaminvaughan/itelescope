import time
import pigpio
from time import sleep
clk = 13
dt = 12

pi = pigpio.pi()
pi.set_mode(clk, pigpio.INPUT)
pi.set_mode(dt, pigpio.INPUT)
pi.set_pull_up_down(clk, pigpio.PUD_DOWN)
pi.set_pull_up_down(dt, pigpio.PUD_DOWN)

counter = 0
clklaststate = pi.read(clk) 
try:

        while True:
                clkstate = pi.read(clk)
                dtstate = pi.read(dt)
                if clkstate != clklaststate:
                        if dtstate != clkstate:
                                counter += 1
                        else:
                                counter -= 1
                                
                        print counter
                clklaststate = clkstate
                sleep(delay)

finally:
        GPIO.clean()
        


counterpercent = counter / 4096
stepspercent = steps / 2592


def encodercheck():
        while counterpercent != stepspercent:
                clkstate = pi.read(clk)
                dtstate = pi.read(dt)
                if clkstate != clklaststate:
                        if dtstate != clkstate:
                                forwards(delay,1)
                        else:
                                backwards(delay,1)
                                
                        print(counter)
                clklaststate = clkstate
