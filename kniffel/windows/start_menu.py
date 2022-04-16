import curses

from kniffel import common

OPTIONS = [
    common.LABEL_MANU_PLAY,
    common.LABEL_MENU_PLAY_BOT,
    common.LABEL_MENU_ESCAPE
]


class StartMenu:

    def __init__(self, window: curses.window):
        self.window = window

    def render(self):
        height, width = self.window.getmaxyx()

        iteration = 0
        for line in OPTIONS:
            start_y = int((height // 2) - 2) + 2 * iteration
            start_x = int(width // 2) - int(len(line) // 2) - len(line) % 2
            self.window.addstr(start_y, start_x, line, curses.color_pair(3))
