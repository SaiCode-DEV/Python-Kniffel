"""
The kniffel-controller contains the functionality needed for controlling
the makro state of the game
"""

from enum import Enum
from time import sleep

from kniffel.data_objects.game_kind import EnumGameKind
from kniffel import common
from kniffel.game_logic.controller.game_controller.game_controller import GameController
from kniffel.game_logic.controller.start_menu_controller import StartMenuController
from kniffel.windows.window_manager import WindowManager


class EnumWindowSelected(Enum):
    """
    Enum used for remembering active window
    """
    START_MENU = 1
    GAME_WINDOW = 2


class KniffelController:
    """
    The KniffelController manages the high level Status of the Game
    """

    def __init__(self, window_manager: WindowManager):
        self.window_manager = window_manager
        self.game_controller = GameController(self, window_manager.game_window)
        self.game_controller.load_from_file()
        self.start_menu_controller = StartMenuController(self, window_manager.start_window)
        self.__running = False

        self.active_window = EnumWindowSelected.START_MENU
        window_manager.show_start_menu(self.game_controller.get_game_state())

    def start(self, test: bool):
        """
        Starts the main game loop in here inputs will get handled
        and to the sub windows distributed
        @param test boolean if true loop will be exited after one run
        """

        self.__running = True
        while self.__running:
            if self.active_window is EnumWindowSelected.START_MENU:
                self.start_menu_controller.step_animation()
                self.window_manager.render(self.game_controller.get_game_state())
                self.window_manager.set_no_input_delay(True)
                sleep(common.ANIMATION_DELAY_START_ANIMATION)
            else:
                self.window_manager.set_no_input_delay(False)
            character = self.window_manager.get_ch()
            if character == -1:  # -1 is returned if there was no input
                continue
            self.handle_input(character)
            if test:
                break
        WindowManager.close()
        self.game_controller.save_to_file()

    def handle_input(self, character: chr):
        """
        distributes input to sub windows
        :param character: key pressed
        :return: -
        """
        if self.active_window is EnumWindowSelected.START_MENU:
            self.start_menu_controller.handle_input(character)
        elif self.active_window is EnumWindowSelected.GAME_WINDOW:
            self.game_controller.handle_input(character)

    def show_start_menu(self):
        """
        Show the start menu
        """
        self.window_manager.show_start_menu(self.game_controller.get_game_state())
        self.active_window = EnumWindowSelected.START_MENU

    def continue_game(self):
        """
        resumes the game where it was left off
        """
        self.window_manager.show_game_window(self.game_controller.get_game_state())
        self.game_controller.continue_game()
        self.active_window = EnumWindowSelected.GAME_WINDOW

    def start_classic_game(self):
        """
        Show the Game Window and start the Game
        """
        self.window_manager.show_game_window(self.game_controller.get_game_state())
        self.game_controller.start_new_game(EnumGameKind.GAME_AGAINST_HUMAN)
        self.active_window = EnumWindowSelected.GAME_WINDOW

    def start_bot_game(self):
        """
        Show the Game Window and starts a game against a bot
        """
        self.window_manager.show_game_window(self.game_controller.get_game_state())
        self.game_controller.start_new_game(EnumGameKind.GAME_AGAINST_BOT)
        self.active_window = EnumWindowSelected.GAME_WINDOW

    def exit(self):
        """
        Sets the variable for exiting the main Game Loop
        """
        self.__running = False
