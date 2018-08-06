from encoder_class import Encoder
from telescope_class import Telescope

class Two_Star_Calibration():

    def __init__(self):
        self.star_alt_offset = star_alt_offset = 0
        self.star_az_offset = star_az_offset = 0
        star_alt_offset = []
        star_az_offset = []
        self.telescope = Telescope()
        self.altitude_encoder = Encoder(16, 19, 26 ,1)
        self.azimuth_encoder = Encoder(20, 21, 12, 2)
    def alt_offset(self):
        alt_offset = self.altitude_encoder.degree - self.telescope.set_star_altitude()
        return alt_offset
    
    def az_offset(self):
        az_offset = self.azimuth_encoder.degree - self.telescope.set_star_azimuth()
        return az_offset

    def add_az_alt_offset(self):
        append.star_alt_offset(self.alt_offset)
        append.star_az_offset(self.az_offset)
        return star_az_offset
        return star_alt_offset

    
        

    
        
