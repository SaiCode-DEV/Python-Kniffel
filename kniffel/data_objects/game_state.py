"""
The game_state module contains all classes for holding and storing a games current state
"""
from typing import List, Dict

from kniffel.data_objects.combinations import Combinations
from kniffel.data_objects.dice import Dice


class GameState:
    """
    The GameState class is supposed to be the main container class for a games state,
    it should withold all information to restore a canceled game
    """

    def __init__(self, dice: List[Dice], combinations: List[Dict[Combinations, int]]):
        self.__combinations = combinations
        self.__dice = dice

    @property
    def combinations(self) -> List[Dict[Combinations, int]]:
        """
        A getter for the combinations within a GameState
        """
        return self.__combinations

    @property
    def dice(self) -> List[Dice]:
        """
        A getter for the dice within a GameState
        """
        return self.__dice
