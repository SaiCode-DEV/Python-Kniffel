"""
Entry Point for Python-Kniffel
"""
import curses
from curses import wrapper

import common
from kniffel.game_logic.controller.kniffel_controller import KniffelController
from windows.window_manager import WindowManager


def main(std_scr: curses.window):
    print("Starting Python-Kniffel")
    common.init_colors()

    window_manager = WindowManager(std_scr)
    game_manager = KniffelController(window_manager)
    game_manager.start()


if __name__ == "__main__":
    wrapper(main)
