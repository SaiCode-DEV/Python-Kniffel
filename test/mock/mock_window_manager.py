# pylint: disable = protected-access
# pylint: disable=C
from test.mock.mock_game_window import MockGameWindow

from test.mock.mock_start_window import MockStartWindow


class MockWindowManager:

    def __init__(self):
        self.check_render = False
        self.check_show_start_menu = False
        self.game_window = MockGameWindow()
        self.start_window = MockStartWindow()
        self.game_state = None
        self.get_chr_called = False
        self.delay = None

    def render(self, game_state):
        self.game_state = game_state
        self.check_render = True

    def show_start_menu(self, game_state):
        self.game_state = game_state
        self.check_show_start_menu = True

    def show_game_menu(self):
        self.check_show_start_menu = True

    def set_no_input_delay(self, delay):
        self.delay = delay

    def get_ch(self):
        pass

    def show_game_window(self, game_state):
        self.game_state = game_state
