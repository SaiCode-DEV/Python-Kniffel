"""
The combinations module provides the data-objects
for handling a single players game state
"""

from enum import Enum
from typing import List, Callable

from kniffel.game_logic import value_calculator


class Combinations(Enum):
    """
    Combinations represents all possible entry fields
    The Values of the enum correspond to indices in an Array
    """
    ONES = 0
    TWOS = 1
    THREES = 2
    FOURS = 3
    FIVES = 4
    SIXES = 5

    THREE_OF_KIND = 6
    FOUR_OF_KIND = 7
    FULL_HOUSE = 8

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
    calc_fn = get_number_calc_fn(combinations)
    if calc_fn is not None:
        return calc_fn
    return get_special_combo_calc_fn(combinations)


def get_number_calc_fn(combinations: Combinations) -> Callable[[List[int]], int]:
    """
    returns a calculation function if the combination is a combination from one to six
    """
    calc_fn = None
    if combinations.value == Combinations.ONES.value:
        calc_fn = value_calculator.get_one_value
    if combinations.value == Combinations.TWOS.value:
        calc_fn = value_calculator.get_two_value
    if combinations.value == Combinations.THREES.value:
        calc_fn = value_calculator.get_three_value
    if combinations.value == Combinations.FOURS.value:
        calc_fn = value_calculator.get_four_value
    if combinations.value == Combinations.FIVES.value:
        calc_fn = value_calculator.get_five_value
    if combinations.value == Combinations.SIXES.value:
        calc_fn = value_calculator.get_six_value
    return calc_fn


def get_special_combo_calc_fn(combinations: Combinations) -> Callable[[List[int]], int]:
    """
    returns a calculation function if the combination is a special combination
    """
    calc_fn = None
    if combinations.value == Combinations.THREE_OF_KIND.value:
        calc_fn = value_calculator.get_three_of_kind_value
    if combinations.value == Combinations.FOUR_OF_KIND.value:
        calc_fn = value_calculator.get_four_of_kind_value

    if combinations.value == Combinations.FULL_HOUSE.value:
        calc_fn = value_calculator.get_full_house_value

    if combinations.value == Combinations.SMALL_STRAIGHT.value:
        calc_fn = value_calculator.get_small_straight_value
    if combinations.value == Combinations.LARGE_STRAIGHT.value:
        calc_fn = value_calculator.get_large_straight_value

    if combinations.value == Combinations.KNIFFEL.value:
        calc_fn = value_calculator.get_kniffel_value
    if combinations.value == Combinations.CHANCE.value:
        calc_fn = value_calculator.get_chance_value
    return calc_fn
