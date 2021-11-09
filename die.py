from random import randint

class Die:
    """a class to express dice"""

    def __init__(self, num_sides=6):
        """default is a 6 sides die"""
        self.num_sides = num_sides

    def roll(self):
        """roll a die and return a number"""
        return randint(1, self.num_sides)
