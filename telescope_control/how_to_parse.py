

#file for attempting to learn how to parse

while True:
    line = input()
    if line == 'quit':
        break

    elif line == ':GA#': #get telescope altitude, returns sDD*MM'SS#
        print('get telescope altitude')
        print('s' + telescope.get_altitude() + '#')

    elif line == ':GG#': #returns sHH.H#
        """
        the number of decimal hours to add to lcoal time to convert it to utc.
        if the number is a whole number then sHH is returned.
        """
        print('get UTC offset time')
        print('s' + get_utc_offset_str() + '#')

    elif line == ':GS#': #gets the sites longitude
        """
        returns sDDD*MM#
        returns sDD* negative is east
        """
        print('get site longitude')

    elif line == ':Gt#': #gets the sites latitude
        """
        returns sDD*MM#
        positive implies north latitude
        """
        print('get site latitude')

    elif line == ':GZ#': #get the telescope's azimuth, returns DDD*MM'SS#
        print('get telescope azimuth')
        print('s' + telescope.get_azimuth + '#')

    elif line == ':MS#': #slews to the target
        """
        returns 0: slew is possible
        returns 1<string># object below horizion w/ string message
        returns 2<string># object below higher w/ string message
        """
        print('slew to target object')

    elif line == ':SasDD*MM#': #set the target altitude to sDD*MM'SS#
        """
        returns 0 object within slew range
        returns 1 object out of slew range
        """
        print('setting target altitude to target_altitude')

    elif line == 'SzDDD*MM#': #sets the target azimuth to sDD*MM'SS#
        """
        returns 0 invalid
        returns 1 valid
        """
        print('setting target azimuth to target_azimuth')

    elif line == '$Badd#': #set altitude antibacklash, returns nothing

        print('setting altitude antibacklash')
    elif line == '$BZdd#': #set azimuth antibacklash, returns nothing

        print('setting azimuth antibacklash')
    elif line == ':Gd#': #set the object declination, returns sDD*MM'SS#

        print("the object's declination is")
    elif line == ':Gr#': #set the object right ascension, returns HH:MM:SS#
        print("the object's right ascension is") 

    elif line == ':Q#' #halts all current slewing, returns nothings
        print('halt all movement')

