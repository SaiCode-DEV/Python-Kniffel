# pylint: disable=C
import json
import os
from os import path
from unittest import TestCase
import unittest

from test import data_objects, state_generator
from kniffel.data_objects.game_state import *
from kniffel.bot.bot import *
from kniffel.data_objects.combinations import Combinations


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
            
if __name__ == "__main__":
    unittest.main()
