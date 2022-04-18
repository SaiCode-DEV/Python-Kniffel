"""
Entry Point for Python-Kniffel
"""
import curses
from curses import wrapper

import common
from kniffel.game_logic.controller.kniffel_controller import KniffelController
from windows.window_manager import WindowManager, WindowToSmall


def main(std_scr: curses.window):
    print("Starting Python-Kniffel")
    common.init_colors()

    window_manager = None
    try:
        window_manager = WindowManager(std_scr)
    except WindowToSmall:
        print("Sadly your Window is to small and cannot be resized, "
              "pleas do so yourself, and then restart the program")
        exit(1)
    game_manager = KniffelController(window_manager)
    game_manager.start()


if __name__ == "__main__":
    wrapper(main)
