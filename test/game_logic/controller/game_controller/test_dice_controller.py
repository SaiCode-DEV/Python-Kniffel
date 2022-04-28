# pylint: disable=C
import curses

from kniffel import common
from kniffel import key_codes
from kniffel.game_logic.controller.game_controller.dice_controller import *

from unittest import TestCase

from test.mock.mock_dice_window import MockDiceWindow
from test.mock.mock_game_controller import MockGameController


class DiceControllerTest(TestCase):
    def setUp(self):
        self.mock_dice_window = MockDiceWindow()
        self.mock_game_controller = MockGameController()
        self.dice_controller = DiceController(self.mock_dice_window, self.mock_game_controller)
        common.ANIMATION_DELAY_ROLL = 0

    def test_handle_arrow_down(self):
        self.dice_controller.handle_input(curses.KEY_DOWN)
        self.assertEqual(1, self.dice_controller.selected,
                         "After pressing arrow down, second dice should be selected")

    def test_handle_arrow_up(self):
        self.dice_controller.handle_input(curses.KEY_UP)
        self.assertEqual(4, self.dice_controller.selected,
                         "After pressing arrow up 5 dice should be selected ")
        self.dice_controller.handle_input(curses.KEY_UP)
        self.assertEqual(3, self.dice_controller.selected,
                         "After pressing arrow up 4 dice should be selected ")

    def test_handle_roll(self):
        old_dice = self.dice_controller.get_dice_values()
        self.dice_controller.roll(8)
        new_dice = self.dice_controller.get_dice_values()
        for i in range(len(old_dice)):
            if old_dice[i] != new_dice[i]:
                return
        raise AssertionError("Dice should change with re-roll")

    def lock_all_dice(self):
        self.dice_controller.lock_dice(0, True)
        self.dice_controller.lock_dice(1, True)
        self.dice_controller.lock_dice(2, True)
        self.dice_controller.lock_dice(3, True)
        self.dice_controller.lock_dice(4, True)

    def test_handle_lock_roll(self):
        self.lock_all_dice()
        old_dice = self.dice_controller.get_dice_values()
        self.dice_controller.roll(8)
        new_dice = self.dice_controller.get_dice_values()
        self.assertListEqual(old_dice, new_dice,
                             "Locked dice should not be rolled")

    def enter_and_select_next(self):
        self.dice_controller.handle_input(curses.KEY_ENTER)
        self.dice_controller.handle_input(curses.KEY_DOWN)

    def test_lock_functionality(self):
        for i in range(5):
            self.enter_and_select_next()
        for i in range(5):
            self.assertTrue(self.dice_controller.is_locked(i),
                            "Dice should be locked")
        for i in range(5):
            self.enter_and_select_next()
        for i in range(5):
            self.assertFalse(self.dice_controller.is_locked(i),
                             "Dice should not be locked")

    def test_roll_count(self):
        self.dice_controller.reset_roll_count()
        for _ in range(common.MAX_ROLL_COUNT):
            self.dice_controller.handle_input(key_codes.VK_SPACE)
            self.assertIsNone(self.mock_game_controller.message,
                              "no error message should be displayed")
        old_dice = self.dice_controller.get_dice_values()
        self.dice_controller.handle_input(key_codes.VK_SPACE)
        self.assertEqual(common.ERROR_NO_MORE_ROLLS, self.mock_game_controller.message,
                         "Error message should be displayed")
        new_dice = self.dice_controller.get_dice_values()
        self.assertListEqual(old_dice, new_dice,
                             "Dice should not be rolled if roll count is exceeded")
