

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
    elif line == ':GS#': #returns HH:MM:SS#
        print()
        print('get sidereal time')
    elif line == ':Gg#':
        print('get site longitude')
    elif line == ':Gt#':
        print('get site latitude')
    elif line == ':GZ#':
        print('get telescope azimuth')
        print('s' + telescope.get_azimuth + '#')
    elif line == ':MS#':
        print('slew to target object')
    elif line == ':
    elif line == ':Q#':
        print('halt all movement')
