import curses
from common_resources import *


class StartAnimation:

    def __init__(self):
        self.step_count = 0

    def show_next_step(self, std_scr):
        height, width = std_scr.getmaxyx()

        start_x_title = int((width // 2) - (TITLE_STR_LEN // 2))
        start_y_title = int((height - TITLE_ARRAY_LEN) // 2)

        std_scr.clear()
        if self.step_count <= len(LOADING):
            for i in range(TITLE_ARRAY_LEN):
                std_scr.addstr(start_y_title + i, start_x_title, LOADING[self.step_count], curses.color_pair(1))
        else:
            for i in range(TITLE_ARRAY_LEN):
                std_scr.addstr(start_y_title + i, start_x_title, title[i], curses.color_pair(1))
        std_scr.refresh()

        self.step_count += 1

        if self.step_count > len(LOADING):
            self.step_count = 0
