import pigpio
import time
from encoder_class import Encoder

encoder1 = Encoder(16, 19, 26)

if __name__ == '__main__':
    encoder1.run_encoder()
    while True:
        Encoder.print_degrees(1)
