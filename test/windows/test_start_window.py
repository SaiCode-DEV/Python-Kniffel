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
        with open(path.join(EXPECTED_PATH, "expected_start_menu.txt"), "r", encoding="utf-8") as expected:
            iteration = 0
            for line in expected:
                if len(actual) - 1 < iteration:
                    raise AssertionError("empty_points_ones_dice length of expected does not match actual")
                self.assertEqual(line.strip(), actual[iteration].strip(), f"empty_points_ones_dice line rendered incorrectly in line {iteration + 1}")
                iteration += 1
