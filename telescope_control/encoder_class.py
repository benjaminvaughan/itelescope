#for encoders
import pigpio
import time

class Encoder():
    def __init__(self, pin_a, pin_b, pin_z, pin_c, pin_d, power_pin, encoder_id, pi = None):
        if pi is None:
            pi = pigpio.pi()
        #Hall_Effect = hall_effect()
        #azimuth_hall_effect = Hall_Effect()
        #altitude_hall_effect = Hall_Effect()
        #azimuth_hall_effect.hall_effect_power_supply()
        #altitude_hall_effect.hall_effect_power_supply()
        self.pi = pi
        self.pin_a = pin_a
        self.pin_b = pin_b
        self.pin_z = pin_z
        pi.set_mode(pin_a, pigpio.INPUT)
        pi.set_mode(pin_b, pigpio.INPUT)
        pi.set_mode(pin_z, pigpio.INPUT)
        self.a_state = None
        self.degree = 0
        self.position = 0
        self.constant = 360.0 / 5000
        self.encoder_id = encoder_id
        self.pin_c = pin_c
        self.pin_d = pin_d
        # *** pi.set_mode(pin_c, pigpio.INPUT)
        # *** pi.set_mode(pin_d, pigpio.INPUT)
        self.power_pin = power_pin
        # *** power_pin? pi.set_mode(pin_e, pigpio.OUTPUT)

    def call_back_a(self, pin, level, tick):
        self.a_state = level 

    def call_back_b(self, pin, level, tick):
        #defines a callback for when the b_state changes and determines in which direction the object is moving.
        if hall_effect_flag:
            if self.a_state:
                self.position += 1
                self.direction = "clockwise"
            else:
                self.position -= 1
                self.direction = "counter_clockwise"
                self.degree = self.position * self.constant
        else:
            pass 

    def call_back_z(self, pin, level, tick):
        #function that counts the number of revolutions that the gear has made and resets the gear once it has reached 360 degrees of motion.
        
        if self.direction == "clockwise":
            self.revs += 1
            if self.revs == 0 or self.revs == 100 or self.revs == -100:
                self.position = 0
                self.revs = 0 
        elif self.direction == "counter_clockwise":    
            self.revs -= 1
            if self.revs == 0 or self.revs == 100 or self.revs == -100:
                self.position = 0
                self.revs = 0 
        else:
            pass 
   
    def altitude_restart(self):
        revs = self.degree // 360.0
        self.degree -= revs * 360

    def get_degrees(self):
        #function that prints the encoder's degrees as well as returns the degrees of the gear so that the telescope knows it's position
        print('encoder', self.encoder_id, self.degree)
        return float(self.degree)

    

    def run_altitude_encoder(self):
        #function that runs the altitude_Encoder
        self.pi.callback(self.pin_a, 2, self.call_back_a)
        self.pi.callback(self.pin_b, 1, self.call_back_b)
        self.altitude_restart()
        
    def run_encoder(self):
        #function that runs the azimuth encoder.
        self.pi.callback(self.pin_a, 2, self.call_back_a)
        self.pi.callback(self.pin_b, 1, self.call_back_b)
        self.pi.callback(self.pin_z, 1, self.call_back_z)
