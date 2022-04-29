# pylint: disable=C
from os import path

from kniffel.windows.game_window.result_card import *

from test.windows.window_test import WindowTest
from test.windows import game_window

EXPECTED_PATH = game_window.__file__.replace("__init__.py", "") + "game_window_outputs"

def get_players_zeros_combinations():
    players_combinations: List[List[Point]] = []
    for _ in range(common.PLAYER_COUNT):
        column = []
        for _ in range(common.COMBINATIONS_COUNT):
            point = Point()
            point.value = 0
            column.append(point)
        players_combinations.append(column)
    return players_combinations


class TestResultCard(WindowTest):
    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.result_card: ResultCard

    def setUp(self):
        super().setUp()
        self.result_card = ResultCard(self.window)

    def tearDown(self) -> None:
        del self.window

    def get_max_yx(self):
        y,x = ResultCard.get_required_size()
        return [y + 7,x]

    def test_empty_result_card(self):
        self.result_card.render(get_players_zeros_combinations())
        actual = self.get_screen_value()

        actual = "\n".join(actual).strip().split("\n")  # remove top and bottom whitespace

        with open(path.join(EXPECTED_PATH, "zeros_result_card.txt"), "r", encoding="utf-8") as expected:
            iteration = 0
            for line in expected:
                if len(actual) - 1 < iteration:
                    raise AssertionError("result card length of expected does not match actual")
                self.assertEqual(line.strip(), actual[iteration].strip(),
                                 f"zeros_result_card.txt line rendered incorrectly in line {iteration + 1}")
                iteration += 1
