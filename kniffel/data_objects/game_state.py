"""
The game_state module contains all classes for holding and storing a games current state
"""
import json
from json import JSONEncoder, JSONDecoder
from typing import List, Dict

from kniffel.data_objects.point import Point, PointEncoder
from kniffel.data_objects.dice import Dice, DiceEncoder


class GameState:
    """
    The GameState class is supposed to be the main container class for a games state,
    it should withold all information to restore a canceled game
    """

    @staticmethod
    def from_json(data):
        game_state = GameState()
        if not isinstance(data, Dict):
            return game_state
        if "active_player" in data:
            game_state.active_player = data["active_player"]
        if "roll_count" in data:
            game_state.roll_count = data["roll_count"]
        if "dice" in data:
            dice = []
            for die in data["dice"]:
                dice.append(Dice.from_json(die))
            game_state.dice = dice
        if "points" in data:
            points_decoded = []
            for column_encoded in data["points"]:
                column_decoded = []
                for point in column_encoded:
                    column_decoded.append(Point.from_json(point))
                points_decoded.append(column_decoded)
            game_state.points = points_decoded
        return game_state

    def __init__(self, dice: List[Dice] = None, points: List[List[Point]] = None, active_player: int = 0, roll_count: int = 0):
        self.active_player = active_player
        self.roll_count = roll_count
        self.__points = points
        self.__dice = dice

    @property
    def points(self) -> List[List[Point]]:
        """
        A getter for the combinations within a GameState
        """
        return self.__points

    @points.setter
    def points(self, value: List[List[Point]]):
        self.__points = value

    @property
    def dice(self) -> List[Dice]:
        """
        A getter for the dice within a GameState
        """
        return self.__dice

    @dice.setter
    def dice(self, value: List[Dice]):
        self.__dice = value


class GameStateEncoder(JSONEncoder):
    """
    GameStateEncoder is used for encoding a game_state to json
    """

    def default(self, o):
        """
        used for decoding GameState to json
        """
        if not isinstance(o, GameState):
            return None

        points = []
        for column in o.points:
            col = []
            for p in column:
                col.append(PointEncoder().default(p))
            points.append(col)
        dice = []
        for die in o.dice:
            dice.append(DiceEncoder().default(die))

        return {
            "active_player": o.active_player,
            "roll_count": o.roll_count,
            "points": points,
            "dice": dice
        }
