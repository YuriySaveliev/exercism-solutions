import random
import math


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    
    def ability(self):
        dices = [self.roll_dice() for i in range(1, 5)]
        min_dice = min(dices)
        dices = filter(lambda item: item != min_dice, dices)
        
        return sum(dices)
                
                
    def roll_dice(self):
        return random.randint(1, 6)


def modifier(value):
    return math.floor((value - 10) / 2)
