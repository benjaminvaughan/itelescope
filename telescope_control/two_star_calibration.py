from encoder_class import Encoder
from telescope_class import Telescope

class Two_Star_Calibration():

    def __init__(self):
        self.star_alt_offset = star_alt_offset
        self.star_az_offset = star_az_offset
        star_alt_offset = []
        star_az_offset = []
        telescope = Telescope()

    def alt_offset(self):
        alt_offset = altitude_encoder.degrees - telescope.set_star_altitude()
        return alt_offset
    
    def az_offset(self):
        az_offset = azimuth_encoder.degrees - telescope.set_star_azimuth()
        return az_offset

    def add_az_alt_offset(self):
        append.star_alt_offset(self.alt_offset)
        append.star_az_offset(self.az_offset)
        return star_az_offset
        return star_alt_offset

    
        

    
        
