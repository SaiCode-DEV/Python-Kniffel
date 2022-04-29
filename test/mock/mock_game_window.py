# pylint disable=C
from kniffel.data_objects.game_state import GameState
from test.mock.mock_dice_window import MockDiceWindow
from test.mock.mock_game_card import MockGameCard
from test.mock.mock_result_card import MockResultCard


class MockGameWindow:
    def __init__(self):
        self.game_state = None
        self.message = None
        self.control_str = None

        self.show_result_card_called = False
        self.show_game_card_called = False

        self.dice_window = MockDiceWindow()
        self.game_card = MockGameCard()
        self.result_card = MockResultCard()

    def show_result_card(self, game_state: GameState):
        self.game_state = game_state
        self.show_result_card_called = True

    def show_game_card(self, game_state: GameState):
        self.game_state = game_state
        self.show_game_card_called = True

    def render(self, game_state: GameState):
        self.game_state = game_state

    def display_message(self, game_state: GameState, message: str):
        self.message = message
        self.game_state = game_state

    def display_controls(self, game_state: GameState, control_str):
        self.control_str = control_str
        self.game_state = game_state
