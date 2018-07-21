
#from motor_class import Motor
#import pigpio

import keyboard
import time

while True:
    if keyboard.is_pressed('left'):
        print('left')
    else:
        time.sleep(0.1)
