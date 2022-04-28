# pylint disable=C
from typing import List

from kniffel.data_objects.point import Point


class MockGameCard:
    def __init__(self):
        self.points = None
        self.show = None

    def render(self, points: List[List[Point]]):
        self.points = points

    def show_selected(self, show):
        self.show = show
