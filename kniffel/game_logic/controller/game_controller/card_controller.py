"""
The card_controller module contains all the functionality for entrance and navigating a game card
"""
from __future__ import annotations

import curses

from typing import TYPE_CHECKING
import common
import key_codes
from data_objects.combinations import Combinations

from windows.game_window.game_card import GameCard
from typing import TYPE_CHECKING
from kniffel.windows.game_window.result_card import ResultCard

# to avoid a circular import
if TYPE_CHECKING:
    from game_logic.controller.game_controller.game_controller import GameController


class CardController:
    """
    The CardController is supposed to be used as an abstraction to a game card.
    The game card is rendered to the passed Game-Card
    """
    def __init__(self, game_card: GameCard,
                 result_card: ResultCard,
                 game_controller: GameController):
        self.game_card = game_card
        self.result_card = result_card
        self.game_controller = game_controller
        self.__selected_player = None
        self.__selected_combination = None

        self.__selected_combination = 0
        self.__selected_player = 0

    @staticmethod
    def get_control_str() -> str:
        """
        Returns the control-string with all available controls for the game card
        """
        return common.LABEL_CONTROL_DESCRIPTION_GAME_CARD

    def handle_input(self, key):
        """
        Combination what to do with a users input
        @param key: chr User input
        """
        combinations = self.game_controller.get_game_state().points
        if key == curses.KEY_DOWN:
            combinations[self.__selected_player][self.__selected_combination].selected = False
            self.__selected_combination = \
                (self.__selected_combination + 1) % common.COMBINATIONS_COUNT
            combinations[self.__selected_player][self.__selected_combination].selected = True
        if key == curses.KEY_UP:
            combinations[self.__selected_player][self.__selected_combination].selected = False
            self.__selected_combination -= 1
            if self.__selected_combination < 0:
                self.__selected_combination = common.COMBINATIONS_COUNT - 1
            combinations[self.__selected_player][self.__selected_combination].selected = True
        if key in (curses.KEY_ENTER, 10, 13, key_codes.VK_NUMPAD_ENTER):
            self.game_controller.add_player_entry(Combinations(self.__selected_combination))
        self.game_card.render(combinations)

    def set_selected_player(self, player: int):
        """
        Set new player to navigate in combinations column
        @param player: new selected player
        """
        combinations = self.game_controller.get_game_state().points
        self.__unselect_all()
        self.__selected_player = player
        combinations[self.__selected_player][self.__selected_combination].selected = True

    def __unselect_all(self):
        combinations = self.game_controller.get_game_state().points
        for col in combinations:
            for point in col:
                point.selected = False

    def show_selected(self, show: bool):
        """
        Sets weather the selected combination are shown with their special property
        @param show: True selected are show, False they are not
        """
        self.game_card.show_selected(show)
