"""
Controller for managing the GameWindow and a Game's State
"""

from __future__ import annotations

import os
import time
from enum import Enum
import json
from os import path

from typing import TYPE_CHECKING, List

from kniffel.data_objects.game_kind import EnumGameKind
from kniffel import common
from kniffel import key_codes
from kniffel.data_objects import combinations
from kniffel.data_objects.combinations import Combinations
from kniffel.game_logic.value_calculator import InvalidThrow
from kniffel.data_objects.point import Point
from kniffel.data_objects.game_state import GameState, GameStateEncoder
from kniffel.game_logic.controller.game_controller.card_controller import CardController
from kniffel.game_logic.controller.game_controller.dice_controller import DiceController
from kniffel.windows.game_window.dice_window import DiceWindow
from kniffel.windows.game_window.game_window import GameWindow
from kniffel.windows.game_window.result_card import ResultCard

# to avoid a circular import
if TYPE_CHECKING:
    from game_logic.controller.kniffel_controller import KniffelController


class EnumWindowSelected(Enum):
    """
    Enum used for remembering active window
    """
    DICE_WINDOW = 1
    CARD_WINDOW = 2


class GameController:
    """
    The GameController class contains the logic for managing a game and for managing a games state
    """
    game_kind = EnumGameKind.GAME_AGAINST_HUMAN

    def __init__(self, kniffel_controller: KniffelController, game_window: GameWindow):
        """
        Initializes the Game Controller and all needed controllers for the controller
        to work properly
        @param kniffel_controller: KniffelController for controlling macro actions
        @param game_window: game window on which the actions will be visible
        """
        self.selected = EnumWindowSelected.DICE_WINDOW
        self.kniffel_controller = kniffel_controller
        self.game_window = game_window
        self.dice_controller: DiceController = DiceController(game_window.dice_window, self)
        self.card_controller: CardController = CardController(game_window.game_card,
                                                              game_window.result_card, self)

        self.__active_player: int = 0
        self.combinations: List[List[Point]] = []
        self.__reset_combinations()

        self.__update_control_str()

    @property
    def active_player(self) -> int:
        """
        @return: index of the currently active player
        """
        return self.__active_player

    @active_player.setter
    def active_player(self, active_player: int):
        """
        sets the currently active player index
        """
        self.__active_player = active_player

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

    def select_card_window(self):
        """
        switches the view to the card_window
        and re-renders the screen
        """
        self.selected = EnumWindowSelected.CARD_WINDOW
        self.dice_controller.show_selected(False)
        self.card_controller.show_selected(True)
        self.game_window.render(self.get_game_state())
        self.__update_control_str()

    def select_dice_window(self):
        """
        switches the view to the dice_window
        and re-renders the screen
        """
        self.selected = EnumWindowSelected.DICE_WINDOW
        self.card_controller.show_selected(False)
        self.dice_controller.show_selected(True)
        self.game_window.render(self.get_game_state())
        self.__update_control_str()

    def handle_input(self, character: chr):
        """
        Handles a Users input and decides what to do with it
        @param character: chr representing the users input
        """
        if character in (key_codes.VK_UC_Q, key_codes.VK_LC_Q):
            self.kniffel_controller.show_start_menu()

        # if the bot is currently playing or game is done ignore user input except quit
        if self.__is_game_over():
            return

        # switch between subwindows
        if character == key_codes.VK_HORIZONTAL_TAB:
            if self.selected is EnumWindowSelected.CARD_WINDOW:
                self.select_dice_window()
            elif self.selected is EnumWindowSelected.DICE_WINDOW:
                self.select_card_window()
            return
        self.__distribute_input(character)

    def __distribute_input(self, character: chr):
        """
        Checks what components are active and passes the given input down to them
        @param character: userinput for subcomponents
        """
        if self.selected is EnumWindowSelected.DICE_WINDOW:
            self.dice_controller.handle_input(character)
        elif self.selected is EnumWindowSelected.CARD_WINDOW:
            self.card_controller.handle_input(character)
        self.game_window.render(self.get_game_state())

    def __update_control_str(self):
        """
        Gets the control string and the active game state and renders them
        """
        game_state = self.get_game_state()
        control_str = self.__get_control_str()
        self.game_window.display_controls(game_state, control_str)

    def display_message(self, message: str):
        """
        Displays the given message to the user
        @param message: str which will be displayed
        @return:
        """
        self.game_window.display_message(self.get_game_state(), message)

    def __show_result(self):
        game_state = self.get_game_state()
        self.display_message(common.GAME_OVER)
        self.game_window.display_controls(game_state, common.LABEL_CONTROL_DESCRIPTION_GAME_WINDOW + ResultCard.get_control_string())
        self.game_window.show_result_card(game_state)

    def __get_control_str(self) -> str:
        """
        Concats the currently available options that the user has.
        @return: str concatenated control options
        """
        sub_str = ""
        if self.selected is EnumWindowSelected.CARD_WINDOW:
            sub_str = self.card_controller.get_control_str()
        elif self.selected is EnumWindowSelected.DICE_WINDOW:
            sub_str = DiceWindow.get_control_string()
        return common.LABEL_CONTROL_DESCRIPTION_GAME_WINDOW + sub_str

    def add_player_entry(self, combination: Combinations):
        """
        Adds the value of the current dice value to active players
        combinations as the passed combination
        @param combination: in which field the value is entered
        """
        player_combination = self.combinations[self.__active_player]
        if player_combination[combination.value].value is not None:
            self.display_message(common.ERROR_COMBINATION_ALREADY_DONE)
            return
        self.__add_entry(combination)
        self.game_window.render(self.get_game_state())
        if not self.__is_game_over():
            self.__next_player()

    def __add_bot_entry(self, combination: Combinations):
        """
        Adds the value of the current dice value to active players
        combinations as the passed combination without advancing player
        @param combination: in which field the value is entered
        """
        player_combination = self.combinations[self.__active_player]
        if player_combination[combination.value].value is not None:
            print("Bot made error should field already taken")
        self.__add_entry(combination)
        self.game_window.render(self.get_game_state())

    def __add_entry(self, combination: Combinations):
        """
        Adds the passed combination value to the combinations of the
        active player does not do any checks if entry is valid
        @param combination: in which field the value is entered
        """
        player_combination = self.combinations[self.__active_player]
        calc_fn = combinations.get_calc_fn(combination)
        try:
            value = calc_fn(self.dice_controller.get_dice_values())
            player_combination[combination.value].value = value
        except InvalidThrow:
            self.display_message("Failed to count Dice values")
            return

        if self.__is_game_over():
            self.dice_controller.unlock_all_dice()
            self.__show_result()

    def __run_bot(self):
        """
        runs the bot and enters its value to the active players combinations
        """
        self.dice_controller.show_selected(False)
        self.card_controller.show_selected(False)
        for _ in range(common.MAX_ROLL_COUNT):
            self.dice_controller.roll(common.ROLL_COUNT_ANIMATION)
            # todo ask bot what dice should be locked/what result should be entered
            time.sleep(common.BOT_DECISION_DELAY)
        # don't call add entry leads to recursive call
        # self.__add_bot_entry(Combinations(value of bot))
        self.game_window.render(self.get_game_state())
        time.sleep(common.BOT_DECISION_DELAY)

    def __next_player(self):
        """
        selects the next player and resets the roll count
        @return:
        """
        self.dice_controller.unlock_all_dice()
        self.dice_controller.reset_roll_count()
        active_player = (self.__active_player + 1) % len(self.combinations)
        self.__set_active_player(active_player)
        self.select_dice_window()

        bot_is_playing = GameController.game_kind.value == EnumGameKind.GAME_AGAINST_BOT.value and self.__active_player % 2 == 1
        if bot_is_playing:
            self.__run_bot()
            if self.__is_game_over():
                return
            self.__next_player()
            return
        self.dice_controller.roll(common.ROLL_COUNT_ANIMATION)

    def __is_game_over(self) -> bool:
        """
        Checks weather the last player has made its last move
        @return:
        """
        for entry in self.combinations[len(self.combinations) - 1]:
            if entry.value is None:
                return False
        return True

    def start_new_game(self, game_kind: EnumGameKind):
        """
        Resets the Game state so a new game can begin
        """
        GameController.game_kind = game_kind
        self.dice_controller.reset_roll_count()
        self.dice_controller.unlock_all_dice()
        self.__set_active_player(0)
        self.__reset_combinations()
        self.game_window.show_game_card(self.get_game_state())
        self.game_window.render(self.get_game_state())
        self.select_dice_window()
        self.dice_controller.roll(common.ROLL_COUNT_ANIMATION)

    def __set_active_player(self, number: int):
        """
        Sets the active player and updates screen to show active player
        @param number: index of active player
        """
        self.__active_player = number
        self.card_controller.set_selected_player(self.__active_player)
        self.display_message(common.LABEL_PLAYER_TURN.format(self.__active_player + 1))

    # ===========================================================================================================
    # State Management
    # ===========================================================================================================

    def save_to_file(self):
        """
        saves the current game_state to a file saved in common
        """
        if not path.isdir(common.DIR_PERSISTENCE):
            os.mkdir(common.DIR_PERSISTENCE)
        with open(common.FILE_GAME_STATE, "w", encoding="utf-8") as file:
            json.dump(obj=self.get_game_state(), fp=file, cls=GameStateEncoder, indent=4)

    def load_from_file(self):
        """
        loads the game_state from file specified in common
        """
        if path.isfile(common.FILE_GAME_STATE):
            with open(common.FILE_GAME_STATE, encoding="utf-8") as file:
                try:
                    data = json.load(file)
                    self.__set_game_state(data)
                except json.JSONDecodeError:
                    print("Error reading game state file")

    def __set_game_state(self, data):
        """
        Retrieves the game state from json data
        @param data: game_state in json form
        """
        try:
            game_state = GameState.from_json(data)
            self.dice_controller.set_dice(game_state.dice)
            self.combinations = game_state.points
            if len(self.combinations) != common.PLAYER_COUNT or \
                    len(self.combinations[0]) != common.COMBINATIONS_COUNT:
                self.__reset_combinations()
            GameController.game_kind = game_state.game_kind
            self.__set_active_player(game_state.active_player)
            self.dice_controller.set_roll_count(game_state.roll_count)
            if self.__is_game_over():
                self.__show_result()
        except TypeError as error:
            print("failed to load game state", error)
            self.start_new_game(EnumGameKind.GAME_AGAINST_HUMAN)

    def get_game_state(self) -> GameState:
        """
        Collects the active game state
        """
        game_state = GameState()
        game_state.dice = self.dice_controller.get_dice()
        game_state.points = self.combinations
        game_state.active_player = self.__active_player
        game_state.roll_count = self.dice_controller.roll_count
        game_state.game_kind = GameController.game_kind
        return game_state
