# pylint: disable=C

from kniffel.windows.game_turn import *

from unittest import TestCase

ONE_DICE = ["##########", "#       #", "#   ¤   #", "#       #", "##########"]


class DiceTest(TestCase):
    def test_display(self):
        curses.initscr()
        curses.start_color()
        common.init_colors()
        [max_y, max_x] = get_required_size()
        curses.resize_term(max_y, max_x)
        window = curses.newwin(max_y, max_x, 0, 0)
        tm = TurnManager(window)
        tm.set_dice([1, 1, 1, 1, 1])
        tm.handle_input('d')
        lines = []
        for y in range(max_y):
            chars = []
            for x in range(max_x):
                chars.append(chr(window.inch(y, x) & 0xFF))
            line = "".join(chars)
            if line.strip() == "":
                continue
            lines.append(line.strip())
        curses.endwin()
        self.assertEqual(ONE_DICE * 5, lines)
