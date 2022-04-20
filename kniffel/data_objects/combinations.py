"""
The combinations module provides the data-objects
for handling a single players game state
"""

from enum import Enum
from typing import List, Callable

from kniffel.game_logic import value_calculator


class Combinations(Enum):
    """
    In combinations
    """
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
    """
    Returns a function for calculating the passed combination
    @param combinations: Combination for which a function is searched
    @return: Callable[[List[int]], int]
    """
    calc_fn = None
    if combinations is Combinations.ONES:
        calc_fn = lambda x: value_calculator.get_number_value(1, x)
    if combinations is Combinations.TWOS:
        calc_fn = lambda x: value_calculator.get_number_value(2, x)
    if combinations is Combinations.THREES:
        calc_fn = lambda x: value_calculator.get_number_value(3, x)
    if combinations is Combinations.FOURS:
        calc_fn = lambda x: value_calculator.get_number_value(4, x)
    if combinations is Combinations.FIVES:
        calc_fn = lambda x: value_calculator.get_number_value(5, x)
    if combinations is Combinations.SIXES:
        calc_fn = lambda x: value_calculator.get_number_value(6, x)

    if combinations is Combinations.THREE_OF_KIND:
        calc_fn = value_calculator.get_three_of_kind_value
    if combinations is Combinations.FOUR_OF_KIND:
        calc_fn = value_calculator.get_four_of_kind_value

    if combinations is Combinations.SMALL_STRAIGHT:
        calc_fn = value_calculator.get_small_straight_value
    if combinations is Combinations.LARGE_STRAIGHT:
        calc_fn = value_calculator.get_large_straight_value

    if combinations is Combinations.KNIFFEL:
        calc_fn = value_calculator.get_kniffel_value
    if combinations is Combinations.CHANCE:
        calc_fn = value_calculator.get_chance_value
    return calc_fn
