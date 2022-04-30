"""
start_animations contains the Logic needed for the starting animation
"""

import curses
from typing import List

from kniffel import common


class StartAnimation:
    """
    StartAnimation controls the state of the StartAnimation
    """

    @staticmethod
    def get_required_size() -> List[int]:
        """
        Returns the minimum required y and x value to show the animation
        @return: min_y min_x
        """
        return [len(common.LOGO), len(common.LOGO[0])]

    def __init__(self, window: curses.window):
        self.step_count = 0
        self.window = window

    def render(self):
        """
        renders the animation in its current state on the screen
        """
        height, width = self.window.getmaxyx()

        start_x_title = int((width - len(common.LOGO[0])) // 2)
        start_y_title = int((height - len(common.LOGO)) // 2)

        self.window.clear()
        if self.step_count < len(common.LOADING):
            iteration = 0
            for line in common.LOADING[self.step_count]:
                self.window.addstr(
                    start_y_title + iteration,
                    start_x_title,
                    line,
                    curses.color_pair(
                        common.COLOR_PAIR_BLUE_BLACK))
                iteration += 1
        else:
            iteration = 0
            for line in common.LOGO:
                self.window.addstr(
                    start_y_title + iteration,
                    start_x_title,
                    line.rstrip(),
                    curses.color_pair(
                        common.COLOR_PAIR_BLUE_BLACK))
                iteration += 1
        self.window.refresh()

    def step_animation(self):
        """
        Switches to the next animation-state
        if done the animation will hold its position for 5 calls
        then return to the start of the animation
        """
        self.step_count += 1
        if self.step_count > len(common.LOADING) + 5:
            self.step_count = 0
