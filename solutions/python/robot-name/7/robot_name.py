import string
import random
class Robot:
    previous_names = set()
    
    def __init__(self):
        self.reset()
        
    def reset(self):
        while True:
            generated_name = ''.join(random.choices(string.ascii_uppercase, k=2) + random.choices(string.digits, k=3))
            
            if generated_name not in Robot.previous_names:
                self.name = generated_name
                Robot.previous_names.add(self.name)
                break