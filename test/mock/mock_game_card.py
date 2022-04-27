from typing import List

from kniffel.data_objects.point import Point


class MockaGameCard:
    def __init__(self):
        self.combinations = []
        self.show = False

    def render(self, combinations: List[List[Point]]):
        self.combinations = combinations

    def show_selected(self, show: bool):
        self.show = show
