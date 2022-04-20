# pylint: disable=C

from kniffel.windows.game_window.dice_window import *

from unittest import TestCase

ONE_DICE = ["---------", "!       !", "!   ¤   !", "!       !", "---------"]


class DiceWindowTest(TestCase):
    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.window: curses.window = None
        self.dice_window: DiceWindow = None
        self.std_scr = curses.initscr()
        curses.start_color()

        common.init_colors()
        curses.curs_set(0)  # hide cursor
        self.std_scr.keypad(True)  # to be able to compare input wit curses constants
        curses.cbreak()  # no input buffering
        curses.noecho()

        curses.resize_term(50, 100)
        self.std_scr.clear()
        self.std_scr.refresh()

    def setUp(self):
        max_y, max_x = DiceWindow.get_required_size()
        self.window = self.std_scr.subwin(max_y, max_x, 0, 0)
        self.dice_window = DiceWindow(self.window)

    def tearDown(self) -> None:
        del self.window

    def test_display(self):
        [max_y, max_x] = DiceWindow.get_required_size()
        dice = []
        for _ in range(5):
            die = Dice()
            die.value = 1
            dice.append(die)
        self.dice_window.render(dice)
        lines = []
        for y in range(max_y):
            chars = []
            for x in range(max_x):
                chars.append(chr(self.window.inch(y, x) & 0xFF))
            line = "".join(chars)
            if line.strip() == "":
                continue
            lines.append(line.strip())
        print(lines)
        self.assertEqual(ONE_DICE * 5, lines)

