import curses
from typing import Tuple

from kniffel import common


class GameCard:
    def __init__(self, window: curses.window):
        self.window = window
        self.__points = 0

    @staticmethod
    def get_required_size() -> Tuple[int, int]:
        return len(common.GAME_PAD), len(common.GAME_PAD[0])

    @staticmethod
    def get_control_string() -> str:
        return common.LABEL_CONTROL_DESCRIPTION_GAME_CARD

    def get_created_points_str(self):
        points_to_add = self.__points

        if points_to_add == 0:
            points_to_add = " "

        attachment = " " * ((5 - len(str(points_to_add))) // 2)
        ending = " " * (5 - len(str(points_to_add)) - len(attachment))

        return attachment + str(points_to_add) + ending

    def render(self):
        self.window.clear()
        self.window.refresh()

        curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)
        card_width = len(common.GAME_PAD[0])
        attachment = " " * (card_width // 2 - len(common.GAME_TITLE) // 2)
        ending = " " * (card_width - len(common.GAME_TITLE) - len(attachment))
        name_str = attachment + common.GAME_TITLE + ending

        max_y, max_x = self.window.getmaxyx()
        x_off = (max_x - len(common.GAME_PAD[0])) // 2
        y_off = (max_y - len(common.GAME_PAD)) // 2

        line_count = 0
        for line in common.GAME_PAD:
            str_to_add = line.format(self.get_created_points_str(), self.get_created_points_str())
            self.window.addstr(line_count + y_off, x_off, str_to_add, curses.color_pair(4))
            line_count += 1

        self.window.addstr(1 + y_off, x_off, name_str, curses.color_pair(4))
        self.window.refresh()

    def handle_input(self, ch: chr):
        pass
