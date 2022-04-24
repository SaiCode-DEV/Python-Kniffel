# pylint: disable=C
from os import path
from kniffel.windows.game_window.dice_window import *

from test.windows.window_test import WindowTest
from test.windows import game_window

EXPECTED_PATH = game_window.__file__.replace("__init__.py", "") + "dice_outputs"


def get_all_dice(value):
    dice = []
    for _ in range(5):
        die = Dice()
        die.value = value
        dice.append(die)
    return dice

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
        self.dice_window.render(get_all_dice(1))
        actual = self.get_screen_value()

        actual = "\n".join(actual).strip().split("\n")  # remove top and bottom whitespace

        with open(path.join(EXPECTED_PATH, "all_ones.txt"), "r", encoding="utf-8") as expected:
            iteration = 0
            for line in expected:
                if len(actual) - 1 < iteration:
                    raise AssertionError("all_ones length of expected does not match actual")
                self.assertEqual(line.strip(), actual[iteration].strip(), f"empty_points_ones_dice line rendered incorrectly in line {iteration+1}")
                iteration += 1

    def test_all_twos(self):
        self.dice_window.render(get_all_dice(2))
        actual = self.get_screen_value()

        actual = "\n".join(actual).strip().split("\n")  # remove top and bottom whitespace

        with open(path.join(EXPECTED_PATH, "all_twos.txt"), "r", encoding="utf-8") as expected:
            iteration = 0
            for line in expected:
                if len(actual) - 1 < iteration:
                    raise AssertionError("all_ones length of expected does not match actual")
                self.assertEqual(line.strip(), actual[iteration].strip(), f"empty_points_ones_dice line rendered incorrectly in line {iteration+1}")
                iteration += 1

    def test_all_threes(self):
        self.dice_window.render(get_all_dice(3))
        actual = self.get_screen_value()

        actual = "\n".join(actual).strip().split("\n")  # remove top and bottom whitespace

        with open(path.join(EXPECTED_PATH, "all_threes.txt"), "r", encoding="utf-8") as expected:
            iteration = 0
            for line in expected:
                if len(actual) - 1 < iteration:
                    raise AssertionError("all_ones length of expected does not match actual")
                self.assertEqual(line.strip(), actual[iteration].strip(), f"empty_points_ones_dice line rendered incorrectly in line {iteration+1}")
                iteration += 1

    def test_all_fours(self):
        self.dice_window.render(get_all_dice(4))
        actual = self.get_screen_value()

        actual = "\n".join(actual).strip().split("\n")  # remove top and bottom whitespace

        with open(path.join(EXPECTED_PATH, "all_fours.txt"), "r", encoding="utf-8") as expected:
            iteration = 0
            for line in expected:
                if len(actual) - 1 < iteration:
                    raise AssertionError("all_ones length of expected does not match actual")
                self.assertEqual(line.strip(), actual[iteration].strip(), f"empty_points_ones_dice line rendered incorrectly in line {iteration+1}")
                iteration += 1

    def test_all_fives(self):
        self.dice_window.render(get_all_dice(5))
        actual = self.get_screen_value()

        actual = "\n".join(actual).strip().split("\n")  # remove top and bottom whitespace

        with open(path.join(EXPECTED_PATH, "all_fives.txt"), "r", encoding="utf-8") as expected:
            iteration = 0
            for line in expected:
                if len(actual) - 1 < iteration:
                    raise AssertionError("all_ones length of expected does not match actual")
                self.assertEqual(line.strip(), actual[iteration].strip(), f"empty_points_ones_dice line rendered incorrectly in line {iteration+1}")
                iteration += 1

    def test_all_sixes(self):
        self.dice_window.render(get_all_dice(6))
        actual = self.get_screen_value()

        actual = "\n".join(actual).strip().split("\n")  # remove top and bottom whitespace

        with open(path.join(EXPECTED_PATH, "all_sixes.txt"), "r", encoding="utf-8") as expected:
            iteration = 0
            for line in expected:
                if len(actual) - 1 < iteration:
                    raise AssertionError("all_ones length of expected does not match actual")
                self.assertEqual(line.strip(), actual[iteration].strip(), f"empty_points_ones_dice line rendered incorrectly in line {iteration+1}")
                iteration += 1
