import curses
from typing import Tuple, List, Dict

from data_objects.combinations import Combinations
from kniffel import common
from kniffel.data_objects.point import Point
from kniffel.data_objects.player import Player


class GameCard:
    def __init__(self, window: curses.window):
        self.__show_selected = False
        self.__selected_str = 0
        self.__selected_player = Player.FIRST
        self.__window = window
        self.__points = Point()

    @staticmethod
    def get_required_size() -> Tuple[int, int]:
        return len(common.GAME_PAD), len(common.GAME_PAD[0])

    @staticmethod
    def get_control_string() -> str:
        return common.LABEL_CONTROL_DESCRIPTION_GAME_CARD

    @staticmethod
    def get_created_points_str(value: str = ""):
        attachment = " " * ((5 - len(value)) // 2)
        ending = " " * (5 - len(value) - len(attachment))

        return attachment + value + ending

    def render(self, points: List[List[Point]]):
        self.__window.clear()

        curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_CYAN)

        card_width = len(common.TEST_GAME_PAD[0])
        attachment = " " * (card_width // 2 - len(common.GAME_TITLE) // 2)
        ending = " " * (card_width - len(common.GAME_TITLE) - len(attachment))
        name_str = attachment + common.GAME_TITLE + ending

        max_y, max_x = self.__window.getmaxyx()
        x_off = (max_x - len(common.GAME_PAD[0])) // 2
        y_off = (max_y - len(common.GAME_PAD)) // 2

        # Print name pad
        for i in range(len(common.TEST_NAME_PAD)):
            self.__window.addstr(y_off + i, x_off, common.TEST_NAME_PAD[i], curses.color_pair(4))

        iteration = 0
        for column in points:
            y_off_column = y_off + len(common.TEST_NAME_PAD) + 1
            x_off_column = x_off + len(common.TEST_GAME_PAD[1]) + iteration * 6
            self.__window.move(y_off_column, x_off_column)
            self.__render_column(column)
            iteration += 1

        # Print game pad
        line_count = 0
        for line in common.TEST_GAME_PAD:
            self.__window.addstr(line_count + y_off + len(common.TEST_NAME_PAD), x_off, line, curses.color_pair(4))
            line_count += 1

        self.__window.addstr(1 + y_off, x_off, name_str, curses.color_pair(4))
        self.__window.refresh()

    def __render_column(self, column: List[Point]):
        y_off, x_off = self.__window.getyx()
        for i in range(len(common.TEST_POINTS_PAD)):
            if i % 2 == 0:
                index = i // 2
                point = column[index]
                if not self.__show_selected and point.selected:
                    self.__window.attron(curses.color_pair(5))
                else:
                    self.__window.attron(curses.color_pair(4))
                str_to_add = common.TEST_POINTS_PAD[i].format(point.value)
                self.__window.addstr(y_off + i, x_off, str_to_add.center(5))
                self.__window.attroff(curses.color_pair(4))
                self.__window.attroff(curses.color_pair(5))
            else:
                str_to_add = common.TEST_POINTS_PAD[i]
                self.__window.addstr(y_off + i, x_off, str_to_add, curses.color_pair(4))

            self.__window.addstr("!", curses.color_pair(4))
            self.__window.refresh()

    def handle_input(self, ch: chr):
        pass

    def show_selected(self, show):
        self.__show_selected = show

    def change_player(self, player: Player):
        self.__selected_player = player
