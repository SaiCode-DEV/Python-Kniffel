from __future__ import annotations

from enum import Enum

import common
import key_codes
from kniffel.data_objects.game_state import GameState
from kniffel.game_logic.controller.card_controller import CardController
from kniffel.game_logic.controller.dice_controller import DiceController
from kniffel.windows.game_window.dice_window import DiceWindow
from kniffel.windows.game_window.game_window import GameWindow
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_logic.controller.kniffel_controller import KniffelController


class EnumWindowSelected(Enum):
    """
    Enum used for remembering active window
    """
    DICE_WINDOW = 1
    CARD_WINDOW = 2


class GameController:
    def __init__(self, kniffel_controller: KniffelController, game_window: GameWindow):
        self.selected = EnumWindowSelected.DICE_WINDOW
        self.kniffel_controller = kniffel_controller
        self.game_window = game_window
        self.dice_controller = DiceController(game_window.dice_window)
        self.card_controller = CardController()
        self.__update_control_str()

    def handle_input(self, ch: chr):
        if ch == key_codes.VK_UC_Q or ch == key_codes.VK_LC_Q:
            self.kniffel_controller.stop_game()

        if ch == key_codes.VK_HORIZONTAL_TAB:
            if self.selected is EnumWindowSelected.CARD_WINDOW:
                self.selected = EnumWindowSelected.DICE_WINDOW
                self.dice_controller.show_selected(True)
            elif self.selected is EnumWindowSelected.DICE_WINDOW:
                self.selected = EnumWindowSelected.CARD_WINDOW
                self.dice_controller.show_selected(False)
                self.game_window.render(self.get_game_state())
            self.__update_control_str()
            return
        if ch == key_codes.VK_SPACE and self.selected is EnumWindowSelected.DICE_WINDOW:
            self.dice_controller.roll(8)
            return
        self.__distribute_input(ch)

    def __distribute_input(self, ch: chr):
        """
        Checks what components are active and passes the given input down to them
        @param ch: userinput for subcomponents
        """
        if self.selected is EnumWindowSelected.DICE_WINDOW:
            self.dice_controller.handle_input(ch)
        elif self.selected is EnumWindowSelected.CARD_WINDOW:
            self.card_controller.handle_input(ch)
        self.game_window.render(self.get_game_state())

    def __update_control_str(self):
        game_state = self.get_game_state()
        control_str = self.__get_control_str()
        self.game_window.display_controls(game_state, control_str)

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
        return GameState(self.dice_controller.get_dice())  # todo get state from card controller
