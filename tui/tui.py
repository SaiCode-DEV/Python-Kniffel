import curses
import start_menu
import test_dices
from Card import Card
from common_resources import *
from Player import Player


def start(std_scr):
    key = 0

    std_scr.clear()
    std_scr.refresh()

    # Start colors in curses
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    player_1 = Player("kogrib")
    player_card_1 = Card(player_1)

    while True:
        std_scr.clear()
        curses.resize_term(40, 150)
        height, width = std_scr.getmaxyx()

        start_x_title = int((width // 2) - (TITLE_STR_LEN // 2))

        for i in range(TITLE_ARRAY_LEN):
            std_scr.addstr(i, start_x_title, TITLE[i], curses.color_pair(1))

        if key == ord('q'):
            break
        elif key == 265:
            player_card_1.show()
            test_dices.show_dices(std_scr)
        elif key == 8 or key == 0:
            start_menu.show(std_scr)

        std_scr.addstr(height-1, 0, STATUS_BAR_STR, curses.color_pair(2))
        std_scr.addstr(height-1, len(STATUS_BAR_STR), " " * (width - len(STATUS_BAR_STR) - 1), curses.color_pair(2))

        std_scr.move(height - 1, width - 1)
        std_scr.refresh()

        key = std_scr.getch()


def show_player_menu(std_scr, is_single: bool):
    while True:
        print("test")


if __name__ == '__main__':
    curses.wrapper(start)
