import curses
from enum import Enum

import key_codes
from kniffel.windows.start_menu import StartMenu
from kniffel.windows.game_window.game_window import GameWindow


class EnumSelected(Enum):
    START_MENU = 1
    GAME_WINDOW = 2


def resize_term():
    game_y, game_x = GameWindow.get_required_size()
    start_y, start_x = StartMenu.get_required_size()
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

        self.start_menu = StartMenu(self.std_scr)
        self.game_window = GameWindow(self.std_scr)

        self.selected = EnumSelected.GAME_WINDOW
        self.render()

    def start_game(self):
        """
        Starts the main game loop in here inputs will get handled
        and to the subwindows distributed
        """

        self.__running = True
        while self.__running:
            ch = self.std_scr.getch()
            if ch == key_codes.VK_LC_Q or ch == key_codes.VK_UC_Q:
                self.__running = False
            if self.selected is EnumSelected.START_MENU:
                pass
            elif self.selected is EnumSelected.GAME_WINDOW:
                self.game_window.handle_input(ch)

        curses.endwin()

    def stop_game(self):
        self.__running = False

    def show_game_window(self):
        self.selected = EnumSelected.GAME_WINDOW
        self.render()

    def show_start_menu(self):
        self.selected = EnumSelected.START_MENU
        self.render()

    def render(self):

        self.std_scr.clear()
        self.std_scr.refresh()
        if self.selected is EnumSelected.START_MENU:
            self.start_menu.render()
        elif self.selected is EnumSelected.GAME_WINDOW:
            self.game_window.render()
