import curses
from typing import Tuple

from data_objects.game_state import GameState
from kniffel import common
from windows.logo import Logo

OPTIONS = [
    common.LABEL_MANU_PLAY,
    common.LABEL_MENU_PLAY_BOT,
    common.LABEL_MENU_ESCAPE
]


def get_screens(window: curses.window) -> Tuple[curses.window, curses.window]:
    max_y, max_x = window.getmaxyx()
    [logo_min_y, _] = Logo.get_required_size()
    logo_y = int(max_y * (logo_min_y / (logo_min_y + len(OPTIONS) * 2)))
    options_y = max_y - logo_y
    return window.subwin(logo_y, max_x, 0, 0), window.subwin(options_y, max_x, logo_y, 0)


class StartWindow:

    @staticmethod
    def get_required_size() -> Tuple[int, int]:
        [logo_y, logo_x] = Logo.get_required_size()
        max_x = logo_x
        for opt in OPTIONS:
            if len(opt) > max_x:
                max_x = len(opt)
        return logo_y + len(OPTIONS) * 2, max_x

    def __init__(self, std_scr: curses.window):
        logo_win, self.window = get_screens(std_scr)
        self.logo = Logo(logo_win)
        self.max_x = len(OPTIONS[0])
        for opt in OPTIONS:
            if len(opt) > self.max_x:
                self.max_x = len(opt)

    def render(self, game_state: GameState = None):
        self.window.clear()
        self.window.refresh()
        height, width = self.window.getmaxyx()

        iteration = 0
        start_x = (width - self.max_x) // 2
        for line in OPTIONS:
            start_y = int((height // 2) - 2) + iteration * 2
            self.window.addstr(start_y, start_x, line, curses.color_pair(3))
            iteration += 1
            self.window.refresh()
        self.logo.render()
