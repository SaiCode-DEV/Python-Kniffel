# pylint: disable = protected-access
# pylint: disable=C

from test.mock.mock_game_window import *

from test.mock.mock_start_window import *


class MockWindowManager:

    def __init__(self):
        self.check_render = False
        self.check_show_start_menu = False
        self.check_no_input_delay = False
        self.game_window = MockGameWindow()
        self.start_window = MockStartWindow()
        self.game_state = None
        self.get_chr_called = False

    def render(self, game_state):
        self.check_render = True

    def show_start_menu(self, game_state:GameState):
        self.check_show_start_menu = True

    def show_game_menu(self):
        self.check_show_start_menu = True

    def set_no_input_delay(self, delay):
        self.check_no_input_delay = True

    def get_ch(self):
        self.get_char_called = True

    def show_game_window(self, game_state):
        return

