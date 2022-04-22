from __future__ import annotations

import curses

import common
import key_codes

from data_objects.point import Point
from windows.game_window.game_card import GameCard
from typing import List


class CardController:
    def __init__(self, game_card: GameCard):
        self.game_card = game_card
        self.__selected_player = None
        self.__selected_combination = None

        self.__combinations: List[List[Point]] = []

        for _ in range(common.PLAYER_COUNT):
            column = []
            for i in range(common.COMBINATIONS_COUNT):
                column.append(Point())
            self.__combinations.append(column)

        self.__combinations[0][0].selected = True
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
        if ch == curses.KEY_DOWN:
            self.__combinations[self.__selected_player][self.__selected_combination].selected = False
            self.__selected_combination = (self.__selected_combination + 1) % common.COMBINATIONS_COUNT
            self.__combinations[self.__selected_player][self.__selected_combination].selected = True
        if ch == curses.KEY_UP:
            self.__combinations[self.__selected_player][self.__selected_combination].selected = False
            self.__selected_combination -= 1
            if self.__selected_combination < 0:
                self.__selected_combination = common.COMBINATIONS_COUNT - 1
            self.__combinations[self.__selected_player][self.__selected_combination].selected = True
        # TODO changing a player does not work correctly
        if ch == curses.KEY_ENTER or ch == 10 or ch == 13 or ch == key_codes.VK_NUMPAD_ENTER:

            self.__combinations[self.__selected_player][self.__selected_combination].value = 5  # TODO test

            self.__combinations[self.__selected_player][self.__selected_combination].selected = False
            self.__selected_player = (self.__selected_player + 1) % common.PLAYER_COUNT
            self.__combinations[self.__selected_player][self.__selected_combination].selected = True
        self.game_card.render(self.__combinations)

    def get_card(self):
        return [card for card in self.__combinations]

    def show_selected(self, show: bool):
        self.game_card.show_selected(show)
