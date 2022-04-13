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
    three, two = False
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


"""
Testing the valueCalculator Functions
"""

from unittest import TestCase
from typing import Callable, List


class TestValueCalculator(TestCase):

    def invalid_throw(self, func: Callable[[List[int]], int]):
        with self.assertRaises(InvalidThrow):
            func([0, 1, 1, 1, 1])
        with self.assertRaises(InvalidThrow):
            func([7, 1, 1, 1, 1])
        with self.assertRaises(InvalidThrow):
            func([0, 1])

    def test_get_number_value(self):
        with self.assertRaises(InvalidThrow):
            get_number_value(1, [0, 1, 1, 1, 1])
        with self.assertRaises(InvalidThrow):
            get_number_value(1, [7, 1, 1, 1, 1])
        with self.assertRaises(InvalidThrow):
            get_number_value(1, [0, 1])
        result = get_number_value(1, [1, 1, 1, 2, 6])
        self.assertEqual(3, result, "1,[1, 1, 1, 2, 6] should result to 3")
        result = get_number_value(5, [1, 3, 1, 2, 6])
        self.assertEqual(0, result, "5,[1, 3, 1, 2, 6] should result to 0")

    def test_get_three_of_kind(self):
        self.invalid_throw(lambda x: get_three_of_kind(x))
        result = get_three_of_kind([1, 1, 1, 2, 6])
        self.assertEqual(11, result, "[1,1,1,2,6] should result to 11")
        result = get_three_of_kind([1, 3, 1, 2, 6])
        self.assertEqual(0, result, "[1,3,1,2,6] should result to ß")

    def test_get_three_of_kind(self):
        self.invalid_throw(lambda x: get_four_of_kind(x))
        result = get_four_of_kind([1, 1, 1, 2, 6])
        self.assertEqual(0, result, "[1,1,1,2,6] should result to 0")
        result = get_four_of_kind([1, 1, 1, 1, 6])
        self.assertEqual(10, result, "[1,3,1,2,6] should result to 10")

    def test_get_full_house(self):
        self.invalid_throw(lambda x: get_full_house(x))
        result = get_full_house([1, 1, 3, 2, 2])
        self.assertEqual(0, result, "[1,1,3,2,2] should result to 0")
        result = get_full_house([1, 1, 1, 2, 2])
        self.assertEqual(FULL_HOUSE_VALUE, result, f"[1,1,1,2,2] should result to {FULL_HOUSE_VALUE}")

    def test_count_run(self):
        result = count_run([1, 1, 3, 2, 2])
        self.assertEqual(3, result, "[1,1,3,2,2] should result to 3")
        result = count_run([1, 4, 3, 2, 5])
        self.assertEqual(5, result, "[1, 4, 3, 2, 5] should result to 5")
        result = count_run([1, 1, 1, 1, 1])
        self.assertEqual(1, result, "[1, 1, 1, 1, 1] should result to 1")
        result = count_run([4, 4, 3, 5, 5])
        self.assertEqual(3, result, "[4,4,3,5,5] should result to 3")

    def test_small_straight(self):
        self.invalid_throw(lambda x: get_small_straight(x))
        result = get_small_straight([1, 1, 3, 2, 2])
        self.assertEqual(SMALL_STRAIGHT_VALUE, result, f"[1,1,3,2,2] should result to {SMALL_STRAIGHT_VALUE}")
        result = get_small_straight([1, 4, 3, 2, 5])
        self.assertEqual(SMALL_STRAIGHT_VALUE, result, f"[1, 4, 3, 2, 5] should result to {SMALL_STRAIGHT_VALUE}")
        result = get_small_straight([1, 1, 1, 2, 1])
        self.assertEqual(0, result, "[1, 1, 1, 2, 1] should result to 0")

    def test_large_straight(self):
        self.invalid_throw(lambda x: get_large_straight(x))
        result = get_large_straight([1, 1, 3, 2, 2])
        self.assertEqual(0, result, f"[1,1,3,2,2] should result to 0")
        result = get_large_straight([1, 4, 3, 2, 5])
        self.assertEqual(LARGE_STRAIGHT_VALUE, result, f"[1, 4, 3, 2, 5] should result to {LARGE_STRAIGHT_VALUE}")
        result = get_large_straight([1, 1, 1, 2, 1])
        self.assertEqual(0, result, "[1, 1, 1, 2, 1] should result to 0")

    def test_kniffel(self):
        self.invalid_throw(lambda x: get_kniffel(x))
        result = get_kniffel([1, 1, 2, 1, 1])
        self.assertEqual(0, result, f"[1,1,2,1,1] should result to 0")
        result = get_kniffel([4, 4, 4, 4, 4])
        self.assertEqual(KNIFFEL_VALUE, result, f"[4,4,4,4,4] should result to {KNIFFEL_VALUE}")

    def test_chance(self):
        self.invalid_throw(lambda x: get_chance(x))
        result = get_chance([1, 1, 2, 1, 1])
        self.assertEqual(6, result, "[1,1,2,1,1] should result to 6")
        result = get_chance([4, 4, 4, 4, 4])
        self.assertEqual(20, result, "[4,4,4,4,4] should result to 20")
