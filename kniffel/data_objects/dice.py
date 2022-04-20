"""
The dice module contains the needed classes for storing the
current state of a diceset
"""
import random


class Dice:
    """
    Dice holds all relevant data of a dice object
    """
    def __init__(self):
        self.__value = random.randint(1, 6)
        self.selected = False
        self.locked = False

    @property
    def value(self):
        """
        Getter for the value of the dice
        """
        return self.__value

    @value.setter
    def value(self, val: int):
        """
        Setter for the value of the dice
        the value is only set if it is between 1 and 6
        """
        if 0 < val < 7:
            self.__value = val

    def roll(self):
        """
        Sets the value of the dice to a random value between 1 and 6
        """
        self.__value = random.randint(1, 6)
