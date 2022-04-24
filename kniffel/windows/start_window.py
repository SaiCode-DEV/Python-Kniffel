"""
The start_window module contains the logic for rendering the start window
"""
import curses
from typing import Tuple

from kniffel.data_objects.game_state import GameState
from kniffel import common
from kniffel.windows.animations.start_animation import StartAnimation

OPTIONS = [
    common.LABEL_MANU_CONTINUE,
    common.LABEL_MANU_PLAY,
    common.LABEL_MENU_PLAY_BOT,
    common.LABEL_MENU_ESCAPE
]


def get_screens(window: curses.window) -> Tuple[curses.window, curses.window]:
    """
    Creates the subwindows from passed window
    @param window: window which contains the subwindows
    @return: logo_window, start_menu_window
    """
    max_y, max_x = window.getmaxyx()
    [logo_min_y, _] = StartAnimation.get_required_size()
    logo_y = int(max_y * (logo_min_y / (logo_min_y + len(OPTIONS) * 2)))
    options_y = max_y - logo_y
    return window.subwin(logo_y, max_x, 0, 0), window.subwin(options_y, max_x, logo_y, 0)


class StartWindow:
    """
    The StartWindow class is used to render the Start Menu to the screen
    """

    @staticmethod
    def get_required_size() -> Tuple[int, int]:
        """
        Returns the minimally required size of the window to render this component
        @return: Tuple[int, int] min_y, min_x
        """
        [logo_y, logo_x] = StartAnimation.get_required_size()
        max_x = logo_x
        for opt in OPTIONS:
            if len(opt) > max_x:
                max_x = len(opt)
        return logo_y + len(OPTIONS) * 2, max_x

    def __init__(self, std_scr: curses.window):
        logo_win, self.window = get_screens(std_scr)
        self.__animation = StartAnimation(logo_win)
        self.max_x = len(OPTIONS[0])
        for opt in OPTIONS:
            if len(opt) > self.max_x:
                self.max_x = len(opt)

    def render(self, game_state: GameState = None):
        """
        Renders the start menu to the screen
        @param game_state: current state of the game
        """
        _ = game_state
        self.window.clear()
        self.window.refresh()
        height, width = self.window.getmaxyx()

        iteration = 0
        start_x = (width - self.max_x) // 2
        for line in OPTIONS:
            start_y = int((height // 2) - 2) + iteration * 2
            self.window.addstr(start_y, start_x, line)
            iteration += 1
            self.window.refresh()
        self.__animation.render()

    def step_animation(self):
        """
        Steps the currently displayed animation one step forward
        """
        self.__animation.step_animation()
