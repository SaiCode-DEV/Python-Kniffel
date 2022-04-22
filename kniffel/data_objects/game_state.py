"""
The game_state module contains all classes for holding and storing a games current state
"""
from typing import List, Dict

from data_objects.point import Point
from kniffel.data_objects.dice import Dice


class GameState:
    """
    The GameState class is supposed to be the main container class for a games state,
    it should withold all information to restore a canceled game
    """

    def __init__(self, dice: List[Dice], points: List[List[Point]]):
        self.__points = points
        self.__dice = dice

    @property
    def points(self) -> List[List[Point]]:
        """
        A getter for the combinations within a GameState
        """
        return self.__points

    @property
    def dice(self) -> List[Dice]:
        """
        A getter for the dice within a GameState
        """
        return self.__dice
