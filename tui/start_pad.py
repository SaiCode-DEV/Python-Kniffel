import curses
from common_resources import *


def show_pad(std_scr):
    height, width = std_scr.getmaxyx()

    for i in range(MENU_ARRAY_LEN):
        start_y = int((height // 2) - 2) + 2 * i
        start_x = int(width // 2) - int(len(START_MENU[i]) // 2) - len(START_MENU[i]) % 2
        std_scr.addstr(start_y, start_x, START_MENU[i], curses.color_pair(3))
