from plistlib import Dict
from combinations import Combinations


class GameState:
    def __init__(self, state_one: Dict[Combinations, int] = None, state_two: Dict[Combinations, int] = None):
        if state_one is None:
            self.state_one = {}
        else:
            self.state_one = state_one
        if state_two is None:
            self.state_two = {}
        else:
            self.state_two = state_two
