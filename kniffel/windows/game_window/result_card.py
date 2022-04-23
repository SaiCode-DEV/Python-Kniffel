"""
The module contains
"""
import curses
from typing import List, Dict

from kniffel.data_objects.point import Point

from data_objects.combinations import Combinations
from kniffel import common


class ResultCard:
    """
    The ResultCard takes in a window
    """
    def __init__(self, window: curses.window):
        self.__window = window
        self.__show_selected = False

    @staticmethod
    def get_required_size():
        """
        Return height and width needed for rendering a game card
        @return height, width
        """
        return len(common.RESULT_PAD), len(common.RESULT_PAD[0])

    @staticmethod
    def get_control_string() -> str:
        """
        Returns the control-string with all available controls for the result card
        """
        return common.LABEL_CONTROL_DESCRIPTION_RESULT_CARD

    def render(self, points: List[List[Point]]):
        """
        Renders the passed List[List[Point]] to the window passed in the constructor
        @param points: List[List[Point]] which is rendered
        """
        self.__window.clear()

        # TODO COLOR INI COMMON
        curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)

        card_width = len(common.RESULT_PAD[0])
        attachment = " " * (card_width // 2 - len(common.GAME_TITLE) // 2)
        ending = " " * (card_width - len(common.GAME_TITLE) - len(attachment))
        name_str = attachment + common.GAME_TITLE + ending

        max_y, max_x = self.__window.getmaxyx()
        x_off = (max_x - len(common.RESULT_PAD[0])) // 2
        y_off = (max_y - len(common.RESULT_PAD)) // 2

        # Print name pad
        count: int = 0
        for line in common.TEST_NAME_PAD:
            self.__window.addstr(y_off + count, x_off, line, curses.color_pair(4))
            count += 1

        # Print result card
        line_count = 0
        for line in common.RESULT_PAD:
            self.__window.addstr(line_count + y_off + len(common.TEST_NAME_PAD), x_off, line, curses.color_pair(4))
            line_count += 1

        count = 0
        for column in points:
            y_off_column = y_off + len(common.TEST_NAME_PAD) + 1
            x_off_column = x_off + len(common.TEST_GAME_PAD[1]) + count * 6
            self.__window.move(y_off_column, x_off_column)
            self.__render_column(column)
            count += 1

        self.__window.addstr(1 + y_off, x_off, name_str, curses.color_pair(4))
        self.__window.refresh()

    def __render_column(self, column: List[Point]):
        """
        Draws column at the current curser-position on the window
        @param column: column which is rendered
        """
        y_off, x_off = self.__window.getyx()
        result_points = [0, 0, 0, 0]
        top_points = range(0, 6)
        all_top_points = range(0, 13)

        index: int = 0
        for point in column:
            if index in top_points:
                result_points[0] += point.value
            if result_points[0] >= 63:
                result_points[1] = 35
            if index in all_top_points:
                result_points[2] += point.value
            result_points[3] = result_points[1] + result_points[2]
            index += 1

        count: int = 0
        for line in common.RESULT_POINTS_PAD:
            if count % 2 == 0:
                index = count // 2
                point = result_points[index]

                if self.__show_selected and point.selected:
                    self.__window.attron(curses.color_pair(5))
                else:
                    self.__window.attron(curses.color_pair(4))

                test = line.format(point)

                self.__window.addstr(y_off + count, x_off, test.center(5))
                self.__window.attroff(curses.color_pair(4))
                self.__window.attroff(curses.color_pair(5))
            else:
                str_to_add = line
                self.__window.addstr(y_off + count, x_off, str_to_add, curses.color_pair(4))

            count += 1
            self.__window.addstr("!", curses.color_pair(4))
            self.__window.refresh()

    def show_selected(self, show):
        self.__show_selected = show
