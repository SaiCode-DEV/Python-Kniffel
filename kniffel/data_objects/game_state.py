from typing import List, Dict

from data_objects.point import Point
from kniffel.data_objects.dice import Dice


class GameState:
    def __init__(self, dice: List[Dice], points: List[Point]):
        self.points = points
        self.dice = dice
