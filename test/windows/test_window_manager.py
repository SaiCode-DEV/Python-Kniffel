# pylint: disable=C
# pylint: disable=protected-access
from os import path

from kniffel.data_objects.game_state import GameState
from test.windows.window_test import WindowTest
from test import windows, state_generator
from kniffel.windows.window_manager import WindowManager, WindowToSmall, check_size
from kniffel.windows.game_window.game_window import GameWindow

EXPECTED_PATH = windows.__file__.replace("__init__.py", "") + "window_manager"


class WindowManagerTest(WindowTest):
    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.window_manager: WindowManager

    def setUp(self):
        super().setUp()
        self.window_manager = WindowManager(self.window, True)

    def get_max_yx(self):
        game_y, game_x = GameWindow.get_required_size()
        start_y, start_x = GameWindow.get_required_size()
        return max(game_y, start_y), max(game_x, start_x)

    def test_render_start(self):
        game_state = GameState()
        game_state.points = state_generator.get_empty_combinations()
        game_state.dice = state_generator.get_dice_with_value(1)
        self.window_manager.show_start_menu(game_state)
        self.assert_window_equals_file(
            path.join(
                EXPECTED_PATH,
                "start_window.txt"))

    def test_render_game(self):
        game_state = GameState()
        game_state.points = state_generator.get_empty_combinations()
        game_state.dice = state_generator.get_dice_with_value(1)
        self.window_manager.show_game_window(game_state)
        self.assert_window_equals_file(
            path.join(
                EXPECTED_PATH,
                "game_window.txt"))

    def test_size_check(self):
        max_y, max_x = self.get_max_yx()
        fail_fn = lambda: check_size(self.window, max_y + 1, max_x)
        self.assertRaises(WindowToSmall, fail_fn)
        fail_fn = lambda: check_size(self.window, max_y, max_x + 1)
        self.assertRaises(WindowToSmall, fail_fn)
