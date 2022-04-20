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

    def render(self, points: List[Point]):
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

        # Print game pad
        line_count = 0
        for line in common.TEST_GAME_PAD:
            self.__window.addstr(line_count + y_off + len(common.TEST_NAME_PAD), x_off, line, curses.color_pair(4))
            line_count += 1

        # Print first player points card
        for i in range(len(common.TEST_POINTS_PAD)):
            start_y = y_off + len(common.TEST_NAME_PAD) + i + 1
            start_x = x_off + len(common.TEST_GAME_PAD[1])

            test_y = y_off + len(common.TEST_NAME_PAD) + 1
            test_x = x_off + len(common.TEST_GAME_PAD[1])

            str_to_add = common.TEST_POINTS_PAD[i].format(self.__selected_player.value)

            if not self.__show_selected:
                self.__window.attron(curses.color_pair(4))
            else:
                self.__window.attron(curses.color_pair(5))

            self.__window.addstr(test_y, test_x, str_to_add)
            self.__window.attroff(curses.color_pair(4))
            self.__window.attroff(curses.color_pair(5))

            self.__window.addstr(start_y, start_x + 5, "!", curses.color_pair(4))
            self.__window.addstr(start_y, start_x + 11, "!", curses.color_pair(4))

        self.__window.addstr(1 + y_off, x_off, name_str, curses.color_pair(4))
        self.__window.refresh()

    def handle_input(self, ch: chr):
        pass

    def show_selected(self, show):
        self.__show_selected = show

    def change_player(self, player: Player):
        self.__selected_player = player
