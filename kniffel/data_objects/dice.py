"""
The dice module contains the needed classes for storing the
current state of a diceset
"""
import random
from json import JSONEncoder
from typing import Dict


class Dice:
    """
    Dice holds all relevant data of a dice object
    """

    @staticmethod
    def from_json(data):
        """
        Marshals a Dice object from dict
        """
        dice = Dice()
        if not isinstance(data, Dict):
            return dice
        if "value" in data:
            dice.value = data["value"]
        if "selected" in data:
            dice.selected = data["selected"]
        if "locked" in data:
            dice.locked = data["locked"]
        return dice

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

    def __eq__(self, other):
        """
        checks if two dice objects are equal
        """
        if not isinstance(other, Dice):
            return False
        return self.value == other.value and self.locked == other.locked and self.selected == other.selected


class DiceEncoder(JSONEncoder):
    """
    Encoder used to to encode a Dice to json
    """

    def default(self, o):
        """
        used for encoding Dice to json
        """
        if not isinstance(o, Dice):
            return None

        return {
            "value": o.value,
            "selected": o.selected,
            "locked": o.locked
        }
