# pylint: disable=C

from itertools import chain, combinations, product
from unittest import TestCase
import unittest
import threading
import sys

from kniffel.bot.bot import get_best_choice, bot_controller
from kniffel.data_objects.combinations import Combinations

# Only swich DEEP_Test to True if you want to test the bot with a lot of
# combinations. This will take a while.
DEEP_TEST = False

available_combinations = [
    Combinations.ONES,
    Combinations.TWOS,
    Combinations.THREES,
    Combinations.FOURS,
    Combinations.FIVES,
    Combinations.SIXES,
    Combinations.THREE_OF_KIND,
    Combinations.FOUR_OF_KIND,
    Combinations.FULL_HOUSE,
    Combinations.SMALL_STRAIGHT,
    Combinations.LARGE_STRAIGHT,
    Combinations.KNIFFEL,
    Combinations.CHANCE
]


class kniffel_bot_test(TestCase):
    """Test the kniffel bot. This test may take up to 10 sec to run."""

    def test_all_kniffel(self):
        dices = [
            [1, 1, 1, 1, 1],
            [2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3],
            [4, 4, 4, 4, 4],
            [5, 5, 5, 5, 5],
            [6, 6, 6, 6, 6]
        ]
        for dice in dices:
            new_value = get_best_choice(dice, [Combinations.KNIFFEL])
            self.assertEqual(new_value.get(next(iter(new_value))), 50)
            self.assertEqual(next(iter(new_value)), Combinations.KNIFFEL)

    def test_bot_combination_1(self):
        x = bot_controller([1, 2, 5, 3, 5], available_combinations, 1)
        self.assertTrue(x[0])
        self.assertEqual(list(x[1]), [True, True, False, False, False])

    def test_bot_combination_2(self):
        x = bot_controller([1, 2, 5, 3, 5], available_combinations, 1)
        self.assertTrue(x[0])
        self.assertEqual(list(x[1]), [True, True, False, False, False])

    def test_bot_combination_3(self):
        x = bot_controller([1, 2, 5, 3, 5], available_combinations, 1)
        self.assertTrue(x[0])
        self.assertEqual(list(x[1]), [True, True, False, False, False])

    def test_bot_combination_4(self):
        available = [
            Combinations.LARGE_STRAIGHT,
            Combinations.KNIFFEL
        ]
        x = bot_controller([5, 4, 3, 3, 1], available, 1)
        self.assertTrue(x[0])
        self.assertEqual(list(x[1]), [True, True, True, True, True])

    def test_bot_combination_5(self):
        available = [
            Combinations.LARGE_STRAIGHT,
            Combinations.KNIFFEL
        ]
        x = bot_controller([5, 4, 3, 3, 1], available, 0)
        self.assertFalse(x[0])
        self.assertEqual(x[1], Combinations.LARGE_STRAIGHT)

    def test_the_universe(self):

        def run_thread(dices, available, rerolls=0):
            if not DEEP_TEST:
                dices = dices[0:1]
            for dice in dices:
                try:
                    bot_controller(dice, available, rerolls)
                except Exception as e:
                    print(dice, available, end="\n")
                    raise e
        cubes = list(product(range(1, 7), repeat=5))
        cubes = sorted(set(tuple(sorted(cube)) for cube in cubes))
        cubes = sorted(list(cube) for cube in cubes)
        possible_combinations = chain(
            *map(
                lambda x: combinations(
                    available_combinations, x), range(
                    0, len(available_combinations) + 1)))
        for i, subset in enumerate(possible_combinations):
            if subset != ():
                threading.Thread(target=run_thread,
                                 args=(cubes, subset)).start()
                if i % 100 == 0 and DEEP_TEST:
                    print(f"Try out all combinations: {round(i/8192*100):>3}%")


if __name__ == "__main__":
    unittest.main()
