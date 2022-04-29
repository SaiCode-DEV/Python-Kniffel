"""
This module contains the needed functionality for rendering a game-card into a window
The logic for a game-card is found in the card_controller_module
"""
import curses
from typing import Tuple, List

from kniffel.windows.game_window import players_card
from kniffel import common
from kniffel.data_objects.point import Point


class GameCard:
    """
    GameCard class takes in a window it will render a game card
    """
    def __init__(self, window: curses.window):
        self.__show_selected = False
        self.__window = window

    @staticmethod
    def get_required_size() -> Tuple[int, int]:
        """
        Return height and width needed for rendering a game card
        @return height, width
        """
        return len(common.GAME_PAD), len(common.GAME_PAD[0])

    @staticmethod
    def get_control_string() -> str:
        """
        Returns the control-string with all available controls for the game card
        """
        return common.LABEL_CONTROL_DESCRIPTION_GAME_CARD

    def render(self, points: List[List[Point]]):
        """
        Render the passed List[List[Point]] to the window passed in the constructor
        @param points: List[List[Point]] which is rendered
        """
        self.__window.clear()

        max_y, max_x = self.__window.getmaxyx()
        x_off = (max_x - len(common.GAME_PAD[0])) // 2
        y_off = (max_y - len(common.GAME_PAD)) // 2

        # Print header pad
        players_card.draw_header(self.__window, y_off, x_off)

        # Print game pad
        line_count = 0
        for line in common.GAME_PAD:
            self.__window.addstr(line_count + y_off + len(common.NAME_PAD),
                                 x_off,
                                 line,
                                 curses.color_pair(common.COLOR_PAIR_BLACK_WHITE))
            line_count += 1

        iteration = 0 
        for column in points:
            y_off_column = y_off + len(common.NAME_PAD) + 1
            x_off_column = x_off + len(common.GAME_PAD[1]) + iteration * 6
            self.__window.move(y_off_column, x_off_column)
            self.__render_column(column)
            iteration += 1

        self.__window.refresh()

    def __render_column(self, column: List[Point]):
        """
        Draws column at the current curser-position on the window
        @param column: column which is rendered
        """
        y_off, x_off = self.__window.getyx()
        count: int = 0
        for line in common.POINTS_PAD:
            if count % 2 == 0:
                index = count // 2
                point = column[index]

                if self.__show_selected and point.selected:
                    self.__window.attron(curses.color_pair(common.COLOR_PAIR_BLACK_CYAN))
                else:
                    self.__window.attron(curses.color_pair(common.COLOR_PAIR_BLACK_WHITE))

                if point.value is None:
                    str_to_add = ""
                elif point.value == 0:
                    str_to_add = "-"
                else:
                    str_to_add = line.format(point.value)

                self.__window.addstr(y_off + count, x_off, str_to_add.center(5))
                self.__window.attroff(curses.color_pair(common.COLOR_PAIR_BLACK_WHITE))
                self.__window.attroff(curses.color_pair(common.COLOR_PAIR_BLACK_CYAN))
            else:
                str_to_add = line
                self.__window.addstr(y_off + count, x_off, str_to_add,
                                     curses.color_pair(common.COLOR_PAIR_BLACK_WHITE))

            count += 1
            self.__window.addstr("!", curses.color_pair(common.COLOR_PAIR_BLACK_WHITE))
            self.__window.refresh()

    def show_selected(self, show):
        """
        Changes the state of the renderer when show is set to True a selected
        combination will be rendered with the appropriate property
        @param show: True=Selected combinations are rendered with selection property,
         False selected combination are not rendered with selection property
        """
        self.__show_selected = show
