import string
import random


class Robot:
    def __init__(self):
        self.name = ''
        self.previous_names = []
        self.turn_on()
        

    def turn_on(self):
        while True:
            digits = ''.join(random.choices(string.ascii_uppercase, k=2))
            letters = ''.join(random.choices(string.digits, k=3))
            generated_name = digits + letters
            self.previous_names.append(self.name)

            if generated_name not in self.previous_names:
                self.name = generated_name
                break
        
    def reset(self):
        self.turn_on()
