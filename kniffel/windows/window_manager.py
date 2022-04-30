"""
The window_manager module contains the functionality for managing sub windows such
as the game_window and start_window
"""
import curses

from kniffel.data_objects.game_state import GameState
from kniffel.windows.start_window import StartWindow
from kniffel.windows.game_window.game_window import GameWindow


class WindowToSmall(Exception):
    """
    Is thrown when the Window is to small and can not be extended to the appropriate size
    """


def resize_term(std_scr: curses.window):
    """
    Tries to resize the Terminal to the required size if it fails to do so and the window
    is smaller than the required size the WindowToSmall Exception is raised
    @param std_scr: curses.window which needs to have the required size
    @raise WindowToSmall if window does not have required size and cannot be resized
    """
    game_y, game_x = GameWindow.get_required_size()
    start_y, start_x = StartWindow.get_required_size()
    wind_x = max(game_x, start_x)
    wind_y = max(game_y, start_y)
    curses.resize_term(10000, 10000)
    curses.resize_term(wind_y, wind_x)
    try:
        std_scr.addstr(wind_y - 1, wind_x - 2, "x")
    except Exception as write_error:
        raise WindowToSmall("Pleas resize your Window") from write_error


class WindowManager:
    """
    The WindowManager is supposed to be used for managing whole pages.
    """

    def __init__(self, std_scr: curses.window, test: bool):
        self.std_scr = std_scr
        curses.curs_set(0)  # hide cursor
        std_scr.keypad(True)  # to be able to compare input wit curses constants
        curses.cbreak()  # no input buffering
        curses.noecho()
        if not test:
            resize_term(std_scr)

        self.__start_window = StartWindow(self.std_scr)
        self.__game_window = GameWindow(self.std_scr)
        self.active_window = None

    @property
    def start_window(self) -> StartWindow:
        """
        @return: StartWindow used by the WindowManager
        """
        return self.__start_window

    @property
    def game_window(self) -> GameWindow:
        """
        @return: GameWindow used by the WindowManager
        """
        return self.__game_window

    def show_game_window(self, game_state: GameState):
        """
        Switches the show the game window and renders it onto the screen
        @param game_state: the current state of the game
        """
        self.active_window = self.__game_window
        self.render(game_state)

    def show_start_menu(self, game_state: GameState):
        """
        Switches the show the start menu and renders it onto the screen
        @param game_state: the current state of the game
        """
        self.active_window = self.__start_window
        self.render(game_state)

    def render(self, game_state: GameState):
        """
        renders the currently active window to the screen
        @param game_state: GameState, the current state of the game
        """
        if self.active_window is not None:
            self.active_window.render(game_state)

    def get_ch(self) -> chr:
        """
        Blocks until the user has entered an input which will
        then be returned
        """
        return self.std_scr.getch()

    def set_no_input_delay(self, delay: bool):
        """
        If flag is True, get_ch() will be non-blocking.
        @return:
        """
        self.std_scr.nodelay(delay)

    @staticmethod
    def close():
        """
        Closes the curses window
        """
        curses.endwin()
