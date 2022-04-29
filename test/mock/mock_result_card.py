# pylint disable=C

from typing import List

from kniffel.data_objects.point import Point


class MockResultCard:
    def __init__(self):
        self.points = None

    def render(self, points: List[List[Point]]):
        self.points = points
