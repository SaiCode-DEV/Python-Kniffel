# pylint: disable=C
# pylint: disable=protected-access


from typing import List

from kniffel.data_objects.point import Point


class MockResultCard:
    def __init__(self):
        self.__points = None

    def render(self, points: List[List[Point]]):
        self.__points = points

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, points):
        self.__points = points
