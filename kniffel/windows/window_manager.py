import curses

import common
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
        #self.game_window = GameWindow()

    def start_game(self):
        """
        Starts the main game loop in here inputs will get handled
        and to the subwindows distributed
        """
        gw = GameWindow(self.std_scr)
        gw.render()
        self.std_scr.getch()

        #self.__running = True
        #while self.__running:
        #    pass

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
