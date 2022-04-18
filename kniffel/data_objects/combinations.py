from enum import Enum
from typing import List, Callable

from game_logic import value_calculator


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


def get_calc_fn(combinations: Combinations) -> Callable[[List[int]], int]:
    if combinations is Combinations.ONES:
        return lambda x: value_calculator.get_number_value(1, x)
    elif combinations is Combinations.TWOS:
        return lambda x: value_calculator.get_number_value(2, x)
    elif combinations is Combinations.THREES:
        return lambda x: value_calculator.get_number_value(3, x)
    elif combinations is Combinations.FOURS:
        return lambda x: value_calculator.get_number_value(4, x)
    elif combinations is Combinations.FIVES:
        return lambda x: value_calculator.get_number_value(5, x)
    elif combinations is Combinations.SIXES:
        return lambda x: value_calculator.get_number_value(6, x)

    elif combinations is Combinations.THREE_OF_KIND:
        return value_calculator.get_three_of_kind_value
    elif combinations is Combinations.FOUR_OF_KIND:
        return value_calculator.get_four_of_kind_value

    elif combinations is Combinations.SMALL_STRAIGHT:
        return value_calculator.get_small_straight_value
    elif combinations is Combinations.LARGE_STRAIGHT:
        return value_calculator.get_large_straight_value

    elif combinations is Combinations.KNIFFEL:
        return value_calculator.get_kniffel_value
    elif combinations is Combinations.CHANCE:
        return value_calculator.get_chance_value
