import random


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
            dice = sorted(dice_roller)
        else:
            dice = sorted([Character.roll_dice() for _ in range(4)])
        return sum(dice[1:])


    @staticmethod         
    def roll_dice():
        return random.randint(1, 6)


def modifier(value):
    return (value - 10) // 2
    