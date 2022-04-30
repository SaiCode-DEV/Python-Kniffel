# pylint: disable=C
# pylint: disable=protected-access

from test.windows.window_test import WindowTest
from kniffel.windows.start_window import StartWindow
from test import windows
from os import path

EXPECTED_PATH = windows.__file__.replace("__init__.py", "") + "start_window"


class GameWindowTest(WindowTest):

    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.start_window: StartWindow = None

    def setUp(self):
        super().setUp()
        self.start_window = StartWindow(self.window)

    def get_max_yx(self):
        return StartWindow.get_required_size()

    def test_start_menu_render(self):
        self.start_window.render(None)
        actual = self.get_screen_value()
        actual = "\n".join(actual).strip().split("\n")  # remove top and bottom whitespace

        self.assert_input_equals_file(path.join(EXPECTED_PATH, "expected_start_menu.txt"), actual)
