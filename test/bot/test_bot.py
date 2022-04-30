# pylint: disable=C
from unittest import TestCase
import unittest

from kniffel.bot.bot import get_best_choice,bot_controller
from kniffel.data_objects.combinations import Combinations
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

    def test_all_combinations(self):
        """Yesss
        """

        dices = []
        for dice1 in range(6):
            for dice2 in range(6):
                for dice3 in range(6):
                    for dice4 in range(6):
                        for dice5 in range(6):
                            # create a new list with the new dice values
                            dices.append(
                                sorted([dice1 + 1, dice2 + 1, dice3 + 1, dice4 + 1, dice5 + 1]))
        dices = list(set({tuple(i) for i in dices}))
        dices = sorted([list(i) for i in dices])
        for dice in dices:
            new_value = get_best_choice(dice, available_combinations)
            # subdivide 10 from chance
            self.assertGreater(new_value.get(next(iter(new_value))), 0)
            self.assertLessEqual(new_value.get(next(iter(new_value))), 50)


    def test_bot_combination_1(self):
        x = bot_controller([1, 2, 5, 3, 5], available_combinations, 1)
        self.assertTrue(x[0])
        self.assertEqual(list(x[1]),[True, True, False, False, False])

    def test_bot_combination_2(self):
        x = bot_controller([1, 2, 5, 3, 5], available_combinations, 1)
        self.assertTrue(x[0])
        self.assertEqual(list(x[1]),[True, True, False, False, False])

    def test_bot_combination_3(self):
        x = bot_controller([1, 2, 5, 3, 5], available_combinations, 1)
        self.assertTrue(x[0])
        self.assertEqual(list(x[1]),[True, True, False, False, False])

if __name__ == "__main__":
    unittest.main()
