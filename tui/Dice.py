import random
import common


class Dice:
    def __init__(self, value: int = 1):
        self.__activate = True

        if value > 0 & value < 7:
            self.__value = value
        else:
            print("Value error.")

    @property
    def value(self):
        return self.__value

    def set_activate(self, activate: bool):
        self.__activate = activate

    def roll(self, is_roll: bool):
        if is_roll:
            self.__value = random.randrange(1, 7, 1)

    def show(self):
        if self.__value == 1:
            return common.ONE
        if self.__value == 2:
            return common.TWO
        if self.__value == 3:
            return common.THREE
        if self.__value == 4:
            return common.FOUR
        if self.__value == 5:
            return common.FIVE
        if self.__value == 6:
            return common.SIX
