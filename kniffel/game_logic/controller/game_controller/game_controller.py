"""
Controller for managing the GameWindow and a Game's State
"""

from __future__ import annotations

from enum import Enum

from typing import TYPE_CHECKING, List
from kniffel import common
from kniffel import key_codes
from kniffel.data_objects import combinations
from kniffel.data_objects.combinations import Combinations
from kniffel.game_logic.value_calculator import InvalidThrow
from kniffel.data_objects.point import Point
from kniffel.data_objects.game_state import GameState
from kniffel.game_logic.controller.game_controller.card_controller import CardController
from kniffel.game_logic.controller.game_controller.dice_controller import DiceController
from kniffel.windows.game_window.dice_window import DiceWindow
from kniffel.windows.game_window.game_window import GameWindow

# to avoid a circular import
if TYPE_CHECKING:
    from game_logic.controller.kniffel_controller import KniffelController


class EnumWindowSelected(Enum):
    """
    Enum used for remembering active window
    """
    DICE_WINDOW = 1
    CARD_WINDOW = 2
    RESULT_WINDOW = 3


class GameController:
    """
    The GameController class contains the logic for managing a game and for managing a games state
    """

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
        self.card_controller: CardController = CardController(game_window.game_card, game_window.result_card, self)

        self.__active_player: int = 0
        self.combinations: List[List[Point]] = []
        self.__reset_combinations()
        self.__combinations_counter = common.COMBINATIONS_COUNT * 2

        self.__update_control_str()

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

    def select_result_window(self):
        """
        switches the view to the result_window
        and re-render the screen
        """
        self.selected = EnumWindowSelected.RESULT_WINDOW
        self.dice_controller.show_selected(False)
        self.card_controller.show_selected(False)
        self.game_window.render(self.get_game_state())
        self.__update_control_str()

    def handle_input(self, character: chr):
        """
        Handles a Users input and decides what to do with it
        @param character: chr representing the users input
        """
        if character in (key_codes.VK_UC_Q, key_codes.VK_LC_Q):
            self.kniffel_controller.show_start_menu()

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

    def get_game_state(self) -> GameState:
        """
        Collects the active game state
        """
        return GameState(self.dice_controller.get_dice(), self.combinations)

    def add_entry(self, combination: Combinations):
        """
        Adds the value of the current dice value to active players
        combinations as the passed combination
        @param combination: in which field the value is entered
        """
        player_combination = self.combinations[self.__active_player]
        if player_combination[combination.value].value is not None:
            self.display_message(common.ERROR_COMBINATION_ALREADY_DONE)
            return

        self.__combinations_counter -= 1
        calc_fn = combinations.get_calc_fn(combination)
        try:
            value = calc_fn(self.dice_controller.get_dice_values())
            player_combination[combination.value].value = value
        except InvalidThrow:
            self.display_message("Failed to count Dice values")
            return
        if self.__combinations_counter == 0:
            self.display_message(common.GAME_OVER)
            self.game_window.show_result_card(self.get_game_state())
            return
        self.game_window.render(self.get_game_state())
        self.__next_player()

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

        self.dice_controller.roll(common.ROLL_COUNT_ANIMATION)

    def reset_game(self):
        """
        Resets the Game state so a new game can begin
        """
        self.dice_controller.reset_roll_count()
        self.__set_active_player(0)
        self.__reset_combinations()
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
