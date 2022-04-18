import curses
from typing import Tuple
from enum import Enum

import common
import key_codes
from kniffel.windows.game_window.dice import DiceSet
from kniffel.windows.game_window.result_card import ResultCard
from kniffel.windows.game_window.game_card import GameCard


class EnumSelected(Enum):
    CARD_SELECTED = 1
    DICE_SELECTED = 2


class GameWindow:
    @staticmethod
    def get_required_size() -> Tuple[int, int]:
        """
        Calculates the minimum screen size required for the game window
        @return: min_y-Value, min_x-Value
        """
        dice_y, dice_x = DiceSet.get_required_size()
        result_card_y, result_card_x = ResultCard.get_required_size()
        game_card_y, game_card_x = GameCard.get_required_size()
        required_x = max(game_card_x, result_card_x) + dice_x
        str_len = len(common.LABEL_CONTROL_DESCRIPTION_GAME_WINDOW + GameCard.get_control_string())
        required_x = max(str_len, required_x)
        str_len = len(common.LABEL_CONTROL_DESCRIPTION_GAME_WINDOW + ResultCard.get_control_string())
        required_x = max(str_len, required_x)
        str_len = len(common.LABEL_CONTROL_DESCRIPTION_GAME_WINDOW + DiceSet.get_control_string())
        required_x = max(str_len, required_x)
        required_y = max(game_card_y, result_card_y, dice_y + 2)  # plus two for statustext and message
        return required_y, required_x + 2

    def __init__(self, window: curses.window):
        self.message = ""
        self.window = window
        self.window.clear()
        self.window.refresh()
        card_window, dice_window = self.__get_sub_windows()

        self.dice_set = DiceSet(dice_window)
        self.game_card = GameCard(card_window)
        self.result_card = ResultCard(card_window)
        self.current_card = self.game_card
        self.selected = EnumSelected.DICE_SELECTED

    def __get_sub_windows(self) -> Tuple[curses.window, curses.window]:
        [_, dice_x] = DiceSet.get_required_size()
        [_, result_card_x] = ResultCard.get_required_size()
        [_, game_card_x] = GameCard.get_required_size()
        card_x = max(result_card_x, game_card_x)

        max_y, max_x = self.window.getmaxyx()
        card_window_x = int(max_x * (card_x / (card_x + dice_x)))
        dice_window_x = max_x - card_window_x
        card_window = self.window.subwin(max_y - 2, card_window_x, 1, 0)
        dice_window = self.window.subwin(max_y - 2, dice_window_x, 1, card_window_x)
        return card_window, dice_window

    def handle_input(self, ch: chr):
        if ch == key_codes.VK_HORIZONTAL_TAB:
            if self.selected is EnumSelected.CARD_SELECTED:
                self.selected = EnumSelected.DICE_SELECTED
                self.dice_set.show_selected(True)
            elif self.selected is EnumSelected.DICE_SELECTED:
                self.selected = EnumSelected.CARD_SELECTED
                self.dice_set.show_selected(False)
            self.render()
            return
        if ch == key_codes.VK_SPACE and self.selected is EnumSelected.DICE_SELECTED:
            self.dice_set.roll(8)
            return
        self.__distribute_input(ch)

    def __distribute_input(self, ch: chr):
        """
        Checks what components are active and passes the given input down to them
        @param ch: userinput for subcomponents
        """
        if self.selected is EnumSelected.DICE_SELECTED:
            self.dice_set.handle_input(ch)
        elif self.selected is EnumSelected.CARD_SELECTED:
            self.current_card.handle_input(ch)
        self.render()

    def show_result_card(self):
        self.current_card = self.result_card
        self.render()

    def show_game_card(self):
        self.current_card = self.game_card
        self.render()

    def render(self):
        """
        Renders all relavent components onto the screen
        """
        self.window.clear()
        self.window.refresh()

        max_y, _ = self.window.getmaxyx()
        self.window.addstr(0, self.__get_str_off(self.message), self.message)
        ctr_str = self.__get_control_str()
        self.window.addstr(max_y - 1, self.__get_str_off(ctr_str), ctr_str)

        self.current_card.render()
        self.dice_set.render()

    def __get_str_off(self, msg: str) -> int:
        """
        Retunrs the required x_offset for placing a string at the middle of the screen
        @param msg: the string for which the offset is going to be calculated
        """
        _, max_x = self.window.getmaxyx()
        if msg is None:
            return max_x // 2
        if max_x <= len(msg):
            return 0
        return (max_x - len(msg)) // 2

    def display_message(self, message: str):
        """
        Renders the passed message onto the screen
        @param message: message that will be rendered to the screen
        """
        self.message = message
        self.render()

    def __get_control_str(self) -> str:
        """
        Concats the currently available options that the user has.
        @return: str concatenated control options
        """
        sub_str = ""
        if self.selected is EnumSelected.CARD_SELECTED:
            if isinstance(self.current_card, GameCard):
                sub_str = GameCard.get_control_string()
            elif isinstance(self.current_card, ResultCard):
                sub_str = ResultCard.get_control_string()
        elif self.selected is EnumSelected.DICE_SELECTED:
            sub_str = DiceSet.get_control_string()
        return common.LABEL_CONTROL_DESCRIPTION_GAME_WINDOW + sub_str
