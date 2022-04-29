"""
The point module contains the needed classes for storing the
current state of a point
"""

from json import JSONEncoder
from typing import Dict


class Point:
    """
    Class Point holds all relevant data of a point object
    """

    @staticmethod
    def from_json(data):
        """
        Marshals a Point object from dict
        """
        point = Point()
        if not isinstance(data, Dict):
            return point
        if "completed" in data:
            point.completed = data["completed"]
        if "value" in data:
            point.value = data["value"]
        return point

    def __init__(self):
        self.selected = False
        self.completed = False
        self.__value = None

    @property
    def value(self) -> int:
        """
        getter for value property (to shut up pylint)
        """
        return self.__value

    @value.setter
    def value(self, value: int):
        """
        setter for value property (to shut up pylint)
        """
        self.__value = value

    def __eq__(self, other) -> bool:
        """
        checks if two Point objects are equal
        """
        if not isinstance(other, Point):
            return False
        return self.completed == other.completed and self.value == other.value


class PointEncoder(JSONEncoder):
    """
    PointEncoder is used for encoding a game_state to json
    """

    def default(self, o):
        """
        used for decoding JSONEncoder to json
        """
        if not isinstance(o, Point):
            return None

        return {
            "selected": o.selected,
            "completed": o.completed,
            "value": o.value
        }
