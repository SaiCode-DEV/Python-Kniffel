# pylint: disable=C
import json
import random
from os import path
from unittest import TestCase

from kniffel import common
from test import data_objects
from kniffel.data_objects.game_state import *

JSON_PATH = data_objects.__file__.replace("__init__.py", "") + "json"


def get_random_dice():
    dice = []
    iteration = 0
    for _ in range(5):
        die = Dice()
        die.value = random.randint(1, 6)
        die.selected = iteration % 2 == 0
        die.selected = iteration % 2 != 0
        dice.append(die)
        iteration += 1
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
            point.selected = point_nr % 2 == player_nr % 2
            column.append(point)
            point_nr += 1
        combinations.append(column)
        player_nr += 1
    return combinations


class GameStateTest(TestCase):
    def test_json_marshal(self):
        game_state = GameState()
        game_state.points = get_random_combinations()
        game_state.dice = get_random_dice()
        game_state.game_kind = EnumGameKind.GAME_AGAINST_BOT
        game_state.active_player = 2
        with open(path.join(JSON_PATH, "test.json"), "w", encoding="utf-8") as file:
            json.dump(obj=game_state, fp=file, cls=GameStateEncoder, indent=4)
        with open(path.join(JSON_PATH, "test.json"), "r", encoding="utf-8") as file:
            data = json.load(file)
            new_game_state = GameState.from_json(data)
            self.assertEqual(game_state, new_game_state, "failed to write or read game state")
