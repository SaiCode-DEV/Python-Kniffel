# pylint: disable=C

import curses
from unittest import TestCase

from kniffel import common


class WindowTest(TestCase):
    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.window: curses.window = None
        self.std_scr = curses.initscr()
        curses.start_color()

        common.init_colors()
        curses.curs_set(0)  # hide cursor
        self.std_scr.keypad(True)  # to be able to compare input wit curses constants
        curses.cbreak()  # no input buffering
        curses.noecho()

        curses.resize_term(10000, 10000)
        max_y, max_x = self.get_max_yx()
        curses.resize_term(max_y, max_x)
        self.std_scr.clear()
        self.std_scr.refresh()

    def setUp(self):
        max_y, max_x = self.get_max_yx()
        self.window = self.std_scr.subwin(max_y, max_x, 0, 0)

    def get_max_yx(self):
        """
        Method is ment to be overwritten by subclasses
        """
        return 100, 100

    def get_screen_value(self):
        max_y, max_x = self.get_max_yx()
        lines = []
        for y in range(max_y):
            chars = []
            for x in range(max_x):
                chars.append(chr(self.window.inch(y, x) & 0xFF))
            line = "".join(chars)
            lines.append(line)
        return lines
