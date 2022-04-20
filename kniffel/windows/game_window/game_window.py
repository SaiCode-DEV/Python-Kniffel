import curses
from typing import Tuple

import common
from data_objects.game_state import GameState
from kniffel.windows.game_window.dice_window import DiceWindow
from kniffel.windows.game_window.result_card import ResultCard
from kniffel.windows.game_window.game_card import GameCard


class GameWindow:
    @staticmethod
    def get_required_size() -> Tuple[int, int]:
        """
        Calculates the minimum screen size required for the game window
        @return: min_y-Value, min_x-Value
        """
        dice_y, dice_x = DiceWindow.get_required_size()
        result_card_y, result_card_x = ResultCard.get_required_size()
        game_card_y, game_card_x = GameCard.get_required_size()
        required_x = max(game_card_x, result_card_x) + dice_x
        str_len = len(common.LABEL_CONTROL_DESCRIPTION_GAME_WINDOW + GameCard.get_control_string())
        required_x = max(str_len, required_x)
        str_len = len(common.LABEL_CONTROL_DESCRIPTION_GAME_WINDOW + ResultCard.get_control_string())
        required_x = max(str_len, required_x)
        str_len = len(common.LABEL_CONTROL_DESCRIPTION_GAME_WINDOW + DiceWindow.get_control_string())
        required_x = max(str_len, required_x)
        required_y = max(game_card_y, result_card_y, dice_y + 2)  # plus two for statustext and message
        return required_y, required_x + 2

    def __init__(self, window: curses.window):
        self.control_str = ""
        self.message = ""
        self.window = window
        self.window.clear()
        self.window.refresh()
        card_window, dice_window = self.__get_sub_windows()

        self.__dice_window = DiceWindow(dice_window)
        self.__game_card = GameCard(card_window)
        self.__result_card = ResultCard(card_window)
        self.__current_card = self.__game_card

    @property
    def dice_window(self):
        return self.__dice_window

    @property
    def game_card(self):
        return self.__game_card

    @property
    def result_card(self):
        return self.__result_card

    def __get_sub_windows(self) -> Tuple[curses.window, curses.window]:
        [_, dice_x] = DiceWindow.get_required_size()
        [_, result_card_x] = ResultCard.get_required_size()
        [_, game_card_x] = GameCard.get_required_size()
        card_x = max(result_card_x, game_card_x)

        max_y, max_x = self.window.getmaxyx()
        card_window_x = int(max_x * (card_x / (card_x + dice_x)))
        dice_window_x = max_x - card_window_x
        card_window = self.window.subwin(max_y - 2, card_window_x, 1, 0)
        dice_window = self.window.subwin(max_y - 2, dice_window_x, 1, card_window_x)
        return card_window, dice_window

    def show_result_card(self, game_state: GameState):
        self.__current_card = self.__result_card
        self.render(game_state)

    def show_game_card(self, game_state: GameState):
        self.__current_card = self.__game_card
        self.render(game_state)

    def render(self, game_state: GameState):
        """
        Renders all relavent components onto the screen
        """
        self.window.clear()
        self.window.refresh()

        max_y, _ = self.window.getmaxyx()
        self.window.addstr(0, self.__get_str_off(self.message), self.message)
        self.window.addstr(max_y - 1, self.__get_str_off(self.control_str), self.control_str)

        self.__current_card.render(game_state.points)
        self.__dice_window.render(game_state.dice)

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

    def display_message(self, game_state: GameState, message: str):
        """
        Renders the passed message onto the screen
        @param game_state: current state of the game
        @param message: message that will be rendered to the screen
        """
        self.message = message
        self.render(game_state)

    def display_controls(self, game_state: GameState, control_str):
        self.control_str = control_str
        self.render(game_state)
