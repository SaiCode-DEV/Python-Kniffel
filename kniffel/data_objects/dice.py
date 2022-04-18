import random


class Dice:
    def __init__(self):
        self.__value = random.randint(1, 6)
        self.selected = False
        self.locked = False

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val: int):
        if 0 < val < 7:
            self.__value = val

    def roll(self):
        self.__value = random.randint(1, 6)
