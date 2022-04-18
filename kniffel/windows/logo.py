import curses
from typing import List

import common


class Logo:
    @staticmethod
    def get_required_size() -> List[int]:
        return [len(common.LOGO), len(common.LOGO[0])]

    def __init__(self, window: curses.window):
        self.window = window

    def render(self):
        self.window.clear()
        self.window.refresh()
        max_y, max_x = self.window.getmaxyx()
        x_off = (max_x - len(common.LOGO[0])) // 2
        y_off = (max_y - len(common.LOGO)) // 2
        iteration = 0
        for line in common.LOGO:
            self.window.addstr(y_off+iteration, x_off, line)
            iteration += 1
        self.window.refresh()
