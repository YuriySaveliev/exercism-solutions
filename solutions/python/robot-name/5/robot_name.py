import string
import random

previous_names = set()

class Robot:
    def __init__(self):
        self.name = ''
        self.reset()
        
    def reset(self):
        while True:
            generated_name = ''.join(random.choices(string.ascii_uppercase, k=2) + random.choices(string.digits, k=3))
            previous_names.add(self.name)

            if generated_name not in previous_names:
                self.name = generated_name
                break
