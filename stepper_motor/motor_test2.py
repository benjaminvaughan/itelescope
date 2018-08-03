from motor_class import Motor
import pigpio
import time
import click
#change
pi = pigpio.pi()
motor2 = Motor(24, 23, 25, 8, 7, pi)
motor1 = Motor(10, 9 , 17, 27, 22, pi)

print('press an arrow key or q to quit')
speed = 0
timeout = 0.1
while True:
    key = click.getchar()
    if len(key) == 1:
        if key >= '1' and key <= '9':
            speed = int(key)
            print('speed %d %d' % (speed, ord(key)))
        if key == 'q':
            motor1.stopping_motor()
            motor2.stopping_motor()
            break
        if key == 'a':
            motor1.set_direction(1)
            motor1.set_speed(speed)
        if key == 'd':
            motor1.set_direction(0)
            motor1.set_speed(speed)
        if key == 'w':
            motor2.set_direction(1)
            motor2.set_speed(speed)
        if key == 's':
            motor2.set_direction(0)
            motor2.set_speed(speed)

    elif len(key) == 3:
        key = ord(key[2])
        if key == 66: #down
            motor1.stopping_motor()
            motor1.set_direction(0)
            motor1.one_step()
        if key == 65: #up
            motor1.stopping_motor()
            motor1.set_direction(1)
            motor1.one_step()
        if key == 68: #right
            motor2.stopping_motor()
            motor2.set_direction(0)
            motor2.one_step
        if key == 67: #left
            motor2.stopping_motor()
            motor2.set_direction(1)
            motor2.one_step()
