




class GPS_Prase(object):

    def __init__(self):


    def global_positioning_system(self):
        GGA_string =
        Message_ID = GGA_string[0] #protocol header
        UTC_Position = GGA_string[1] #hhmmss.sss
        Latitude = GGA_string[2] #dddmm.mmmm
        N_or_S_indicator = GGA_string[3] #N = north, S = South
        Longitude = GGA_string[4] #dddmm.mmmm
        E_or_W_indicator = GGA_string[5] #E = east, W = West
        Position_Fix_indicator = GGA_string[6] #
        Satelites_used = GGA_string[7]#0 - 12
        HDOP = GGA_string[8] #horizontal dilution of precision
        MSL = GGA_string[9] #in meters
        Units = GGA_string[10]
        Geoid_Separation = GGA_string[11] #in meter
        Units = GGA_string[12]
        age_of_diff_corr = GGA_string[13] #null fields when DGPS is not used
        diff_ref_station_ID = GGA_string[14]
        checksum = GGA_string[15]
        CR_LF = GGA_string[16] #End of message termination
        
        
