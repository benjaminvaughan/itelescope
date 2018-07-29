import time
import pigpio
from motor_class import Motor
from encoder_class import Encoder
import click

print('press wasd or up,down,left, right; q is quit')

encoder1 = Encoder(16, 19, 26, 1)
encoder2 = Encoder(20, 21, 12, 2)
motor1 = Motor(24, 23, 25, 8 ,7)
motor2 = Motor(10, 9 , 17, 27, 22)

if __name__ == '__main__':
    encoder1.run_encoder()
    encoder2.run_encoder()
    prev_degree2 = None
    prev_degree1 = None
    while True:
        if prev_degree1 != encoder1.degree:
            encoder1.print_degrees()
            prev_degree1 = encoder1.degree
        if prev_degree2 != encoder2.degree:
            encoder2.print_degrees()
            prev_degree2 = encoder2.degree

    motor1.motor_control(w, s, 65, 66)
    motor2.motor_control(a, d, 67, 68)
