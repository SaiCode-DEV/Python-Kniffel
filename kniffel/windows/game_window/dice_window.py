import curses
from typing import List, Tuple

import common
from data_objects.dice import Dice

DICE_FACES = [
    ["       ", "   ¤   ", "       "],
    [" ¤     ", "       ", "     ¤ "],
    [" ¤     ", "   ¤   ", "     ¤ "],
    [" ¤   ¤ ", "       ", " ¤   ¤ "],
    [" ¤   ¤ ", "   ¤   ", " ¤   ¤ "],
    [" ¤   ¤ ", " ¤   ¤ ", " ¤   ¤ "]
]

DICE_BORDER = ["---------", "!       !", "!       !", "!       !", "---------"]
GAP_SIZE = 2


class DiceWindow:
    @staticmethod
    def get_required_size() -> Tuple[int, int]:
        return GAP_SIZE * 2 + common.DICE_COUNT * (len(DICE_BORDER) + GAP_SIZE), len(DICE_BORDER[0])

    @staticmethod
    def get_control_string() -> str:
        return common.LABEL_CONTROL_DESCRIPTION_DICE_SET

    def __init__(self, window: curses.window):
        self.__window = window
        self.__show_selected = True

    def render(self, dice: List[Dice]):
        self.__window.clear()
        self.__window.noutrefresh()

        max_y, max_x = self.__window.getmaxyx()
        off_top = (max_y - (common.DICE_COUNT * (len(DICE_BORDER) + GAP_SIZE) - GAP_SIZE)) // 2
        dice_x = (max_x - len(DICE_BORDER[0])) // 2
        iteration = 0
        for single_dice in dice:
            dice_y = off_top + iteration * (len(DICE_BORDER) + GAP_SIZE)
            self.__window.move(dice_y, dice_x)
            self.__render_single_dice(single_dice)
            iteration += 1
        self.__window.refresh()

    def show_selected(self, show: bool):
        self.__show_selected = show

    def __render_single_dice(self, dice: Dice):
        y, x = self.__window.getyx()
        max_y, max_x = self.__window.getmaxyx()
        if x + len(DICE_BORDER[0]) > max_x:
            print("Failed to draw dice X position to high")
            return
        if y + len(DICE_BORDER) > max_y:
            print("Failed to draw dice Y position to high")
            return
        self.__draw_dice_border(dice)
        self.__window.move(y + 1, x + 1)
        self.__draw_dice_face(dice)

    def __draw_dice_border(self, dice: Dice):
        y, x = self.__window.getyx()
        for i in range(len(DICE_BORDER)):
            if dice.locked:
                self.__window.attron(common.COLOR_DICE_LOCKED)
            self.__window.addstr(y + i, x, DICE_BORDER[i])
            self.__window.attroff(common.SELECTED_OPTION)
            self.__window.attroff(common.COLOR_DICE_LOCKED)

    def __draw_dice_face(self, dice: Dice):
        y, x = self.__window.getyx()
        dice_face = DICE_FACES[dice.value - 1]
        for i in range(len(dice_face)):
            if dice.selected and self.__show_selected:
                self.__window.attron(common.SELECTED_OPTION)
            self.__window.addstr(y + i, x, dice_face[i])
            self.__window.attroff(common.SELECTED_OPTION)
