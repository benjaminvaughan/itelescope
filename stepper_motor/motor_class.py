
import pigpio
import time
import click

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

    def set_speed(self, duty_cycle, frequency, direction):
        print('speed', duty_cycle, frequency, direction)
        self.pi.write(self.dir_pin, direction)
        self.pi.set_PWM_dutycycle(self.step_pin, duty_cycle)
        self.pi.set_PWM_frequency(self.step_pin, frequency)

    def write_to_motor(self, direction):
        #self.pi.write(self.dir_pin,direction)
        time.sleep(1)

    def stopping_motor(self):
        self.pi.set_PWM_dutycycle(self.step_pin, 0)
        self.pi.stop()
        
    def creating_wave(self, frequency):
        self.pi.wave_create(self.step_pin, self.step_pin, 1.0 // frequency)

    def one_step(self):
        self.pi.wave_send_once(1)

    def motor_control(self, clockwise_key1, counter_clockwise_key1, clockwise_key2, counter_clockwise_key2):
        while True:
            key = click.getchar()
            if key == 'q':
                break
            if key == 'clockwise_key1':
                self.set_speed(128, 1000, 1)
            if key == 'counter_clockwise_key1':
                self.set_speed(128, 1000, 0)
            if len(key) = 3: #arrow keys: 66 down,  67 left, 68 right, 65 up
                key = ord(key[2])
                if key == clockwise_key2:
                    motor.set_speed(128, 1000, 1)
                    time.sleep(0.1)
                if key == counter_clockwise_key2:
                    motor.set_speed(128, 1000, 0)
                    time.sleep(0.1)
                
        
        
