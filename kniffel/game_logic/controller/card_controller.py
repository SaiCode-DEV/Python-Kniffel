from __future__ import annotations

import curses

import common

from data_objects.point import Point
from data_objects.player import Player
from windows.game_window.game_card import GameCard
from typing import TYPE_CHECKING


class CardController:
    def __init__(self, game_card: GameCard):
        self.__selected_player = Player.FIRST
        self.game_card = game_card
        self.__selected_point = None

        self.__points = []
        for i in range(common.POINTS_COUNT):
            self.__points.append(Point())

        self.__points[0].selected = True
        self.__points[0].position = 0
        self.__selected_point = 0

    def get_control_str(self) -> str:
        return ""
        # if isinstance(self.current_card, GameCard):
        #    sub_str = GameCard.get_control_string()
        # elif isinstance(self.current_card, ResultCard):
        #    sub_str = ResultCard.get_control_string()

    def handle_input(self, ch):
        if ch == curses.KEY_DOWN:
            self.__points[self.__selected_point].selected = False
            self.__selected_point = (self.__selected_point + 1) % common.POINTS_COUNT
            self.__points[self.__selected_point].position = self.__selected_point
            self.__points[self.__selected_point].selected = True
        if ch == curses.KEY_UP:
            self.__points[self.__selected_point].selected = False
            self.__selected_point -= 1
            if self.__selected_point < 0:
                self.__selected_point = common.POINTS_COUNT - 1
            self.__points[self.__selected_point].position = self.__selected_point
            self.__points[self.__selected_point].selected = True
        if ch == curses.KEY_ENTER:
            if not self.__points[self.__selected_point].completed:
                self.__points[self.__selected_point].completed = True
                self.__points[self.__selected_point].save_value(15, self.__selected_point)
            else:
                print("Combination is completed. Select another combination")
        self.game_card.render([self.__points])

    def show_selected(self, show: bool):
        self.game_card.show_selected(show)

    def change_player(self):
        if self.__selected_player is Player.FIRST:
            self.__selected_player = Player.SECOND
        elif self.__selected_player is Player.SECOND:
            self.__selected_player = Player.FIRST

        self.game_card.change_player(self.__selected_player)
