# pylint: disable=C
# pylint: disable=protected-access


from unittest import TestCase

from kniffel import key_codes
from kniffel.game_logic.controller.start_menu_controller import StartMenuController
from test.mock.mock_start_window import MockStartWindow
from test.mock.mock_kniffel_controller import MockKniffelController


class TestStartMenuController(TestCase):

    def __init__(self, method_name="test"):
        super().__init__(method_name)
        self.start_controller = None
        self.kniffel_controller = None
        self.start_window = None

    def setUp(self) -> None:
        self.start_window = MockStartWindow()
        self.kniffel_controller = MockKniffelController()
        self.start_controller = StartMenuController(self.kniffel_controller, self.start_window)

    def test_handle_input_N(self):
        self.start_controller.handle_input(key_codes.VK_UC_N)
        self.assertTrue(self.kniffel_controller.start_classic_game_called,
                        "When N is pressed, new classic game should be started")

    def test_handle_input_n(self):
        self.start_controller.handle_input(key_codes.VK_LC_N)
        self.assertTrue(self.kniffel_controller.start_classic_game_called,
                        "When n is pressed, new classic game should be started")

    def test_handle_input_C(self):
        self.start_controller.handle_input(key_codes.VK_UC_C)
        self.assertTrue(self.kniffel_controller.continue_game_called,
                        "When C is pressed, game should be continued")

    def test_handle_input_c(self):
        self.start_controller.handle_input(key_codes.VK_LC_C)
        self.assertTrue(self.kniffel_controller.continue_game_called,
                        "When c is pressed, game should be continued")

    def test_handle_input_p(self):
        self.start_controller.handle_input(key_codes.VK_LC_P)
        self.assertTrue(self.kniffel_controller.start_bot_game_called,
                        "When p is pressed, new bot games should be started")

    def test_handle_input_P(self):
        self.start_controller.handle_input(key_codes.VK_UC_P)
        self.assertTrue(self.kniffel_controller.start_bot_game_called,
                        "When P is pressed, new bot game should be started")

    def test_handle_input_Q(self):
        self.start_controller.handle_input(key_codes.VK_UC_Q)
        self.assertTrue(self.kniffel_controller.exit_called,
                        "When Q is pressed, game should be quit")

    def test_handle_input_q(self):
        self.start_controller.handle_input(key_codes.VK_LC_Q)
        self.assertTrue(self.kniffel_controller.exit_called,
                        "When q is pressed,  game should be quit")

    def tearDown(self) -> None:
        del self.start_controller
        del self.kniffel_controller
