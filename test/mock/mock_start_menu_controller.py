# pylint: disable=protected-access
# pylint: disable=C


class MockStartMenuController:

    def __init__(self):
        self.handle_input_check = False
        self.step_animation_check = False

    def handle_input(self, ):
        self.handle_input_check = True

    def step_animation_check(self):
        self.step_animation_check = True
