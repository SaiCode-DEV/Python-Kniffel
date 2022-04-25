
class MockKniffelController:

    def __init__(self):
        self.start_classic_game_called = False
        self.start_bot_game_called = False
        self.continue_game_called = False
        self.exit_called = False

    def start_classic_game(self):
        self.start_classic_game_called = True


    def start_bot_game(self):
        self.start_bot_game_called = True


    def continue_game(self):
        self.continue_game_called = True


    def exit(self):
        self.exit_called = True

