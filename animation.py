import curses
from time import sleep
from common_resources import *


def show_start_animation(std_scr):
    height, width = std_scr.getmaxyx()

    start_x_title = int((width // 2) - (TITLE_STR_LEN // 2))
    start_y_title = int((height - TITLE_ARRAY_LEN) // 2)

    for state in LOADING:
        std_scr.clear()
        for i in range(TITLE_ARRAY_LEN):
            std_scr.addstr(start_y_title + i, start_x_title, state[i], curses.color_pair(1))
        std_scr.refresh()
        sleep(0.175)

    std_scr.clear()
    for i in range(TITLE_ARRAY_LEN):
        std_scr.addstr(start_y_title + i, start_x_title, title[i], curses.color_pair(1))
    std_scr.refresh()

    sleep(1)
