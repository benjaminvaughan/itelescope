import numpy as np #imports NumPy and can call functions as np
import math #imports math
from two_star_correction import two_star_correction #imports the previously written two correction module

class two_Star_calibration(two_star_correction): #defines a class called two_star_callibration that inherits from the class of two_star_correction, has everything that two_star_correction, but can modify it.
    def __init__(self,log): #defines __init__ with the variables self and log. __init___ is a special function called the constructor that is called when the class is instantiated. self is a refrence to the instance of the class.
        self.reset() #calls the reset function
        self.logger = log #sets logger function = to log

    def reset(self): #defines the reset function
        self.stars = [] #creates an empty list of stars
        self.star_count = 0 #sets the star_count zero
        self.test_pass = True #calls the test_pass function and sets a variable to True

    def add_star(self.tel_star,stel_star):
        self.stars.append(star(tel_star,stel_star) #adds the stars to the list
        self.star_count += 1 #increases the number of stars counted by 1

    def get_rotation_matrix(self): #defines the function get_rotation_matrix
        if(self.star_count==1): #defines an if statement where if the starcount is 1 then the function does something
            return self.one_star_rotation_matrix() #calls a function called one_star_rotation_matrix
        elif(self.star_count==2): #or if the star count is equal to two then it does a different operation
            return self.two_star_rotation_matrix() #calls the function two_star_rotation_matrix
        else: #otherwise do this
            self.logger.error("Rotation matrix calculation failed. The identity was used instead") #calls a class called logger within the self class and that calls a function called error.
            return np.matrix(np.identity(3)) #returns the identity matrix

    def one_star_rotation_matrix(self):
        if(self.star_count<1):
            raise index_error("there are no loaded stars so cannot calculate matrix)" # checks to see if there is an adequate number of sars and returns an error message if there is not.
        the_star = self.stars[0] #sets the star equal to the first star in the list of stars.
        dAz = self.plus_minus180(the_Star.sAz-the_star.tAz)
        #dAlt = self.plusMinus180(theStar.sAlt-theStar.tAlt)
        qAz = self.__build_quaternion(dAz, [0,0,1]
        #qAlt = self.__buildQuaternion(dAlt, [0,1,0])
                                      #q = self.__quaternion_product(qAz, qAlt
        R = self.__quaternion_to_matrix(qAz) #sets r equal the result of the function within the class two_star_correction when plugging in the result for qAz
        if self.test_matrix(R):
            return R #if plugging in R to the test_matrix function returns True then the function returns R again.
        else:
            self.test_pass = False
            return self.get_identity_matrix() #then the function falls and it returns the identity matrix

    def two_star_rotation_matrix(self): # defining a new function called two_Star_rotation_matrix
        if(self.star_count<2):
            raise index_error("There are not enough loaded stars") #checks to see if there are at least two stars for the two star rotation matrix
        star1 = self.stars[0] #star1 = the first star in the list of stars
        star2 = self.stars[1] #star2 = the second star in the list of stars
        tel_mat = self.__two_star_difference_matrix([star1.tAz,star1.tAlt],[star2.tAz,star2.tAlt])
        stel_mat = self.__two_star_difference_matrix([star1.sAz,star1.sAlt],[star2.sAz,star2.sAlt])
        R = np.linalg.solve(stel_mat.T,tel_mat.T) #calls a function in numpy to do some calculations on a set of matrices
        if self.test_matrix(R):
            return R
        else:
            self.test_pass = False
            return self.one_star_rotation_matrix()

    def get_identity_matrix(self):
        return np.matrix(np.identity(3)) #function that returns an identity matrix from numpy
                                      
    def test_matrix(self,R): #tests to see whether the matrix is a valid matrix
        if np.isnan(R.sum()) or np.isinf(R.sum()):
            return False
        else:
            return True

    def __two_Star_difference_matrix(self,star1,star2):
        c1 = self.AzAltToVec(star1[0], star1[1])
        c2 = self.AzAltToVec(star2[0], star1[1])
        c3 = np.cross(c1,c2) #does the cross product of the two matrices
        c3 = c3/n.linalg.norm(c3) #finds the unit vector
        M = np.matrix([c1,c2,c3]) #defines a list of c1,c2,c3
        M = M.T
        return M
        pass

    def __build_quaternion(self,angle,axis): #defines a function that builds the quaternion
        sin_angle = math.sin(angle/2) #defines sin_angle
        quaternion = np.array([math.cos(angle/2), sin_angle*axis[0],sin_angle*axis[1], sin_angle*axis[2]]) #defines the quaternion
        return quaternion

    def __quaternion_to_matrix(self, quaternion): #converts the quaternion to a matrix
        s = quaternion[0];
        vx = quaternion[1];
        vy = quaternion[2];
        vz = quaternion[3];

        i1j1=1-2*math.pow(vy,2)-2*math.pow(vz,2);
        i1j2=2*vx*vy-2*s*vz;
        i1j3=2*vx*vz+2*s*vy;
        i2j1=2*vx*vy+2*s*vz;
        i2j2=1-2*math.pow(vx,2)-2*math.pow(vz,2);
        i2j3=2*vy*vz-2*s*vx;
        i3j1=2*vx*vz-2*s*vy;
        i3j2=2*vy*vz+2*s*vx;
        i3j3=1-2*math.pow(vx,2)-2*math.pow(vy,2);
        
        R = np.matrix([[i1j1, i1j2, i1j3], [i2j1, i2j2, i2j3],[i3j1, i3j2, i3j3]])
        return R

    def __quaternion_product(self,q,r):
        s1 = q[0]
        v1 = np.array([q[1],q[2],q[3]])
        s2 = r[0]
        v2 = np.array([r[1],r[2],r[3]])
        s0 = s1*s2 - np.dot(v1,v2)
        v0 = s1*v2 + s2*v1 + np.cross(v1,v2)
        q0 = np.array([s0,v0[0],v0[1],v0[2]])
        q0 = q0/np.linalg.norm(q0)
        return q0

class star(object): #creates a new class called star
    def __init__(self,tel_coordinates,stel_coordinates):
        self.tAz = tel_coordinates[0].r #the azimuth coordinates of the telescope
        self.tAlt = tel_coordinates[1].r #the altitude coordinates of the telescope
        self.sAz = stel_coordinates[0].r #the stellar azimuth coordinates
        self.sAlt = stel_coordinates[1].r#the stellar altitude coordinates
