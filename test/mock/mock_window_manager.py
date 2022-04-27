# pylint: disable = protected-access
# pylint: disable=C


class MockWindowManager:

    def __init__(self, method_name="test"):
        super().__init__(method_name)
        self.check_render = False
        self.check_game_window = False
        self.check_show_start_menu = False
        self.check_show_start_window = False
        self.check_no_input_delay = False

    def render(self):
        self.check_render = True

    def game_window(self):
        self.check_game_window = True

    def show_start_menu(self):
        self.check_show_start_menu = True

    def start_window(self):
        self.check_show_start_window = True

    def set_no_input_delay(self):
        self.check_no_input_delay = True
