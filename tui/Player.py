import curses
from common_resources import *


class Player:
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def show_card(self, std_scr):
        padding = 2
        height, width = std_scr.getmaxyx()
        curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)

        for i in range(PLAYER_CARD_FIRST_ARRAY_LEN):
            start_y = TITLE_ARRAY_LEN + padding + i
            start_x = width - padding - PLAYER_CARD_STR_LEN

            start_name_x = PLAYER_CARD_STR_LEN // 2 - len(self.__name) // 2
            start_name_y = TITLE_ARRAY_LEN + padding

            std_scr.addstr(start_y, start_x, PLAYER_CARD_FIRST[i], curses.color_pair(4))
            std_scr.addstr(start_name_y, start_name_x, self.__name, curses.color_pair(4))

        for i in range(PLAYER_CARD_SECOND_ARRAY_LEN):
            start_y = TITLE_ARRAY_LEN + padding + i
            start_x = padding
            std_scr.addstr(start_y, start_x, PLAYER_CARD_SECOND[i], curses.color_pair(4))

