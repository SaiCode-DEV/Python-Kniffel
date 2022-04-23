"""
This module contains the needed functionality for rendering a same elements
into a window
The logic for a game-card is found in the card_controller_module
"""
import curses

import common


class PlayerCard:
    """
    Super-class for game and result card
    """
    @staticmethod
    def draw_header(window: curses.window, y_off: int, x_off: int):
        """
        Draw header for game and result cards
        @param window: screen in which will be drawn
        @param y_off: y coordinate
        @param x_off: x coordinate
        """
        count: int = 0
        for line in common.NAME_PAD:
            window.addstr(y_off + count, x_off, line,
                          curses.color_pair(common.COLOR_PAIR_BLACK_WHITE))
            count += 1
