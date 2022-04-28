"""
This modul contains the needed functionality for rendering a game-card into a window
"""
import curses
from typing import List

from kniffel.windows.game_window import players_card

from kniffel import common
from kniffel.data_objects.point import Point


class ResultCard:
    """
    The ResultCard takes in a window it will render a result card
    """
    def __init__(self, window: curses.window):
        self.__window = window

    @staticmethod
    def get_required_size():
        """
        Return height and width needed for rendering a result card
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

        max_y, max_x = self.__window.getmaxyx()
        x_off = (max_x - len(common.RESULT_PAD[0])) // 2
        y_off = (max_y - len(common.RESULT_PAD)) // 2

        # Print header pad
        players_card.draw_header(self.__window, y_off, x_off)

        # Print result card
        count = 0
        for line in common.RESULT_PAD:
            self.__window.addstr(count + y_off + len(common.NAME_PAD), x_off, line,
                                 curses.color_pair(common.COLOR_PAIR_BLACK_WHITE))
            count += 1

        count = 0
        for column in points:
            y_off_column = y_off + len(common.NAME_PAD) + 1
            x_off_column = x_off + len(common.NAME_PAD[1]) + count * 6
            self.__window.move(y_off_column, x_off_column)
            self.__render_column(column)
            count += 1

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

                str_to_add = line.format(point).center(5)

                self.__window.addstr(y_off + count, x_off - 12, str_to_add.center(5),
                                     curses.color_pair(common.COLOR_PAIR_BLACK_WHITE))
            else:
                str_to_add = line
                self.__window.addstr(y_off + count, x_off - 12, str_to_add,
                                     curses.color_pair(common.COLOR_PAIR_BLACK_WHITE))

            count += 1

            self.__window.addstr("!", curses.color_pair(common.COLOR_PAIR_BLACK_WHITE))

            self.__window.refresh()
