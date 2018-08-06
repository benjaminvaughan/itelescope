#!/usr/bin/python3

import sys, select, termios, tty

class Keyboard:
    """
    Reads keys from standard input
    """
    def __init__(self, timeout=.1):
        """
        timeout (float) how long to wait for a key in seconds
        """
        self.timeout = timeout

    def getKey(self):
        """
        Return the code for the next keypress or None if no key pressed
        within the timeout period
        """
        self.settings = termios.tcgetattr(sys.stdin)
        tty.setraw(sys.stdin.fileno())
        read, write, error = select.select([sys.stdin], [], [], self.timeout)
        if len(read) == 0:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
            return None
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        return key

if __name__ == "__main__":
    keyboard = Keyboard()
    while True:
        key = keyboard.getKey()
        if key == 'q':
           break
        if key is None:
           print('no key\r')
           continue
        print('key', key, ord(key), '\r')

