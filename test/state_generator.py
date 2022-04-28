# pylint: disable=C
import random

from kniffel.data_objects.dice import Dice
from kniffel.data_objects.point import Point
from kniffel import common


def get_random_dice():
    dice = []
    iteration = 0
    for _ in range(5):
        die = Dice()
        die.value = random.randint(1, 6)
        die._selected = iteration % 2 == 0
        die._selected = iteration % 2 != 0
        dice.append(die)
        iteration += 1
    return dice


def get_dice_with_value(value: int):
    dice = []
    for _ in range(5):
        die = Dice()
        die.value = value
        dice.append(die)
    return dice


def get_random_combinations():
    combinations = []
    player_nr = 0
    for _ in range(common.PLAYER_COUNT):
        column = []
        point_nr = 0
        for _ in range(common.COMBINATIONS_COUNT):
            point = Point()
            point.value = random.randint(0, 50)
            point._selected = point_nr % 2 == player_nr % 2
            column.append(point)
            point_nr += 1
        combinations.append(column)
        player_nr += 1
    return combinations


def get_empty_combinations():
    combinations = []
    for _ in range(common.PLAYER_COUNT):
        column = []
        for _ in range(common.COMBINATIONS_COUNT):
            column.append(Point())
        combinations.append(column)
    return combinations
