from typing import List, Dict

from kniffel.data_objects.combinations import Combinations
from kniffel.data_objects.dice import Dice


class GameState:
    def __init__(self, dice: List[Dice], combinations: List[Dict[Combinations, int]] = None):
        self.combinations = combinations
        self.dice = dice
