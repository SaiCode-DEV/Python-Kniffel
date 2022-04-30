# pylint: disable=C
# pylint: disable=protected-access

from unittest import TestCase
from kniffel import key_codes
from kniffel.game_logic.controller.kniffel_controller import KniffelController, EnumWindowSelected

from test.mock.mock_window_manager import MockWindowManager


class TestKniffelController(TestCase):
    def __init__(self, method_name="test"):
        super().__init__(method_name)
        self.window_manager = None
        self.game_controller = None
        self.exit_called = False

    def setUp(self) -> None:
        self.window_manager = MockWindowManager()
        self.kniffel_controller = KniffelController(self.window_manager)

    def test_handle_input_n(self):
        self.kniffel_controller.show_start_menu()
        self.kniffel_controller.handle_input(key_codes.VK_LC_N)
        self.assertEqual(
            EnumWindowSelected.GAME_WINDOW.value,
            self.kniffel_controller.active_window.value,
            "New Game should be started.")

    def test_handle_input_C(self):
        self.kniffel_controller.show_start_menu()
        self.kniffel_controller.handle_input(key_codes.VK_LC_C)
        self.assertEqual(
            EnumWindowSelected.GAME_WINDOW.value,
            self.kniffel_controller.active_window.value,
            "Game should be continued.")

    def test_handle_input_p(self):
        self.kniffel_controller.show_start_menu()
        self.kniffel_controller.handle_input(key_codes.VK_LC_P)
        self.assertEqual(
            EnumWindowSelected.GAME_WINDOW.value,
            self.kniffel_controller.active_window.value,
            "Bot Game should be started.")

    def test_handle_input_q(self):
        self.kniffel_controller.start_classic_game()
        self.kniffel_controller.handle_input(key_codes.VK_LC_Q)
        self.assertEqual(
            EnumWindowSelected.START_MENU.value,
            self.kniffel_controller.active_window.value,
            "Game should be quit.")

    def test_start(self):
        self.kniffel_controller.start(True)
        self.assertTrue(self.window_manager.start_window.step_animation_called,
                        "Animation should be executed")

    def tearDown(self):
        del self.window_manager
        del self.game_controller
