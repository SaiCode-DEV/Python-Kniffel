"""
Entry Point for Python-Kniffel
"""
import sys
import curses
from curses import wrapper

from kniffel import common
from kniffel.game_logic.controller.kniffel_controller import KniffelController
from kniffel.windows.window_manager import WindowManager, WindowToSmall


def main(std_scr: curses.window):
    """
    main represents the main entrypoint for the kniffel-program
    @param std_scr: main window
    """
    print("Starting Python-Kniffel")
    common.init_colors()

    try:
        window_manager = WindowManager(std_scr)
    except WindowToSmall:
        print("Sadly your Window is to small and cannot be resized, "
              "pleas do so yourself, and then restart the program")
        sys.exit(1)
    game_manager = KniffelController(window_manager)
    game_manager.start(False)

if __name__ == "__main__":
    wrapper(main)
