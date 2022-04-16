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

    SMALL_STRAIGHT = 9
    LARGE_STRAIGHT = 10

    KNIFFEL = 11
    CHANCE = 12
