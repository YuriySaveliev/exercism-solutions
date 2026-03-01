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

    
    def ability(self, dice_roller=None):
        if dice_roller:
            dices = sorted(dice_roller)
        else:
            dices = sorted([Character.roll_dice() for _ in range(4)])
        return sum(dices[1:])


    @staticmethod         
    def roll_dice():
        return random.randint(1, 6)


def modifier(value):
    return (value - 10) // 2
    