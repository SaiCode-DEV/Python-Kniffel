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
        attachment = " " * ((5 - len(str(self.__points))) // 2)
        ending = " " * (5 - len(str(self.__points)) - len(attachment))
        return attachment + str(self.__points) + ending

    def show_first_card(self, std_scr):
        padding = 3
        height, width = std_scr.getmaxyx()

        spacer = " " * 5

        curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)

        attachment = " " * (PLAYER_CARD_STR_LEN // 2 - len(self.__player.name) // 2)
        ending = " " * (PLAYER_CARD_STR_LEN - len(self.__player.name) - len(attachment))
        name_str = attachment + self.__player.name + ending

        start_name_y = TITLE_ARRAY_LEN + padding

        std_scr.attron(curses.color_pair(4))

        std_scr.addstr(start_name_y - 1, padding, name_str)
        std_scr.addstr(start_name_y - 2, padding, EMPTY_STR)

        start_y = TITLE_ARRAY_LEN + padding
        start_x = 0

        if self.__player_num == Number.FIRST:
            start_x = padding
        elif self.__player_num == Number.SECOND:
            start_x = width - PLAYER_CARD_STR_LEN - padding
        else:
            print("ERROR: Invalid player number")

        for i in range(PLAYER_CARD_SECOND_ARRAY_LEN):
            if PLAYER_CARD_FIRST[i].__contains__("→"):
                std_scr.addstr(start_y + i, start_x, PLAYER_CARD_FIRST[i].format(self.get_created_points_str(), spacer, spacer, spacer))
                continue
            std_scr.addstr(start_y + i, start_x, PLAYER_CARD_FIRST[i].format(spacer, spacer, spacer, spacer))

    def show_second_card(self, std_scr):
        padding = 3
        height, width = std_scr.getmaxyx()

        spacer = " " * 5

        curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)

        attachment = " " * (PLAYER_CARD_STR_LEN // 2 - len(self.__player.name) // 2)
        ending = " " * (PLAYER_CARD_STR_LEN - len(self.__player.name) - len(attachment))
        name_str = attachment + self.__player.name + ending

        start_name_y = TITLE_ARRAY_LEN + padding

        std_scr.attron(curses.color_pair(4))

        std_scr.addstr(start_name_y - 1, padding, name_str)
        std_scr.addstr(start_name_y - 2, padding, EMPTY_STR)

        start_y = TITLE_ARRAY_LEN + padding
        start_x = 0

        if self.__player_num == Number.FIRST:
            start_x = padding
        elif self.__player_num == Number.SECOND:
            start_x = width - PLAYER_CARD_STR_LEN - padding
        else:
            print("ERROR: Invalid player number")

        for i in range(PLAYER_CARD_SECOND_ARRAY_LEN):
            if PLAYER_CARD_FIRST[i].__contains__("→"):
                std_scr.addstr(start_y + i, start_x, PLAYER_CARD_FIRST[i].format(self.get_created_points_str(), spacer, spacer, spacer))
                continue
            std_scr.addstr(start_y + i, start_x, PLAYER_CARD_FIRST[i].format(spacer, spacer, spacer, spacer))



