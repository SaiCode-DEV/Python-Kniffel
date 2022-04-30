# pylint: disable=C
# pylint: disable=protected-access

from typing import List

from kniffel.data_objects.dice import Dice


class MockDiceWindow:
    def __init__(self):
        self.dice = None
        self.show = False

    def render(self, dice: List[Dice]):
        self.dice = dice

    def show_selected(self, show: bool):
        self.show = show
