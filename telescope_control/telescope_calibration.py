#!/usr/bin/python
"""
code for calibration the telescope using a transformation matrix. Math is taken from this website: http://www.geocities.jp/toshimi_taki/aim/aim.htm
"""

from telescope_class import Telescope
from encoder_class import Encoder
from digital_setting_circle import digital_setting_circle
import numpy as np
from calculations import calculations
from angle_conversions import angle_conversions
import datetime
import time
import sys
from parsing_gps import GPS_parse

telescope = Telescope()
calculations = calculations()
angle_conversions = angle_conversions()
altitude_encoder = Encoder()
azimuth_encoder = Encoder()

class Stars():
    def __init__(self):
        """
        sets right ascension and declination of both stars to zero at
        start, so checking function returns false if no data was entered,
        or if data was entered incorrectly.
        """
        self.star_1 = [0, 0]
        self.star_2 = [0, 0]

    def define_star_2(self, s_declination, s_right_ascension):
        #function that stores the data for star_2
        telescope.set_star_declination(s_declination)
        telescope.set_star_right_ascension(s_right_ascension)
        self.star_2 = [telescope.s_right_ascension, telescope.s_declination]

    def define_star_1(self, s_declination, s_right_ascension):
        #function that stores the data for star_1
        telescope.set_star_Declination(s_declination)
        telescope.set_star_right_ascension(s_right_ascension)
        self.star_1 = [telescope.s_right_ascension, telescope.s_declination]

class Matrices():
    def __init__(self):
        self.stars = Stars()

    def correction_matrices(self):
        #star1_data
        L1 = np.cos(self.stars.star_1[0])*np.cos(self.stars.star_1[1])
        M1 = np.cos(self.stars.star_1[0])*np.sin(self.stars.star_1[1])
        N1 = np.sin(self.stars.star_1[0])

        #star2_data
        L2 = np.cos(self.stars.star_2[0])*np.cos(star_2[1])
        M2 = np.cos(star_2[0])*np.sin(star_2[1])
        N2 = np.sin(star_2[0])
        
        #star1_telescope_position
        telescope_position = [altitude_encoder.get_degrees(), azimuth_encoder.get_degrees()]
        l1 = np.cos(telescope_position[0])*np.cos(telescope_position[1])
        m1 = np.cos(telescope_position[0])*np.sin(telescope_position[1])
        n1 = np.sin(telescope_position[0])

        #star2_telescope_position
        telescope_position = [altitude_encoder.get_degrees(), azimuth_encoder.get_degrees()]
        l2 = np.cos(telescope_position[0])*np.cos(telescope_position[1])
        m2 = np.cos(telescope_position[0])*np.sin(telescope_position[1])
        n2 = np.sin(telescope_position[0])

        constant_1 = 1/math.sqrt((m1*n1-n1*m1)^2 + (n1*l2 - l1*n2)^2 + (l1*m2 - m1*l2)^2)
        l3 = constant_1* (m1*n2- n1*m2)
        m3 = constant_1* (n1*l2- l1*n2)
        n3 = constant_1* (l1*m2- m1*l2)
        correction_matrix_1 = [l3, m3, n3]
        constant_2 = 1/math.sqrt((M1*N2 - N1*m2)^2 + (N1*L2-L1*N2)^2 + (L1*M2-M1*L2)^2)
        L3 = constant_2* (M1*N2- N1*M2)
        M3 = constant_2* (N1*L2- L1*N2)
        N3 = constnat_2* (L1*M2- M1*L2)
        correction_matrix_2 = [L3, M3, N3]
        print(correction_matrix_1, correction_matrix_2)

        #rotation matrices
        star_matrix       = np.matrix([[l1,l2,l3],
                                       [m1,m2,m3],
                                       [n1,n2,n3]])
        telescope_matrix  = np.matrix([[L1,L2,L3],
                                       [M1,M2,M3],
                                       [N1,N2,N3]])
        self.transformation_matrix = np.matmul(star_matrix, telescope_matrix)

        return self.transformation_matrix

    def convert_to_telescope_coordinates(self, declination, right_ascension):
        pass

    
if __name__ == '__main__':
    print('enter declination of star in DD:MM:SS')
    line = input()
    star_declination = str(line)
    star_declination = angle_conversions.degrees_to_degrees(star_declination)
    print('enter right ascension of star in HH:MM:SS')
    line = input()
    star_right_ascension = str(line)
    star_right_ascension = angle_conversions.hours_to_degrees2(star_right_ascension)
    Stars.define_star_1(star_declination, star_right_ascension)
    print(Stars.star_1)
        
                    
                    

                    
