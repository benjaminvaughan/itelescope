

#file for attempting to learn how to parse

while True:
    line = input()
    if line == ':Aa#':
        print('start telescope automatic align sequence')
    elif line == 'quit':
        break
    elif line == ':GA#': #returns sDD*MM# or sDD*MM'SS# get telescope altitude
        print('get telescope altitude')
        print('s' + telescope.get_altitude() + '#')
    elif line == ':GG#': #returns sHH# or sHH.H# #get UTC offset time
        print('get UTC offset time')
        print('s' + get_utc_offset_str() + '#")
    elif line == ':GS#': #gets the sites longitude
        print('get site longitude')
    elif line == ':Gt#': #gets the sites latitude
        print('get site latitude')
    elif line == ':GZ#': #get the telescope's azimuth
        print('get telescope azimuth')
        print('s' + telescope.get_azimuth + '#')
    elif line == ':MS#': #slews to the target
        print('slew to target object')
    elif line == ':SasDD*MM#': #sets the targets object altitude to sDD*MM'SS#
        print('setting target altitude to target_altitude')
    elif line == 'SzDDD*MM#': #sets the target object azimuth
        print('setting target azimuth to target_azimuth')
    
    elif line == ':
    elif line == ':Q#':
        print('halt all movement')
