import pigpio
import time
from encoder_class import Encoder

encoder1 = Encoder(16, 19, 26, 1)
encoder2 = Encoder(20, 21, 12, 2)

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
        #time.sleep(9.1)
