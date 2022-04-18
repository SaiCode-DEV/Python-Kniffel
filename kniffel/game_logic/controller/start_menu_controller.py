from __future__ import annotations

import key_codes

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_logic.controller.kniffel_controller import KniffelController


class StartMenuController:
    def __init__(self, kniffel_controller: KniffelController):
        self.kniffel_controller = kniffel_controller

    def handle_input(self, ch: chr):
        if ch == key_codes.VK_UC_P or ch == key_codes.VK_LC_P:
            self.kniffel_controller.start_classic_game()
        if ch == key_codes.VK_LC_Q or ch == key_codes.VK_UC_Q:
            self.kniffel_controller.stop_game()
