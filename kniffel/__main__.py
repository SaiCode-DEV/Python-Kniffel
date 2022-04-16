"""
Entry Point for Python-Kniffel
"""
import curses
from curses import wrapper

import common
from windows import game_turn
import key_codes


def main(std_scr):
    print("Starting Python-Kniffel")
    common.init_colors()
    curses.curs_set(0)  # hide cursor
    std_scr.keypad(True)  # to be able to compare input wit curses constants
    curses.cbreak()  # no input buffering
    curses.noecho()
    max_y, max_x = std_scr.getmaxyx()
    window = curses.newwin(max_y - 1, max_x - 1, 0, 0)
    tm = game_turn.TurnManager(window)
    while True:
        ch = std_scr.getch()
        if ch == key_codes.VK_UC_Q or ch == key_codes.VK_LC_Q:
            curses.endwin()
            return
        tm.handle_input(ch)
        std_scr.refresh()


if __name__ == "__main__":
    wrapper(main)
