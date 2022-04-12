import curses
from common_resources import *


def show_player_cards(std_scr):
    padding = 2
    height, width = std_scr.getmaxyx()
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)

    for i in range(PLAYER_CARD_ARRAY_LEN):
        start_y = TITLE_ARRAY_LEN + padding + i
        start_x = width - padding - PLAYER_CARD_STR_LEN
        std_scr.addstr(start_y, start_x, PLAYER_CARD[i], curses.color_pair(4))

    for i in range(PLAYER_CARD_ARRAY_LEN):
        start_y = TITLE_ARRAY_LEN + padding + i
        start_x = padding
        std_scr.addstr(start_y, start_x, PLAYER_CARD[i], curses.color_pair(4))
