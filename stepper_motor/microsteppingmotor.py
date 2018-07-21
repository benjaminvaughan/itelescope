"""
https://www.rototron.info/raspberry-pi-stepper-motor-tutorial/
"""

from time import sleep
import pigpio

DIR = 20 # direction GPIO pin
step = 21 # step GPIO pin
#switch = 16 # GPIO pin of switch

#connect to pigpiod daemon
pi = pigpio.pi()

pi.set_mode(DIR, pigpio.OUTPUT)
pi.set_mode(step, pigpio.OUTPUT)

pi.set_mode(switch,pio.INPUT)
#pi.set_pull_up_down(switch, pigpio.PULL_DOWN)

mode = (14,15,18) #microstep resolution
resolution = {'Full':(0,0,0),
	   'Half':(1,0,0),
	   '1/4':(0,1,0),
	   '1/8':(1,1,0)
	   '1/16':(0,0,1),
	   '1/32'(1,0,1)}

for i in range(3):
    pi.write(MODE[i], resolution['Full'][i])

pi.set_PWM_dutycycle(step,128) #PWM 1/2 on 1/2 off
pi.set_PWM_frequency(Step,500) #500 pulses per second

try:
    while True:
        # pi.write(DIR, pi.read(switch)) # set direction
        pi.write(DIR,0)
        sleep.(1)
except KeyBoardInterrupt:
    print("\nCtrl-C presssed. Stopped pigpio and exiting...")
finally:
    pi.set_PWM_dutycycle(step,0) #PWM off
    pi.stop()

def generate_ramp(ramp): #generating a ramp up
    """
generate ramp waveforms. ramp: list of [frequency,steps]
    """
#generate a wave per ramp level
    pi.wave_clear() #clear existing waves
    length = len(ramp) #number of ramp levels
    wid = [-1]*length #width of the length

    for i in range(length): 
        frequency = ramp[i][o]
        micros = int(500000/frequency)
        wf = []
        wf.append(pigpio.pulse(1<<step,0,micros) # pulse on
        wf.append(pigpio.pulse(0,1<<step, micros) #pulse off
        pi.wave_add_generic(wf)
        wid[i] = pi.wave_create()

#generate a chain of waves
        chain =  []
        for i in range(length):
            steps = ramp[i][1]
            x = steps & 255
            y = steps >> 8
            chain += [255,0,wid[i],255,1,x,y]
        pi.wave_chain(chain) #transmit the wave

              
