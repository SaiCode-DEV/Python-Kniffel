# pylint: disable=C
# pylint: disable=protected-access

from typing import List

from kniffel.data_objects import combinations
from kniffel.data_objects.dice import Dice
from kniffel.game_logic.value_calculator import InvalidThrow
from kniffel import common
from kniffel.data_objects.point import Point
from kniffel.game_logic.controller.game_controller.game_controller import GameController
from kniffel.data_objects.game_state import GameState
from kniffel.data_objects.combinations import Combinations


class MockGameController:

    def __init__(self):
        self.combination = None
        self.game_state = None
        self.message = None
        self.character = None
        self.combinations = None
        self.__reset_combinations()

    def __reset_combinations(self):
        """
        resets the all combinations to be empty again
        """
        self.combinations: List[List[Point]] = []
        for _ in range(common.PLAYER_COUNT):
            column = []
            for _ in range(common.COMBINATIONS_COUNT):
                column.append(Point())
            self.combinations.append(column)
        self.combinations[0][0].selected = True

    def handle_input(self, character: chr):
        self.character = character

    def display_message(self, message: str):
        self.message = message

    def add_entry(self, combination: Combinations):
        self.combination = combination

    def reset_game(self):
        pass

    def get_game_state(self) -> GameState:
        """
        Collects the active game state
        """
        game_state = GameState()
        dice = []
        for _ in range(common.DICE_COUNT):
            dice.append(Dice())
        game_state.dice = dice
        game_state.points = self.combinations
        game_state.active_player = 1
        game_state.roll_count = 0
        game_state.game_kind = GameController.game_kind
        return game_state

    def add_player_entry(self, combination: Combinations):
        """
        Adds the value of the current dice value to active players
        combinations as the passed combination
        @param combination: in which field the value is entered
        """
        player_combination = self.combinations[0]
        if player_combination[combination.value].value is not None:
            self.display_message(common.ERROR_COMBINATION_ALREADY_DONE)
            return
        self.__add_entry(combination)

    def __add_entry(self, combination: Combinations):
        """
        Adds the passed combination value to the combinations of the
        active player does not do any checks if entry is valid
        @param combination: in which field the value is entered
        """
        player_combination = self.combinations[0]
        calc_fn = combinations.get_calc_fn(combination)
        dice_values = [1, 2, 3, 4, 5]
        try:
            value = calc_fn(dice_values)
            player_combination[combination.value].value = value
        except InvalidThrow:
            self.display_message("Failed to count Dice values")
            return
