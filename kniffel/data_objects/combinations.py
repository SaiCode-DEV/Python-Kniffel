from enum import Enum


class Combinations(Enum):
    ONES = 1
    TWOS = 2
    THREES = 3
    FOURS = 4
    FIVES = 5
    SIXES = 6

    THREE_OF_KIND = 7
    FOUR_OF_KIND = 8
    FULL_HOUSE = 9

    SMALL_STRAIGHT = 10
    LARGE_STRAIGHT = 11

    KNIFFEL = 12
    CHANCE = 13
