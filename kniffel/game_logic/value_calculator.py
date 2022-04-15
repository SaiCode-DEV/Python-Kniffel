"""
Here are Functions which take in a Kniffel-Turn-Value aka a List of Five Numbers.
Depending on the function that is called the according value of the corresponding
Field will be returned.
"""
import unittest

from typing import Dict, List

FULL_HOUSE_VALUE = 25
SMALL_STRAIGHT_VALUE = 30
LARGE_STRAIGHT_VALUE = 40
KNIFFEL_VALUE = 50


class InvalidThrow(Exception):
    pass


def validate_throw(throw: List[int]):
    if len(throw) != 5:
        raise InvalidThrow(f"A throw has to consist of 5 Dice not: {len(throw)}")
    for dice in throw:
        if dice < 1 or dice > 6:
            raise InvalidThrow(f"In the passed throw is at least one number not between 1 and 6 got {throw}")


def contains_n_dice(count: int, throw: List[int]) -> bool:
    counts = get_count_dict(throw)
    for _, value in counts.items():
        if value >= count:
            return True
    return False


def get_count_dict(throw: List[int]) -> Dict[int, int]:
    counts = {}
    for dice in throw:
        if dice in counts:
            counts[dice] += 1
        else:
            counts[dice] = 1
    return counts


def get_number_value(number: int, throw: List[int]) -> int:
    validate_throw(throw)
    result = 0
    for dice in throw:
        if number == dice:
            result += dice
    return result


def get_three_of_kind(throw: List[int]) -> int:
    validate_throw(throw)
    result = 0
    for dice in throw:
        result += dice
    if contains_n_dice(3, throw):
        return result
    return 0


def get_four_of_kind(throw: List[int]) -> int:
    validate_throw(throw)
    result = 0
    for dice in throw:
        result += dice
    if contains_n_dice(4, throw):
        return result
    return 0


def get_full_house(throw: List[int]) -> int:
    validate_throw(throw)
    counts = get_count_dict(throw)
    three, two = False, False
    for _, count in counts.items():
        if count == 2:
            two = True
        if count == 3:
            three = True
    if two and three:
        return FULL_HOUSE_VALUE
    return 0


def count_run(throw: List[int]) -> int:
    longest_run = 0
    run = 0
    for i in range(1, 7):
        if i in throw:
            run += 1
        else:
            if run > longest_run:
                longest_run = run
                run = 0
    if run > longest_run:
        longest_run = run
    return longest_run


def get_small_straight(throw: List[int]) -> int:
    validate_throw(throw)
    if count_run(throw) >= 3:
        return SMALL_STRAIGHT_VALUE
    return 0


def get_large_straight(throw: List[int]) -> int:
    validate_throw(throw)
    if count_run(throw) >= 4:
        return LARGE_STRAIGHT_VALUE
    return 0


def get_kniffel(throw: List[int]) -> int:
    validate_throw(throw)
    value = throw[0]
    for dice in throw:
        if dice != value:
            return 0
    return KNIFFEL_VALUE


def get_chance(throw: List[int]) -> int:
    validate_throw(throw)
    result = 0
    for dice in throw:
        result += dice
    return result
