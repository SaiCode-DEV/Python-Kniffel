"""
The start_menu_controller module contains the logic needed for the start menu
of the game
"""
from __future__ import annotations
from typing import TYPE_CHECKING

from kniffel import key_codes
from kniffel.windows.start_window import StartWindow

if TYPE_CHECKING:
    from game_logic.controller.kniffel_controller import KniffelController


class StartMenuController:
    """
    Start menu controller handles the inputs on the start menu window
    """

    def __init__(self, kniffel_controller: KniffelController, start_window: StartWindow):
        self.kniffel_controller = kniffel_controller
        self.start_window = start_window

    def handle_input(self, character: chr):
        """
        Decides what to do with a users input
        @param character: input from the user
        """
        if character in (key_codes.VK_UC_P, key_codes.VK_LC_P):
            self.kniffel_controller.start_classic_game()
        if character in (key_codes.VK_LC_Q, key_codes.VK_UC_Q):
            self.kniffel_controller.exit()

    def step_animation(self):
        """
        Steps the currently displayed animation one step forward
        """
        self.start_window.step_animation()
