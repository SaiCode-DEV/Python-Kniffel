from json import JSONEncoder
from typing import Dict


class Point:
    @staticmethod
    def from_json(data):
        """
        Marshals a Point object from dict
        """
        point = Point()
        if not isinstance(data, Dict):
            return point
        if "selected" in data:
            point.value = data["selected"]
        if "completed" in data:
            point.value = data["completed"]
        if "value" in data:
            point.value = data["value"]
        return point

    def __init__(self):
        self.selected = False
        self.completed = False
        self.value = None


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
