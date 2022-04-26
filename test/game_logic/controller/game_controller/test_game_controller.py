# pylint disable=C
from unittest import TestCase

from kniffel import key_codes
from kniffel.game_logic.controller.game_controller.game_controller import *
from test.mock.mock_game_window import MockGameWindow
from test.mock.mock_kniffel_controller import MockKniffelController


class GameControllerTest(TestCase):

    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.game_controller: GameController = None
        common.ANIMATION_DELAY_ROLL = 0

    def setUp(self):
        self.mock_kniffel_controller = MockKniffelController()
        self.mock_game_window = MockGameWindow()
        self.game_controller = GameController(self.mock_kniffel_controller, self.mock_game_window)

    def test_quit(self):
        self.game_controller.handle_input(key_codes.VK_LC_Q)
        self.assertTrue(self.mock_kniffel_controller.show_start_menu_called, "Exit should have been called")

        self.game_controller.handle_input(key_codes.VK_UC_Q)
        self.assertTrue(self.mock_kniffel_controller.show_start_menu_called, "Exit should have been called")

    def test_input_dice_forward(self):
        self.game_controller.select_dice_window()
        dice_changed = False
        dice = [d.value for d in self.game_controller.get_game_state().dice]
        for _ in range(10):
            self.game_controller.handle_input(key_codes.VK_SPACE)
            dice_rolled = [d.value for d in self.game_controller.get_game_state().dice]
            self.assertEqual(len(dice), len(dice_rolled), "Dice count should not vary during roll")
            if len(set(dice).intersection(dice_rolled)) != len(dice_rolled):
                dice_changed = True
                break
        self.assertTrue(dice_changed, "dice did not roll either because of error in dice controller or input not forwarded to dice controller")

