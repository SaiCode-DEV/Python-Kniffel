from typing import List

from kniffel.data_objects.point import Point


class MockaResultCard:
    def __init__(self):
        self.points = []

    def render(self, points: List[List[Point]]):
        self.points = points
