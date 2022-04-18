import curses
from typing import List, Dict

from data_objects.combinations import Combinations
from kniffel import common


class ResultCard:
    def __init__(self, window: curses.window):
        self.window = window

    @staticmethod
    def get_required_size():
        return len(common.RESULT_PAD), len(common.RESULT_PAD[0])

    @staticmethod
    def get_control_string() -> str:
        return common.LABEL_CONTROL_DESCRIPTION_RESULT_CARD

    def render(self, combinations: List[Dict[Combinations, int]]):
        pass

    def handle_input(self, ch: chr):
        pass
