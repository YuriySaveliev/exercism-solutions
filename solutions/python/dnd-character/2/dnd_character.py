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
        dices = sorted([Character.roll_dice() for _ in range(4)], reverse=True)
        return sum(dices[:3])
                
    @staticmethod         
    def roll_dice():
        return random.randint(1, 6)


def modifier(value):
    return (value - 10) // 2
    