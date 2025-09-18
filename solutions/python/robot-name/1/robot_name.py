import string
import random


class Robot:
    def __init__(self):
        self.name = ''
        self.turn_on()


    def turn_on(self):
        random.seed()
        digits = ''.join(random.choice(string.ascii_uppercase) for item in range(0, 2))
        letters = ''.join(random.choice(string.digits) for item in range(0, 3))
        self.name = digits + letters


    def reset(self):
        self.name = ''
        self.turn_on()
