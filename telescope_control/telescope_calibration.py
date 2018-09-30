#!/usr/bin/python
"""
code for calibration the telescope using a transformation matrix. Math is taken from this website: http://www.geocities.jp/toshimi_taki/aim/aim.htm
"""

import sys
from telescope_class import Telescope
from encoder_class import Encoder
#from digital_setting_circle import digital_setting_circle
import numpy as np
from calculations import Calculations
from angle_conversions import angle_conversions
import datetime
import time
from parsing_gps import GPS_parse
import math

telescope = Telescope()
calculations = Calculations()
angle_conversions = angle_conversions()
altitude_encoder = Encoder(16, 19, 26, 6, 5, 13, 1)
azimuth_encoder = Encoder(20, 21 ,12, 25, 4, 18, 2)
altitude_encoder.run_encoder()
azimuth_encoder.run_encoder()
class Stars():
    def __init__(self):
        """
        sets right ascension and declination of both stars to zero at
        start, so checking function returns false if no data was entered,
        or if data was entered incorrectly.
        """
        self.star_1 = [0, 0]
        self.star_2 = [0, 0]
        self.target_star = [0,0]

    def in_ra_dec(self):
        """
        function that lets you input data for the target star
        """
        print('enter right ascension in HH:MM:SS')
        line = input()
        right_ascension = str(line)
        right_ascension = angle_conversions.hours_to_degrees2(right_ascension)
        self.target_star[0] = right_ascension
        telescope.set_right_ascension(right_ascension)
        print('enter declination in DD:MM:SS')
        line = input()
        declination = str(line)
        declination = angle_conversions.degrees_to_degrees(declination)
        self.target_star[1] = declination
        telescope.set_declination(declination)
        telescope.set_declination(degrees)
        telescope.get_gast()
        telescope.get_local_hour_angle()
        telescope.set_altitude()
        telescope.set_azimuth()
        telescope.get_azimuth()
        telescope.get_altitude()
        print(self.target_star)

    def star_az_alt(self):
        self.inverse_transformation()
        Z1 = np.cos(self.target_star[1])*np.cos(self.target_star[0])
        X1 = np.cos(self.target_star[1])*np.sin(self.target_star[0])
        C1 = np.sin(self.target_star[1])
        target_star_matrix = np.matrix([[Z1]
                                        [X1]
                                        [C1]])
        telescope_matrix = np.matmul(target_star_matrix, self.inverse_transformation_matrix)
        print(telescope_matrix)

    def define_star_2(self, s_declination, s_right_ascension):
        #function that stores the data for star_2
        telescope.set_star_declination(s_declination)
        telescope.set_star_right_ascension(s_right_ascension)
        self.star_2 = [telescope.s_right_ascension, telescope.s_declination]
        self.set_telescope_star_2_position()

    def define_star_1(self, s_declination, s_right_ascension):
        #function that stores the data for star_1
        telescope.set_star_declination(s_declination)
        telescope.set_star_right_ascension(s_right_ascension)
        self.star_1 = [telescope.s_right_ascension, telescope.s_declination]
        self.set_telescope_star_1_position()

    def set_telescope_star_2_position(self):
        #star2_telescope_position
        self.telescope_position2 = [altitude_encoder.get_degrees(), azimuth_encoder.get_degrees()]
        
    def set_telescope_star_1_position(self):        
        #star1_telescope_position
        self.telescope_position1 = [altitude_encoder.get_degrees(), azimuth_encoder.get_degrees()]
        
    def correction_matrices(self):
        #star1_data
        L1 = np.cos(stars.star_1[1])*np.cos(stars.star_1[0])
        M1 = np.cos(stars.star_1[1])*np.sin(stars.star_1[0])
        N1 = np.sin(stars.star_1[1])

        #star2_data
        L2 = np.cos(stars.star_2[1])*np.cos(stars.star_2[0])
        M2 = np.cos(stars.star_2[1])*np.sin(stars.star_2[0])
        N2 = np.sin(stars.star_2[1])

        l1 = np.cos(self.telescope_position1[0])*np.cos(self.telescope_position1[1])
        m1 = np.cos(self.telescope_position1[0])*np.sin(self.telescope_position1[1])
        n1 = np.sin(self.telescope_position1[0])
        
        l2 = np.cos(self.telescope_position2[0])*np.cos(self.telescope_position2[1])
        m2 = np.cos(self.telescope_position2[0])*np.sin(self.telescope_position2[1])
        n2 = np.sin(self.telescope_position2[0])

        x = m1*n2 - n1*m1
        print(m1, "m1")
        print(n2, "n2")
        print(n1, "n1")
        print(x)
        x2 = x*x
        y = n1*l2 - l1*n2
        print(y)
        y2 = y*y
        z = l1*m2 - m1*l2
        print(z)
        z2 = z*z
        constant_1 = 1/math.sqrt(x2 + y2 + z2)
        l3 = constant_1* (m1*n2- n1*m2)
        m3 = constant_1* (n1*l2- l1*n2)
        n3 = constant_1* (l1*m2- m1*l2)
        correction_matrix_1 = [l3, m3, n3]
        x = (M1*N2-N1*M2)
        x2 = x*x
        y = N1*L2-L1*N2
        y2 = y*y
        z = L1*M2 - M1*L2
        z2 = z*z
        constant_2 = 1/math.sqrt(x2 + y2 + z2)
        L3 = constant_2* (M1*N2- N1*M2)
        M3 = constant_2* (N1*L2- L1*N2)
        N3 = constant_2* (L1*M2- M1*L2)
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

    def inverse_transformation(self):
        self.inverse_transformation_matrix = np.linalg.inv(self.transformation_matrix)
        return self.inverse_transformation_matrix

    
if __name__ == '__main__':
    print('enter declination of star in DD:MM:SS')
    stars = Stars()
    line = input()
    star_declination = str(line)
    star_declination = angle_conversions.degrees_to_degrees(star_declination)
    print('enter right ascension of star in HH:MM:SS')
    line = input()
    star_right_ascension = str(line)
    star_right_ascension = angle_conversions.hours_to_degrees2(star_right_ascension)
    stars.define_star_1(star_declination, star_right_ascension)
    print(stars.star_1)
    print('enter declination of star in DD:MM:SS')
    line = input()
    star_declination = str(line)
    star_declination = angle_conversions.degrees_to_degrees(star_declination)
    print('enter right ascension of star in HH:MM:SS')
    line = input()
    star_right_ascension = str(line)
    star_right_ascension = angle_conversions.hours_to_degrees2(star_right_ascension)
    stars.define_star_2(star_declination, star_right_ascension)
    print(stars.star_2)
    stars.correction_matrices()
    print(stars.correction_matrices())
    stars.inverse_transformation()
    print(stars.inverse_transformation())
    
        
                    
                    

                    
