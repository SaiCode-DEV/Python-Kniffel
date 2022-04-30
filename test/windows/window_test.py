"""
Module containing superclass for all tests with a curses window
"""
# pylint: disable=C
# pylint: disable=protected-access,R0801

import curses
import os
from unittest import TestCase

from kniffel import common


class WindowTest(TestCase):
    """
    Superclass for all tests with a curses window
    """

    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.window: curses.window = None
        self.std_scr = curses.initscr()
        curses.start_color()

        common.init_colors()
        curses.curs_set(0)  # hide cursor
        # to be able to compare input wit curses constants
        self.std_scr.keypad(True)
        curses.cbreak()  # no input buffering
        curses.noecho()

    def setUp(self):
        """
        runs before each test and initializes window
        """
        max_y, max_x = self.get_max_yx()
        curses.resize_term(10000, 10000)
        self.std_scr.clear()
        self.std_scr.refresh()
        curses.resize_term(max_y, max_x)
        self.window = self.std_scr.subwin(max_y, max_x, 0, 0)

    def tearDown(self):
        _ = self
        if os.name != 'nt':
            curses.endwin()

    def get_max_yx(self):
        """
        Method is ment to be overwritten by subclasses
        """
        _ = self
        return 100, 100

    def get_screen_value(self):
        """
        collects the currently displayed characters on the screen
        @return:
        """
        max_y, max_x = self.get_max_yx()
        lines = []
        for current_y in range(max_y):
            chars = []
            for current_x in range(max_x):
                chars.append(chr(self.window.inch(
                    current_y, current_x) & 0xFF))
            line = "".join(chars)
            lines.append(line)
        return lines

    def assert_input_equals_file(self, file, actual):
        with open(file, "r", encoding="utf-8") as expected:
            iteration = 0
            for line in expected:
                if len(actual) - 1 < iteration:
                    raise AssertionError(
                        "empty_points_ones_dice length of expected does not match actual")
                self.assertEqual(
                    line.strip(),
                    actual[iteration].strip(),
                    f"empty_points_ones_dice line rendered incorrectly in line {iteration + 1}")
                iteration += 1
