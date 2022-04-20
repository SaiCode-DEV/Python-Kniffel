import curses

from data_objects.combinations import Combinations

POINTS_PAD = [
    "------",
    "{}!",
    "-----!",
    "{}!",
    "-----!",
    "{}!",
    "-----!",
    "{}!",
    "-----!",
    "{}!",
    "-----!",
    "{}!",
    "-----!",
    "{}!",
    "-----!",
    "{}!",
    "-----!",
    "{}!",
    "-----!",
    "{}!",
    "-----!",
    "{}!",
    "-----!",
    "{}!",
    "-----!",
    "{}!",
    "------"
]

points = {
    Combinations.ONES: "     ",
    Combinations.TWOS: "     ",
    Combinations.THREES: "     ",
    Combinations.FOURS: "     ",
    Combinations.FIVES: "     ",
    Combinations.SIXES: "     ",

    Combinations.THREE_OF_KIND: "     ",
    Combinations.FOUR_OF_KIND: "     ",
    Combinations.FULL_HOUSE: "     ",
    Combinations.SMALL_STRAIGHT: "     ",
    Combinations.LARGE_STRAIGHT: "     ",
    Combinations.KNIFFEL: "     ",
    Combinations.CHANCE: "     "
}


class PointsWindow:
    def __init__(self, window: curses.window):
        self.__window = window
        self.__selected_player = 1
        self.__selected_combination = None
