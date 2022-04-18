import curses

from data_objects.game_state import GameState
from kniffel.windows.start_menu import StartWindow
from kniffel.windows.game_window.game_window import GameWindow


def resize_term():
    game_y, game_x = GameWindow.get_required_size()
    start_y, start_x = StartWindow.get_required_size()
    wind_x = max(game_x, start_x)
    wind_y = max(game_y, start_y)
    curses.resize_term(wind_y, wind_x)


class WindowManager:
    def __init__(self, std_scr: curses.window):
        self.std_scr = std_scr
        self.__running = False
        curses.curs_set(0)  # hide cursor
        std_scr.keypad(True)  # to be able to compare input wit curses constants
        curses.cbreak()  # no input buffering
        curses.noecho()
        resize_term()

        self.__start_window = StartWindow(self.std_scr)
        self.__game_window = GameWindow(self.std_scr)
        self.active_window = None

    @property
    def start_window(self):
        return self.__start_window

    @property
    def game_window(self):
        return self.__game_window

    def stop_game(self):
        self.__running = False

    def show_game_window(self, game_state: GameState):
        self.active_window = self.__game_window
        self.render(game_state)

    def show_start_menu(self, game_state: GameState):
        self.active_window = self.__start_window
        self.render(game_state)

    def render(self, game_state: GameState):
        self.std_scr.clear()
        self.std_scr.refresh()
        if self.active_window is not None:
            self.active_window.render(game_state)

    def get_ch(self) -> chr:
        return self.std_scr.getch()

    @staticmethod
    def close():
        curses.endwin()
