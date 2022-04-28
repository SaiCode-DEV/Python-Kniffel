# pylint disable=C
from copy import deepcopy
from unittest import TestCase

from kniffel import key_codes
from kniffel.game_logic.controller.game_controller.game_controller import *
from test import state_generator
from test.game_logic.controller import game_controller
from test.mock.mock_game_window import MockGameWindow
from test.mock.mock_kniffel_controller import MockKniffelController


class GameControllerTest(TestCase):

    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.game_controller: GameController = None
        common.ANIMATION_DELAY_ROLL = 0

    def setUp(self):
        common.ANIMATION_DELAY_ROLL = 0
        common.BOT_DECISION_DELAY = 0
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

    def test_saving_and_loading_state(self):
        common.DIR_PERSISTENCE = game_controller.__file__.replace("__init__.py", "") + "json-temp"
        common.FILE_GAME_STATE = path.join(common.DIR_PERSISTENCE, "game_state.json")

        game_state: GameState = GameState()
        game_state.points = state_generator.get_random_combinations()
        game_state.dice = state_generator.get_dice_with_value(2)
        game_state.dice[1].selected = True
        game_state.active_player = 1
        game_state.game_kind = EnumGameKind.GAME_AGAINST_BOT

        self.game_controller.combinations = deepcopy(game_state.points)
        self.game_controller.dice_controller.set_dice(game_state.dice)
        GameController.game_kind = game_state.game_kind
        self.game_controller.active_player = game_state.active_player
        self.game_controller.save_to_file()
        self.game_controller.start_new_game(EnumGameKind.GAME_AGAINST_HUMAN)

        for i in range(common.PLAYER_COUNT):
            values_expected = [p.value for p in state_generator.get_empty_combinations()[i]]
            values_actual = [p.value for p in self.game_controller.combinations[i]]
            self.assertListEqual(values_expected, values_actual,
                                 "Game-Controller did not reset game-state after new game started")

        equal_dice = set([d.value for d in game_state.dice]).intersection(self.game_controller.dice_controller.get_dice_values())
        self.assertNotEqual(5, equal_dice, "game controller should have re-rolled dice after game start")
        self.assertEqual(0, self.game_controller.active_player, "game controller should have reset active player")

        self.game_controller.load_from_file()

        self.assertEqual(game_state, self.game_controller.get_game_state(), "Game-Controller did not load game-state correctly")

    def test_entry(self):
        dice = state_generator.get_dice_with_value(2)
        self.game_controller.dice_controller.set_dice(dice)
        self.game_controller.select_card_window()

        self.game_controller.card_controller.set_selected_player(0)
        self.game_controller.card_controller.set_selected_combination(Combinations.TWOS.value)
        self.game_controller.card_controller.handle_input(key_codes.VK_NUMPAD_ENTER)

        self.assertEqual(10, self.game_controller.get_game_state().points[0][Combinations.TWOS.value].value,
                         "should have added entry to twos with value 10")

    def test_bot_running(self):
        self.game_controller.start_new_game(EnumGameKind.GAME_AGAINST_BOT)
        self.game_controller.select_card_window()
        self.game_controller.handle_input(key_codes.VK_NUMPAD_ENTER)
        game_state = self.game_controller.get_game_state()
        bot_played = False
        for point in game_state.points[1]:
            if point.value is not None:
                bot_played = True
        self.assertTrue(bot_played, "bot should have made a turn")

    def test_available_bot_options(self):
        combos = state_generator.get_empty_combinations()
        combos[1][0].value = 1
        combos[1][2].value = 2
        self.game_controller.combinations = combos

        available = self.game_controller._get_available_options_for_bot()
        self.assertListEqual([1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [a.value for a in available], "the available options were wrongly prepared for bot")
