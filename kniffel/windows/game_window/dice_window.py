"""
This module contains the needed functionality for rendering a Dice-Set onto a window
The logic for a DiceSet is found in the dice_controller_module
"""
import curses
from typing import List, Tuple

from kniffel import common
from kniffel.data_objects.dice import Dice

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
    """
    The DiceWindow takes in a window in which it will render a passed DiceSet
    """
    @staticmethod
    def get_required_size() -> Tuple[int, int]:
        """
        Calculates the minimum Screen space needed for rendering a set of dice
        @return: min_y, min_x
        """
        return GAP_SIZE * 2 + common.DICE_COUNT * (len(DICE_BORDER) + GAP_SIZE), len(DICE_BORDER[0])

    @staticmethod
    def get_control_string() -> str:
        """
        Returns the Control-String with all available Controls for the Dice-Window
        @return:
        """
        return common.LABEL_CONTROL_DESCRIPTION_DICE_SET

    def __init__(self, window: curses.window):
        self.__window = window
        self.__show_selected = True

    def render(self, dice: List[Dice]):
        """
        Renders the passed List[Dice] to the window passed in the constructor
        @param dice: List[Dice] wich is rendered
        """
        self.__window.clear()
        self.__window.refresh()

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
        """
        Changes the state of the renderer when show is set to True a selected Dice will be rendered
        with the appropriate property
        @param show: True=Selected Dice are rendered with selection property,
         False selected Dice are not rendered with selection property
        """
        self.__show_selected = show

    def __render_single_dice(self, dice: Dice):
        """
        Draws a single Dice with border at the current Curser-Position on the window
        @param dice: Dice which is rendered
        """
        current_y, current_x = self.__window.getyx()
        max_y, max_x = self.__window.getmaxyx()
        if current_x + len(DICE_BORDER[0]) > max_x:
            print("Failed to draw dice X position to high")
            return
        if current_y + len(DICE_BORDER) > max_y:
            print("Failed to draw dice Y position to high")
            return
        self.__draw_dice_border(dice)
        self.__window.move(current_y + 1, current_x + 1)
        self.__draw_dice_face(dice)

    def __draw_dice_border(self, dice: Dice):
        """
        Draws a single Dice-Border at the current Curser-Position on the window
        @param dice: Dice of which the border is rendered
        """
        current_y, current_x = self.__window.getyx()
        iteration = 0
        for border in DICE_BORDER:
            if dice.locked:
                self.__window.attron(curses.color_pair(common.COLOR_DICE_LOCKED))
            self.__window.addstr(current_y + iteration, current_x, border)
            self.__window.attroff(common.SELECTED_OPTION)
            self.__window.attroff(curses.color_pair(common.COLOR_DICE_LOCKED))
            iteration += 1

    def __draw_dice_face(self, dice: Dice):
        """
        Draws a single Dice-Face at the current Curser-Position on the window
        @param dice: Dice of which the face is rendered
        """
        current_y, current_x = self.__window.getyx()
        dice_face = DICE_FACES[dice.value - 1]
        iteration = 0
        for face in dice_face:
            if dice.selected and self.__show_selected:
                self.__window.attron(common.SELECTED_OPTION)
            self.__window.addstr(current_y + iteration, current_x, face)
            self.__window.attroff(common.SELECTED_OPTION)
            iteration += 1
