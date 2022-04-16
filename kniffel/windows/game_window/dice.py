import random
import curses
from typing import List, Tuple

import common
from kniffel.game_logic.value_calculator import validate_throw
import key_codes

DICE_FACES = [
    ["       ", "   ¤   ", "       "],
    [" ¤     ", "       ", "     ¤ "],
    [" ¤     ", "   ¤   ", "     ¤ "],
    [" ¤   ¤ ", "       ", " ¤   ¤ "],
    [" ¤   ¤ ", "   ¤   ", " ¤   ¤ "],
    [" ¤   ¤ ", " ¤   ¤ ", " ¤   ¤ "]
]

DICE_BORDER = ["---------", "!       !", "!       !", "!       !", "---------"]
DICE_COUNT = 5
GAP_SIZE = 2


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

    def render(self, window: curses.window):
        y, x = window.getyx()
        max_y, max_x = window.getmaxyx()
        if x + len(DICE_BORDER[0]) > max_x:
            print("Failed to draw dice X position to high")
            return
        if y + len(DICE_BORDER) > max_y:
            print("Failed to draw dice Y position to high")
            return
        self.draw_border(window)
        window.move(y + 1, x + 1)
        self.draw_face(window)

    def draw_border(self, window: curses.window):
        y, x = window.getyx()
        for i in range(len(DICE_BORDER)):
            if self.locked:
                window.attron(common.COLOR_DICE_LOCKED)
            window.addstr(y + i, x, DICE_BORDER[i])
            window.attroff(common.SELECTED_OPTION)
            window.attroff(common.COLOR_DICE_LOCKED)

    def draw_face(self, window: curses.window):
        y, x = window.getyx()
        dice_face = DICE_FACES[self.__value - 1]
        for i in range(len(dice_face)):
            if self.selected:
                window.attron(common.SELECTED_OPTION)
            window.addstr(y + i, x, dice_face[i])
            window.attroff(common.SELECTED_OPTION)


class DiceSet:
    @staticmethod
    def get_required_size() -> Tuple[int, int]:
        return GAP_SIZE * 2 + DICE_COUNT * (len(DICE_BORDER) + GAP_SIZE), len(DICE_BORDER[0])

    @staticmethod
    def get_control_string() -> str:
        return common.LABEL_CONTROL_DESCRIPTION_DICE_SET

    def __init__(self, window: curses.window):
        self.__window = window
        self.__dice = []
        for i in range(DICE_COUNT):
            self.__dice.append(Dice())

        self.__selected = 0
        self.__dice[self.__selected].selected = True

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
        if ch == key_codes.VK_SPACE:
            for dice in self.__dice:
                if not dice.locked:
                    dice.roll()
        # 10/13 are added to catch enter from numeric keyboard
        if ch == curses.KEY_ENTER or ch == 10 or ch == 13 or ch == key_codes.VK_NUMPAD_ENTER:
            self.__dice[self.__selected].locked = self.__dice[self.__selected].locked ^ 1
        self.render()

    def render(self):
        self.__window.clear()
        self.__window.refresh()

        max_y, max_x = self.__window.getmaxyx()
        off_top = (max_y - (DICE_COUNT * (len(DICE_BORDER) + GAP_SIZE) - GAP_SIZE)) // 2
        dice_x = (max_x - len(DICE_BORDER[0])) // 2
        for i in range(DICE_COUNT):
            dice_y = off_top + i * (len(DICE_BORDER) + GAP_SIZE)
            self.__window.move(dice_y, dice_x)
            self.__dice[i].render(self.__window)
        self.__window.refresh()

    def get_dice(self):
        return [dice.value for dice in self.__dice]

    def set_dice(self, dices: List[int]):
        validate_throw(dices)
        for iteration in range(len(self.__dice)):
            self.__dice[iteration].value = dices[iteration]
