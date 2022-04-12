import curses
import start_pad
import test_dices
import player_card
from common_resources import *


def show_tui(std_scr):
    key = 0
    padding = 5

    std_scr.clear()
    std_scr.refresh()

    # Start colors in curses
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    while key != 27:
        std_scr.clear()
        curses.resize_term(45, 180)
        height, width = std_scr.getmaxyx()

        start_x_title = int((width // 2) - (TITLE_STR_LEN // 2))
        start_x_dices = int((width // 2) - (DICE_STR_LEN // 2))

        for i in range(TITLE_ARRAY_LEN):
            std_scr.addstr(i, start_x_title, title[i], curses.color_pair(1))

        if key == 265:
            player_card.show_player_cards(std_scr)
        elif key == 266:
            test_dices.show_dices(std_scr)
        elif key == 8:
            start_pad.show_pad(std_scr)
        else:
            start_pad.show_pad(std_scr)

        std_scr.addstr(height-1, 0, STATUS_BAR_STR, curses.color_pair(2))
        std_scr.addstr(height-1, len(STATUS_BAR_STR), " " * (width - len(STATUS_BAR_STR) - 1), curses.color_pair(2))

        std_scr.move(height - 1, width - 1)
        std_scr.refresh()

        key = std_scr.getch()


if __name__ == '__main__':
    curses.wrapper(show_tui)
