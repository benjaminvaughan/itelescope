
from time import sleep
import pigpio

DIR = 5 # direction GPIO pin
step = 6 # step GPIO pin
#switch = 16 # GPIO pin of switch

#connect to pigpiod daemon
pi = pigpio.pi()

pi.set_mode(DIR, pigpio.OUTPUT)
pi.set_mode(step, pigpio.OUTPUT)

###pi.set_mode(switch,pio.INPUT)
#pi.set_pull_up_down(switch, pigpio.PULL_DOWN)

mode = (13,19,26) #microstep resolution
resolution = {'Full':(0,0,0),
	   'Half':(1,0,0),
	   '1/4':(0,1,0),
	   '1/8':(1,1,0),
	   '1/16':(0,0,1),
	   '1/32':(1,0,1)}

for i in range(3):
    pi.write(mode[i], resolution['Full'][i])

pi.set_PWM_dutycycle(step,128) #PWM 1/2 on 1/2 off
pi.set_PWM_frequency(step,1000) #500 pulses per second

try:
    while True:
        # pi.write(DIR, pi.read(switch)) # set direction
        #pi.write(DIR,0)
        sleep(1)
except KeyboardInterrupt:
    print("\nCtrl-C presssed. Stopped pigpio and exiting...")
finally:
    pi.set_PWM_dutycycle(step,0) #PWM off
    pi.stop()

def generate_ramp(ramp):
    pi.wave(clear)
    length = len(ramp)
    wid = [-1]*length

    for i in range(length):
        frequency = ramp[i][0]
        micros = int(500000/frquency)
        wf = []
        wf.append(pigpio.pulse(1<< STEP, 0,micros))
        wf.append(pigpio.pulse(0,1 << STEP, micros))
        pi.wave_add_generic(wf)
        wid[i] = pi.wave_clear()

        chain = []
        for i in range(length):
            steps = ramp[i][1]
            x = steps & 255
            y = steps >> 8
            chain += [255,0,wid[i],255,1,x,y]
