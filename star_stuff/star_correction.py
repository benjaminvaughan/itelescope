"""
https://sourceforge.net/p/itelescope/code/ci/master/tree/iTelRaspberry/twoStarCorrection.py (source code)
"""

import numpy as np #import numpy and be able to call it using np.
import math #imports the math module
from angles import angles #from created module called angles import the class angles

class two_star_correction(object): #creates a class that holds the object object
    def __init__(self,rotation_matrix):
        self.add_rotation_matrix(rotation_matrix)
    def add_rotation_matrix(self,rotation_matrix):
        self.rotation_matrix = rotation_matrix
    def correct(self,Az,Alt):
        tVec = self.AzAltToVec(Az.r,Alt.r)
        tV = np.matrix([tVec])
        dVec = self.rotation_matrix*tV.t
        [rAz,rAlt] = self.VectoAzAlt(dVec)
        aAz = angle(r =Az)
        aAlt = angle(r = Alt)
        return [aAz,aAlt]
    def plus_minus_180(self,the_angle): #checks to see if the angle is greater than, equal to, or less than pi then corrects the angle to fit within 360 degrees
        while (the_angle <= -math.pi):
            the_angle = the_angle + 2*math.pi
        while (the_angle > math.pi):
            the_angle = the_angle - 2*math.pi
        return the_angle
    def VecToAzAlt(self,vec_in):
        Alt = math.asin(vec_in[2])
        pAz = math.atan(vec_in[1]/vec_in[0])
        Az = 0

        if (vec_in[0]>=0):
            Az = pAz
        elif (vec_in[0]<0):
            Az = math.pi + pAz
        Az = self.plus_minus_180(Az);
        return [Az,Alt]
    def AzAltToVec(self,Az,Alt):
        z = self.plus_minus_180(Az)
        t = self.plus_minus_180(Alt)
        v = np.array([math.cos(t)*math.cos(z),math.cos(t)*math.sin(z),math.sin(t)])
        return v
            
