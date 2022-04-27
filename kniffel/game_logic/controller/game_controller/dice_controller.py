"""
The dice_controller module contains all the functionality for rolling,
retrieving and navigating a dice-set
"""

from __future__ import annotations

import copy
import curses
from time import sleep
from typing import List, TYPE_CHECKING

from kniffel import common
from kniffel import key_codes
from kniffel.data_objects.dice import Dice
from kniffel.game_logic.value_calculator import validate_throw
from kniffel.windows.game_window.dice_window import DiceWindow

# to avoid a circular import
if TYPE_CHECKING:
    from game_logic.controller.game_controller.game_controller import GameController


class DiceController:
    """
    The Dice Controller is supposed to be used as an abstraction to a dice-set.
    The dice-set is rendered to the passed DiceWindow
    """

    def __init__(self, dice_window: DiceWindow, game_controller: GameController):
        self.game_controller = game_controller
        self.dice_window = dice_window
        self.__dice = []
        for _ in range(common.DICE_COUNT):
            self.__dice.append(Dice())
        self.__dice[0].selected = True
        self.__selected = 0
        self.__roll_count = 0

    @property
    def selected(self) -> int:
        """
        Getter for the index of the currently selected dice
        """
        return self.__selected

    @selected.setter
    def selected(self, selected_index: int):
        """
        selects the dice with the passed index
        @param selected_index: index of dice to be selected
        """
        self.__dice[self.selected].selected = False
        self.__selected = selected_index
        self.__dice[self.selected].selected = True

    @property
    def roll_count(self) -> int:
        """
        returns the current roll count
        """
        return self.__roll_count

    def handle_input(self, character: chr):
        """
        Decides what to do with a users input
        @param character: chr User input
        """
        if character == curses.KEY_DOWN:
            self.__dice[self.__selected].selected = False
            self.__selected = (self.__selected + 1) % len(self.__dice)
            self.__dice[self.__selected].selected = True
        if character == curses.KEY_UP:
            self.__dice[self.__selected].selected = False
            self.__selected -= 1
            if self.__selected < 0:
                self.__selected = len(self.__dice) - 1
            self.__dice[self.__selected].selected = True
        if character == key_codes.VK_SPACE and not self.__is_all_locked():
            if not self.__is_roll_allowed():
                self.game_controller.display_message(common.ERROR_NO_MORE_ROLLS)
                return
            self.roll(common.ROLL_COUNT_ANIMATION)
            return
        if key_codes.is_enter(character):
            self.__dice[self.__selected].locked = self.__dice[self.__selected].locked ^ 1
        self.dice_window.render(self.__dice)

    def roll(self, roll_count: int):
        """
        Rolls the dice and displays them with a nice animation,
        during the animation this method is blocking
        @param roll_count: number of times the dice should be rolled
        """
        self.__roll_count += 1
        for iteration in range(roll_count):
            for dice in self.__dice:
                if not dice.locked:
                    dice.roll()
            self.dice_window.render(self.__dice)
            if iteration != roll_count - 1:
                sleep(common.ANIMATION_DELAY_ROLL)

    def get_dice(self) -> List[Dice]:
        """
        Getter for dice
        @return: List[Dice] The currently used dice set
        """
        return copy.deepcopy(self.__dice)

    def get_dice_values(self) -> List[int]:
        """
        Getter for dice values
        @return: List[int] The values of the current dice-set
        """
        return [dice.value for dice in self.__dice]

    def set_dice(self, dices: List[Dice]):
        """
        Sets the currently displayed dice value
        @param dices: values that the new dice should have
        """
        validate_throw([die.value for die in dices])
        iteration = 0
        for die in dices:
            self.__dice[iteration] = copy.deepcopy(die)
            if die.selected:
                self.__selected = iteration
            self.__dice[iteration].selected = False
            iteration += 1
        self.__dice[self.__selected].selected = True
        self.dice_window.render(self.__dice)

    def set_dice_value(self, dices: List[int]):
        """
        Sets the currently displayed dice value
        @param dices: values that the new dice should have
        """
        validate_throw(dices)
        iteration = 0
        for die in self.__dice:
            die.value = dices[iteration]
            iteration += 1
        self.dice_window.render(self.__dice)

    def unlock_all_dice(self):
        """
        unlocks all dice
        """
        for dice in self.__dice:
            dice.locked = False

    def lock_dice(self, dice_nr: int, locked: bool):
        """
        locks or unlocks a die depending on the locked value
        @param dice_nr: index of the die which is affected
        @param locked: True die gets locked, False die gets unlocked
        """
        self.__dice[dice_nr].locked = locked

    def is_locked(self, dice_nr: int) -> bool:
        """
        Checks weather a die in the dice-set is locked
        @param dice_nr: index of the dice for which the status is returned
        @return: True if the die is locked, False if not
        """
        return self.__dice[dice_nr].locked

    def __is_all_locked(self) -> bool:
        """
        Checks if all dice are locked
        @return: True if all are locked False if at least one isn't
        """
        for dice in self.__dice:
            if not dice.locked:
                return False
        return True

    def __is_roll_allowed(self):
        """
        Checks if a roll in this throw is allowed
        @return: True if allowed, False if not
        """
        return self.__roll_count < common.MAX_ROLL_COUNT

    def set_roll_count(self, roll_count: int):
        """
        sets the roll count to the passed number
        """
        self.__roll_count = roll_count

    def reset_roll_count(self):
        """
        Resets the roll counter to 0 usually done when players change
        """
        self.__roll_count = 0

    def show_selected(self, show: bool):
        """
        Sets weather the selected dice are shown with their special property
        @param show: True selected are show, False they are not
        """
        self.dice_window.show_selected(show)
