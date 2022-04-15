import curses
from common_resources import *


def show_dices(std_scr):
    padding = 2

    height, width = std_scr.getmaxyx()
    start_x = int((width // 2) - (DICE_STR_LEN // 2))

    for i in range(DICE_ARRAY_LEN):
        start_y = TITLE_ARRAY_LEN + i + padding

        std_scr.addstr(start_y + DICE_ARRAY_LEN * 0, start_x, ONE[i], curses.color_pair(3))
        std_scr.addstr(start_y + DICE_ARRAY_LEN * 1, start_x, TWO[i], curses.color_pair(3))
        std_scr.addstr(start_y + DICE_ARRAY_LEN * 2, start_x, THREE[i], curses.color_pair(3))
        std_scr.addstr(start_y + DICE_ARRAY_LEN * 3, start_x, FOUR[i], curses.color_pair(3))
        std_scr.addstr(start_y + DICE_ARRAY_LEN * 4, start_x, FIVE[i], curses.color_pair(3))
        std_scr.addstr(start_y + DICE_ARRAY_LEN * 5, start_x, SIX[i], curses.color_pair(3))
