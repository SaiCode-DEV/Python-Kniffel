# pylint: disable=C
from os import path
from kniffel.windows.game_window.dice_window import *

from test.windows.window_test import WindowTest
from test.windows import game_window

EXPECTED_PATH = game_window.__file__.replace("__init__.py", "") + "dice_outputs"


class DiceWindowTest(WindowTest):

    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.dice_window: DiceWindow = None

    def setUp(self):
        super().setUp()
        self.dice_window = DiceWindow(self.window)

    def tearDown(self) -> None:
        del self.window

    def get_max_yx(self):
        return DiceWindow.get_required_size()

    def test_all_ones(self):
        dice = []
        for _ in range(5):
            die = Dice()
            die.value = 1
            dice.append(die)
        self.dice_window.render(dice)
        actual = self.get_screen_value()

        actual = "\n".join(actual).strip().split("\n")  # remove top and bottom whitespace

        with open(path.join(EXPECTED_PATH, "all_ones.txt"), "r", encoding="utf-8") as expected:
            iteration = 0
            for line in expected:
                if len(actual) - 1 < iteration:
                    raise AssertionError("all_ones length of expected does not match actual")
                self.assertEqual(line.strip(), actual[iteration].strip(), "all ones rendered incorrectly")
                iteration += 1

    def test_all_twos(self):
        dice = []
        for _ in range(5):
            die = Dice()
            die.value = 2
            dice.append(die)
        self.dice_window.render(dice)
        actual = self.get_screen_value()

        actual = "\n".join(actual).strip().split("\n")  # remove top and bottom whitespace

        with open(path.join(EXPECTED_PATH, "all_twos.txt"), "r", encoding="utf-8") as expected:
            iteration = 0
            for line in expected:
                if len(actual) - 1 < iteration:
                    raise AssertionError("all_ones length of expected does not match actual")
                self.assertEqual(line.strip(), actual[iteration].strip(), "all ones rendered incorrectly")
                iteration += 1
