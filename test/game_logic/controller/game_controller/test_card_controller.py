# pylint: disable=C
# pylint: disable=protected-access
import curses

from kniffel.game_logic.controller.game_controller.card_controller import CardController

from unittest import TestCase

from test.mock.mock_game_card import MockGameCard
from test.mock.mock_result_card import MockResultCard
from test.mock.mock_game_controller import MockGameController


class GameCardControllerTest(TestCase):
    def setUp(self):
        self.mock_game_card = MockGameCard()
        self.mock_result_card = MockResultCard()
        self.mock_game_controller = MockGameController()
        self.card_controller = CardController(self.mock_game_card,
                                              self.mock_result_card,
                                              self.mock_game_controller)

    def test_handle_key_down(self):
        self.card_controller.handle_input(curses.KEY_DOWN)
        self.assertEqual(1, self.card_controller.selected_combination)

    def test_handel_key_up(self):
        self.card_controller.handle_input(curses.KEY_UP)
        self.assertEqual(12, self.card_controller.selected_combination)

    def test_handel_enter(self):
        player_combination = self.mock_game_controller.combinations[0]
        self.card_controller.handle_input(curses.KEY_ENTER)
        self.assertIsNotNone(player_combination[0].value)
