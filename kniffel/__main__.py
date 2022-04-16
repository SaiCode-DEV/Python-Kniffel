"""
Entry Point for Python-Kniffel
"""
import curses
from curses import wrapper

import common
from windows.window_manager import WindowManager


def main(std_scr: curses.window):
    std_scr.clear()
    std_scr.refresh()
    print("Starting Python-Kniffel")
    common.init_colors()

    window_manager = WindowManager(std_scr)
    window_manager.start_game()


if __name__ == "__main__":
    wrapper(main)
