import curses
from Player import Player
from Enum_card_number import Number
from common_resources import *


class Card:
    def __init__(self, player: Player, points: int = 0, player_num: Number = Number.FIRST):
        self.__player = player
        self.__points = points
        self.__player_num = player_num

    def get_created_points_str(self):
        points_to_add = self.__points

        if points_to_add == 0:
            points_to_add = " "

        attachment = " " * ((5 - len(str(points_to_add))) // 2)
        ending = " " * (5 - len(str(points_to_add)) - len(attachment))

        return attachment + str(points_to_add) + ending

    def show(self):
        curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)

        window = curses.newwin(PLAYER_CARD_HEIGHT + 1, PLAYER_CARD_WIDTH, TITLE_ARRAY_LEN + 1, PADDING)

        attachment = " " * (len(PLAYER_CARD[0]) // 2 - len(self.__player.name) // 2)
        ending = " " * (len(PLAYER_CARD[0]) - len(self.__player.name) - len(attachment))
        name_str = attachment + self.__player.name + ending

        for i in range(len(PLAYER_CARD)):
            str_to_add = PLAYER_CARD[i].format(self.get_created_points_str(), self.get_created_points_str())
            window.addstr(i, 0, str_to_add, curses.color_pair(4))

        window.addstr(1, 0, name_str, curses.color_pair(4))

        window.refresh()
