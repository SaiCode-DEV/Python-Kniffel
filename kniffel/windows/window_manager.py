import curses

import common
import key_codes
from kniffel.windows.start_menu import StartMenu
from kniffel.windows.game_window.game_window import GameWindow
from kniffel.windows.logo import Logo


class WindowManager:
    def __init__(self, std_scr: curses.window):
        self.std_scr = std_scr
        self.__running = False
        curses.curs_set(0)  # hide cursor
        std_scr.keypad(True)  # to be able to compare input wit curses constants
        curses.cbreak()  # no input buffering
        curses.noecho()

        #self.logo = Logo()
        #self.start_menu = StartMenu()
        self.game_window = GameWindow(self.std_scr)
        self.game_window.render()

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
            self.game_window.handle_input(ch)

        curses.endwin()

    def stop_game(self):
        self.__running = False

    def show_game_window(self):
        self.std_scr.clear()
        self.logo.render()
        self.game_window.render()
        self.std_scr.refresh()

    def show_start_menu(self):
        self.std_scr.clear()
        self.logo.render()
        self.start_menu.render()
        self.std_scr.refresh()


if __name__=="__main__":
    pass
