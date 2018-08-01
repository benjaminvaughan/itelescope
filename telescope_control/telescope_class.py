

#used for talking with meadle LX200 Protocol

class Telescope(Object):
    def __init__(self):
        self.altitude_encoder = Encoder()
        self.altitide_motor = Motor()
        self.azimuth_encoder = Encoder()
        self.azimuth_motor = Motor()

    def set_azimuth(self, target_azimuth):
        self.target_azimuth = target_azimuth
        return target_azimuth
    
    def set_altitude(self, target_altitude):
        self.target_altitude = target_altitude
        return target_altitude
        
    def update(self):
        self.current_altitude = self.altitude_encoder.print_degrees()
        altitude_error = self.target_altitude - self.current_altitude
        self.current_azimuth = self.azimuth_encoder.print_degrees()
        azimuth_error = self.target_azimuth - self.current_azimuth
        if azimuth_error >0:
            print('positive azimuth')
            azimuth_motor.set_direction(1)
        elif azimuth_error >0:
            print('negative azimuth')
            azimuth_motor.set_direction(0)
        if altitude_error >= 0:
            print('positive altitude')
            self.altitude_motor.set_direction(1)
        if altitude_error < 0:
            print('this is a negative number')
            self.altitude_motor.set_direction(0)
        altitude_error = abs(altitude_error)
        azimuth_error = abs(azimuth_error)
        if azimuth_error >= 0:
            azimuth_motor.set_speed(6)
        if azimuth_error >= 200:
            azimuth_motor.set_speed(5)
        if azimuth_error >= 400:
            azimuth_motor.set_speed(4)
        if azimuth_error >= 500:
            azimuth_motor.set_speed(3)
        if azimuth_error >= 600:
            azimuth_motor.set_speed(2)
        if azimuth_error >= 700:
            azimuth_motor.set_speed(1)
        if altitude_error >= 0:
            altitude_motor.set_speed(6)
        if altitude_error >= 200:
            altitude_motor.set_speed(5)
        if altitude_error >= 400:
            altitude_motor.set_speed(4)
        if altitude_error >= 500:
            altitude_motor.set_speed(3)
        if altitude_error >= 600:
            altitude_motor.set_speed(2)
        if altitude_error >= 700:
            altitude_motor.set_speed(1)

if __name__ == "__main__":
    telescope = Telescope()
    while True:
        time.sleep(1)
        telescope.update()
        
