# pylint: disable=C
# pylint: disable=protected-access

from os import path

from kniffel.data_objects.game_state import GameState
from test import state_generator
from kniffel.windows.game_window.game_window import GameWindow

from test.windows.window_test import WindowTest
from test.windows import game_window

EXPECTED_PATH = game_window.__file__.replace("__init__.py", "") + "game_window_outputs"


class GameWindowTest(WindowTest):

    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.game_window: GameWindow = None

    def setUp(self):
        super().setUp()
        self.game_window = GameWindow(self.window)

    def tearDown(self) -> None:
        del self.window

    def get_max_yx(self):
        return GameWindow.get_required_size()

    def test_game_card_render(self):
        game_state = GameState()
        game_state.dice = state_generator.get_dice_with_value(1)
        game_state.points = state_generator.get_empty_combinations()
        self.game_window.show_game_card(game_state)
        actual = self.get_screen_value()

        actual = "\n".join(actual).strip().split("\n")  # remove top and bottom whitespace
        self.assert_input_equals_file(path.join(EXPECTED_PATH, "empty_points_ones_dice.txt"), actual)

    def test_result_card_render(self):
        game_state = GameState()
        game_state.dice = state_generator.get_dice_with_value(1)
        game_state.points = state_generator.get_empty_combinations()
        player = 0
        for column in game_state.points:
            combination = 0
            for _ in column:
                game_state.points[player][combination].value = player + combination
                combination += 1
            player += 1
        self.game_window.show_result_card(game_state)
        actual = self.get_screen_value()

        actual = "\n".join(actual).strip().split("\n")  # remove top and bottom whitespace

        with open(path.join(EXPECTED_PATH, "result_card_render.txt"), "r", encoding="utf-8") as expected:
            iteration = 0
            for line in expected:
                if len(actual) - 1 < iteration:
                    raise AssertionError("test_result_card_render length of expected does not match actual")
                self.assertEqual(line.strip(), actual[iteration].strip(), f"test_result_card_render line rendered incorrectly in line {iteration + 1}")
                iteration += 1

    def test_display_message(self):
        game_state = GameState()
        game_state.dice = state_generator.get_dice_with_value(2)
        game_state.points = state_generator.get_empty_combinations()
        self.game_window.display_message(game_state, "This is a test")
        self.game_window.display_controls(game_state, "This is another test")
        self.game_window.show_game_card(game_state)  # has to be present after re-render
        actual = self.get_screen_value()

        actual = "\n".join(actual).strip().split("\n")  # remove top and bottom whitespace

        with open(path.join(EXPECTED_PATH, "with_test_message.txt"), "r", encoding="utf-8") as expected:
            iteration = 0
            for line in expected:
                if len(actual) - 1 < iteration:
                    raise AssertionError("with_test_message length of expected does not match actual")
                self.assertEqual(line.strip(), actual[iteration].strip(), f"with_test_message line rendered incorrectly in line {iteration + 1}")
                iteration += 1
