import curses
from typing import Tuple
from enum import Enum

from kniffel.windows.game_window.dice import DiceSet
from kniffel.windows.game_window.result_card import ResultCard
from kniffel.windows.game_window.game_card import GameCard


class EnumSelected(Enum):
    CARD_SELECTED = 1
    DICE_SELECTED = 2


class GameWindow:
    @staticmethod
    def get_required_size() -> Tuple[int, int]:
        dice_y, dice_x = DiceSet.get_required_size()
        result_card_y, result_card_x = ResultCard.get_required_size()
        game_card_y, game_card_x = GameCard.get_required_size()
        required_x = max(game_card_x, result_card_x) + dice_x
        required_y = max(game_card_y, result_card_y) + dice_y + 1  # plus one for statustext
        return required_y, required_x

    def __init__(self, window: curses.window):
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
        card_window = curses.newwin(max_y - 1, card_window_x, 0, 0)
        dice_window = curses.newwin(max_y - 1, dice_window_x, 0, card_window_x)
        return card_window, dice_window

    def handle_input(self, ch: chr):
        if ch == curses.KEY_CTAB:
            if self.selected is EnumSelected.CARD_SELECTED:
                self.selected = EnumSelected.DICE_SELECTED
            elif self.selected is EnumSelected.DICE_SELECTED:
                self.selected = EnumSelected.CARD_SELECTED
            return
        if self.selected is EnumSelected.DICE_SELECTED:
            self.dice_set.handle_input(ch)
        elif self.selected is EnumSelected.CARD_SELECTED:
            self.current_card.handle_input(ch)

    def show_result_card(self):
        self.current_card = self.result_card
        self.render()

    def show_game_card(self):
        self.current_card = self.game_card
        self.render()

    def render(self):
        max_y, _ = self.window.getmaxyx()

        self.window.clear()
        self.window.refresh()

        self.window.addstr(max_y - 1, 0, self.__get_control_str())
        self.current_card.render()
        self.dice_set.render()

    def __get_control_str(self) -> str:
        if self.selected is EnumSelected.CARD_SELECTED:
            if isinstance(self.current_card, GameCard):
                return GameCard.get_control_string()
            elif isinstance(self.current_card, ResultCard):
                return ResultCard.get_control_string()
        elif self.selected is EnumSelected.DICE_SELECTED:
            return DiceSet.get_control_string()
        return ""
