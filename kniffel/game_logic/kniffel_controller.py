from enum import Enum

from game_logic.game_controller import GameController
from game_logic.start_menu_controller import StartMenuController
from windows.window_manager import WindowManager


class EnumWindowSelected(Enum):
    """
    Enum used for remembering active window
    """
    START_MENU = 1
    GAME_WINDOW = 2


class KniffelController:
    def __init__(self, window_manager: WindowManager):
        self.window_manager = window_manager
        self.game_controller = GameController(self, window_manager.game_window)
        self.start_menu_controller = StartMenuController(self)
        self.__running = False

        self.active_window = EnumWindowSelected.START_MENU
        window_manager.show_start_menu(self.game_controller.get_game_state())

    def start(self):
        """
        Starts the main game loop in here inputs will get handled
        and to the subwindows distributed
        """

        self.__running = True
        while self.__running:
            ch = self.window_manager.get_ch()
            if self.active_window is EnumWindowSelected.START_MENU:
                self.start_menu_controller.handle_input(ch)
            elif self.active_window is EnumWindowSelected.GAME_WINDOW:
                self.game_controller.handle_input(ch)
        WindowManager.close()

    def start_classic_game(self):
        self.window_manager.show_game_window(self.game_controller.get_game_state())
        self.active_window = EnumWindowSelected.GAME_WINDOW

    def start_bot_game(self):
        pass

    def stop_game(self):
        self.__running = False
