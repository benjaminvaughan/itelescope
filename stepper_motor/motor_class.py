
import pigpio

class Motor():
    def __init__(self, dir_pin, step_pin, mode1, mode2, mode3, pi=None):
        if pi is None:
            pi = pigpio.pi()
        self.pi = pi
        self.dir_pin = dir_pin
        self.step_pin = step_pin
        pi.set_mode(dir_pin, pigpio.OUTPUT)
        pi.set_mode(step_pin, pigpio.OUTPUT)
        mode = (mode1,mode2,mode3)
        resolution =  {'Full':(0,0,0),
	   'Half':(1,0,0),
	   '1/4':(0,1,0),
	   '1/8':(1,1,0),
	   '1/16':(0,0,1),
	   '1/32':(1,0,1)}
        for i in range(3):
            pi.write(mode[i], resolution['1/32'][i])

    def set_speed(self, duty_cyle, frequency, direction):
        self.pi.set_PWM_dutycycle(self.step_pin, duty_cycle)
        self.pi.set_PWM_frequency(self.step_pin, frequency)

