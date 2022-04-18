import curses
from time import sleep
from typing import List

import common
import key_codes
from data_objects.dice import Dice
from game_logic.value_calculator import validate_throw
from windows.game_window.dice_window import DiceWindow


class DiceController:
    def __init__(self, dice_window: DiceWindow):
        self.__selected = None
        self.dice_window = dice_window
        self.__dice = []
        for i in range(common.DICE_COUNT):
            self.__dice.append(Dice())
        self.__dice[0].selected = True
        self.__selected = 0

    @property
    def selected(self) -> int:
        return self.__selected

    def handle_input(self, ch: chr):
        if ch == curses.KEY_DOWN:
            self.__dice[self.__selected].selected = False
            self.__selected = (self.__selected + 1) % len(self.__dice)
            self.__dice[self.__selected].selected = True
        if ch == curses.KEY_UP:
            self.__dice[self.__selected].selected = False
            self.__selected -= 1
            if self.__selected < 0:
                self.__selected = len(self.__dice) - 1
            self.__dice[self.__selected].selected = True
        # 10/13 are added to catch enter from numeric keyboard
        if ch == curses.KEY_ENTER or ch == 10 or ch == 13 or ch == key_codes.VK_NUMPAD_ENTER:
            self.__dice[self.__selected].locked = self.__dice[self.__selected].locked ^ 1
        self.dice_window.render(self.__dice)

    def roll(self, roll_count: int):
        for iteration in range(roll_count):
            for dice in self.__dice:
                if not dice.locked:
                    dice.roll()
            self.dice_window.render(self.__dice)
            if iteration != roll_count - 1:
                sleep(0.15)

    def get_dice(self):
        return [dice for dice in self.__dice]

    def get_dice_values(self):
        return [dice.value for dice in self.__dice]

    def set_dice(self, dices: List[int]):
        validate_throw(dices)
        for iteration in range(len(self.__dice)):
            self.__dice[iteration].value = dices[iteration]
        self.dice_window.render(self.__dice)

    def lock_dice(self, dice_nr: int, locked: bool):
        self.__dice[dice_nr].locked = locked

    def is_locked(self, dice_nr: int) -> bool:
        return self.__dice[dice_nr].locked

    def show_selected(self, show: bool):
        self.dice_window.show_selected(show)
