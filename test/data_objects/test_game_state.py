# pylint: disable=C
import json
import os
from os import path
from unittest import TestCase

from test import data_objects, state_generator
from kniffel.data_objects.game_state import *

JSON_PATH = data_objects.__file__.replace("__init__.py", "") + "json-temp"


class GameStateTest(TestCase):
    def test_json_marshal(self):
        game_state = GameState()
        game_state.points = state_generator.get_random_combinations()
        game_state.dice = state_generator.get_random_dice()
        game_state.game_kind = EnumGameKind.GAME_AGAINST_BOT
        game_state.active_player = 2
        if not path.isdir(JSON_PATH):
            os.mkdir(JSON_PATH)
        with open(path.join(JSON_PATH, "test.json"), "w", encoding="utf-8") as file:
            json.dump(obj=game_state, fp=file, cls=GameStateEncoder, indent=4)
        with open(path.join(JSON_PATH, "test.json"), "r", encoding="utf-8") as file:
            data = json.load(file)
            new_game_state = GameState.from_json(data)
            self.assertEqual(game_state, new_game_state, "failed to write or read game state")
