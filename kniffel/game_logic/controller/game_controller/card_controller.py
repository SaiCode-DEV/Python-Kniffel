from __future__ import annotations

import curses

import common
import key_codes
from data_objects.combinations import Combinations

from windows.game_window.game_card import GameCard
from typing import TYPE_CHECKING

# to avoid a circular import
if TYPE_CHECKING:
    from game_logic.controller.game_controller.game_controller import GameController


class CardController:
    def __init__(self, game_card: GameCard, game_controller: GameController):
        self.game_card = game_card
        self.game_controller = game_controller
        self.__selected_player = None
        self.__selected_combination = None

        self.__selected_combination = 0
        self.__selected_player = 0

    @staticmethod
    def get_control_str() -> str:
        return common.LABEL_CONTROL_DESCRIPTION_GAME_CARD

        # if isinstance(self.current_card, GameCard):
        #    sub_str = GameCard.get_control_string()
        # elif isinstance(self.current_card, ResultCard):
        #    sub_str = ResultCard.get_control_string()

    def handle_input(self, ch):
        combinations = self.game_controller.get_game_state().points
        if ch == curses.KEY_DOWN:
            combinations[self.__selected_player][self.__selected_combination].selected = False
            self.__selected_combination = (self.__selected_combination + 1) % common.COMBINATIONS_COUNT
            combinations[self.__selected_player][self.__selected_combination].selected = True
        if ch == curses.KEY_UP:
            combinations[self.__selected_player][self.__selected_combination].selected = False
            self.__selected_combination -= 1
            if self.__selected_combination < 0:
                self.__selected_combination = common.COMBINATIONS_COUNT - 1
            combinations[self.__selected_player][self.__selected_combination].selected = True
        if ch == curses.KEY_ENTER or ch == 10 or ch == 13 or ch == key_codes.VK_NUMPAD_ENTER:
            self.game_controller.add_entry(Combinations(self.__selected_combination))
        self.game_card.render(combinations)

    def set_selected_player(self, player: int):
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
        self.game_card.show_selected(show)
