from encoder_class import Encoder
from telescope_class import Telescope

class Two_Star_Calibration():
    def __init__(self, telescope=None):
        self.star_alt_offset = []
        self.star_az_offset = []
        if telescope is None:
            telescope = Telescope()
        self.telescope = telescope

    def alt_offset_calibration(self):
        self.alt_offset = self.telescope.altitude_encoder.degree - self.telescope.s_altitude
        print(self.alt_offset, 'altitude offset') 
        return str(self.alt_offset)
    
    def az_offset_calibration(self):
        self.az_offset = self.telescope.azimuth_encoder.degree - self.telescope.set_star_azimuth()
        print(self.az_offset, 'azimuth offset')
        return str(self.az_offset)

    def add_az_alt_offset(self):
        self.star_alt_offset.append(self.alt_offset)
        self.star_az_offset.append(self.az_offset)
        return self.star_az_offset, self.star_alt_offset

    
        

    
        
