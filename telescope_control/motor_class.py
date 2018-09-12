
import pigpio
import time
import click

class Motor():
    def __init__(self, dir_pin, step_pin, mode1, mode2, mode3, pi=None):
        if pi is None:
            pi = pigpio.pi()
        self.pi = pi
        self.dir_pin = dir_pin
        print('dir', dir_pin)
        self.step_pin = step_pin
        pi.set_mode(dir_pin, pigpio.OUTPUT)
        pi.set_mode(step_pin, pigpio.OUTPUT)
        self.mode = (mode1,mode2,mode3)
        self.resolution =  {'Full':(0,0,0),
	   'Half':(1,0,0),
	   '1/4':(0,1,0),
	   '1/8':(1,1,0),
	   '1/16':(0,0,1),
	   '1/32':(1,0,1)}
        self.speed = 0
        self.speed_callback = None

    def set_speed_callback(self, callback):
        self.speed_callback = callback
        
    def a32_microsteps(self):
        for i in range(3):
            self.pi.write(self.mode[i], self.resolution['1/32'][i])

    def a16_microsteps(self):
        for i in range(3):
            self.pi.write(self.mode[i], self.resolution['1/16'][i])

    def a8_microsteps(self):
        for i in range(3):
            self.pi.write(self.mode[i], self.resolution['1/8'][i])

    def a4_microsteps(self):
        for i in range(3):
            self.pi.write(self.mode[i], self.resolution['1/4'][i])

    def full_step(self):
        for i in range(3):
            self.pi.write(self.mode[i], self.resolution['Full'][i])
        

    def set_speed(self, speed):
        # if there is a callback registered, and speed changes from zero
        # to non-zero, call it
        if not self.speed_callback is None and self.speed == 0 and speed != 0:
            self.speed_callback()
        self.speed = speed
        if speed == 0:
            self.stopping_motor()
            return self.speed
        if speed == 1:
            self.a32_microsteps()
            self.set_frequency_dutycycle(128, 1500)
            return self.speed
        elif speed == 2:
            self.a32_microsteps()
            self.set_frequency_dutycycle(128, 2000)
            return self.speed
        elif speed == 3:
            self.a16_microsteps()
            self.set_frequency_dutycycle(128, 1000)
            return self.speed
        elif speed == 4:
            self.a8_microsteps()
            self.set_frequency_dutycycle(128, 1000)
            return self.speed
        elif speed == 5:
            self.a4_microsteps()
            self.set_frequency_dutycycle(128, 1000)
        elif speed == 6:
            self.full_step()
            self.set_frequency_dutycycle(128, 500)
        else:
            print('invalid speed', speed)

    def set_direction(self, direction):
        self.pi.write(self.dir_pin, direction)

    def set_frequency_dutycycle(self, duty_cycle, frequency):
        self.pi.set_PWM_dutycycle(self.step_pin, duty_cycle)
        self.pi.set_PWM_frequency(self.step_pin, frequency)

    def stopping_motor(self):
        self.pi.set_PWM_dutycycle(self.step_pin, 0)
        self.pi.set_PWM_frequency(self.step_pin, 0)

    def creating_wave(self, frequency):
        self.pi.wave_create(1.0 / frequency)

    def one_step(self):
        self.pi.wave_send_once(1)

    """
    def motor_control(self, clockwise_key1, counter_clockwise_key1, clockwise_key2, counter_clockwise_key2):
        while True:
            key = click.getchar()
            if key == 'q':
                break
            if key == 'clockwise_key1':
                self.set_speed(128, 1000, 1)
            if key == 'counter_clockwise_key1':
                self.set_speed(128, 1000, 0)
            if len(key) == 3: #arrow keys: 66 down,  67 left, 68 right, 65 up
                key = ord(key[2])
                if key == clockwise_key2:
                    motor.set_speed(128, 1000, 1)
                    time.sleep(0.1)
                if key == counter_clockwise_key2:
                    motor.set_speed(128, 1000, 0)
                    time.sleep(0.1)
    """
                
        
        
