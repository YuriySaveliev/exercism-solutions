import string
import random


class Robot:
    def __init__(self):
        self.name = ''
        self.turn_on()

    def turn_on(self):
        random.seed()
        digits = ''.join(random.choices(string.ascii_uppercase, k=2))
        letters = ''.join(random.choices(string.digits, k=3))
        self.name = digits + letters

    def reset(self):
        self.turn_on()
