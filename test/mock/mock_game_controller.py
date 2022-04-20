from kniffel.data_objects.combinations import Combinations


class MockGameController:

    def __init__(self):
        self.combination = None
        self.game_state = None
        self.message = None
        self.character = None

    def handle_input(self, character: chr):
        self.character = character

    def display_message(self, message: str):
        self.message = message

    def get_game_state(self):
        return self.game_state

    def add_entry(self, combination: Combinations):
        self.combination = combination

    def reset_game(self):
        pass
