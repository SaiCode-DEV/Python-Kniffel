"""
The common module is supposed to contain all commonly used attributes and
all strings which get displayed to the user
"""

from os import path
import curses
import kniffel

GAME_TITLE = "Kniffel"

LABEL_MANU_CONTINUE = "(C) Spiel fortführen"
LABEL_MANU_PLAY = "(N) Neues Spiel starten"
LABEL_MENU_PLAY_BOT = "(P) Neues Spiel gegen Computer starten"
LABEL_MENU_ESCAPE = "(Q) Spiel beenden"

LABEL_PLAYER_TURN = "Spieler Nummer {} ist am Zug"

LABEL_CONTROL_DESCRIPTION_GAME_WINDOW = " | (Q) Start Menu"
LABEL_CONTROL_DESCRIPTION_DICE_SET = " | (TAB) Ergebnis eintragen | (Space) Würfeln " \
                                     "| (Pfeiltasten) Würfel navigieren | (Enter) Würfel ent-/sperren |"
LABEL_CONTROL_DESCRIPTION_GAME_CARD = " | (TAB) Weiter würfeln | (Pfeiltasten) Kombinationen navigieren |" \
                                      " (Enter) Ergebnis eintragen |"
LABEL_CONTROL_DESCRIPTION_RESULT_CARD = " |"

ERROR_COMBINATION_ALREADY_DONE = "In dieses Feld können Sie nichts mehr eintragen"
ERROR_NO_MORE_ROLLS = "Leider dürfen Sie in diesem Zug keine weiteren Würfe mehr tätigen"
GAME_OVER = "GAME OVER"

DICE_COUNT = 5
PLAYER_COUNT = 2
MAX_ROLL_COUNT = 3  # Number of rolls a player can roll in one turn
ANIMATION_DELAY_START_ANIMATION = 0.175
ANIMATION_DELAY_ROLL = 0.15
BOT_DECISION_DELAY = 1  # number of seconds the bots decision is displayed
ROLL_COUNT_ANIMATION = 8

POINTS_STR_LEN = 5
COMBINATIONS_COUNT = 13

TRACE_OUTPUT = False

DIR_PERSISTENCE = kniffel.__file__.replace("__init__.py", "") + "persistence"
FILE_GAME_STATE = path.join(DIR_PERSISTENCE, "game_state.json")

LOGO = [" _  __      _  __  __      _  ",
        "| |/ /_ __ (_)/ _|/ _| ___| | ",
        "| ' /| '_ \\| | |_| |_ / _ \\ | ",
        "| . \\| | | | |  _|  _|  __/ | ",
        "|_|\\_\\_| |_|_|_| |_|  \\___|_| "]

NAME_PAD = [
    "                                   ",
    "              Kniffel              ",
    "                                   "
]

GAME_PAD = [
    "-----------------------------------",
    "! Einser      !nur 1er!",
    "!-------------!-------!",
    "! Zweier      !nur 2er!",
    "!-------------!-------!",
    "! Dreier      !nur 3er!",
    "!-------------!-------!",
    "! Vierer      !nur 4er!",
    "!-------------!-------!",
    "! Fünfer      !nur 5er!",
    "!-------------!-------!",
    "! Sechser     !nur 6er!",
    "!-------------!-------!",
    "! Dreierpasch !  alle !",
    "!-------------!-------!",
    "! Viererpasch !  alle !",
    "!-------------!-------!",
    "! Full-House  !  +25  !",
    "!-------------!-------!",
    "! K.Straße    !  +30  !",
    "!-------------!-------!",
    "! G.Straße    !  +40  !",
    "!-------------!-------!",
    "! Kniffel     !  +50  !",
    "!-------------!-------!",
    "! Chance      !  alle !",
    "-----------------------------------"
]

POINTS_PAD = [
    "{}",
    "-----",
    "{}",
    "-----",
    "{}",
    "-----",
    "{}",
    "-----",
    "{}",
    "-----",
    "{}",
    "-----",
    "{}",
    "-----",
    "{}",
    "-----",
    "{}",
    "-----",
    "{}",
    "-----",
    "{}",
    "-----",
    "{}",
    "-----",
    "{}"
]

RESULT_PAD = [
    "-----------------------------------",
    "! Oberer Teil !   →   !",
    "!-------------!-------!",
    "! bei >=63    !  +35  !",
    "!-------------!-------!",
    "!Gesamt o.Teil!   →   !",
    "!-------------!-------!",
    "! Endsumme    !   →   !",
    "-----------------------------------"
]

RESULT_POINTS_PAD = [
    "{}",
    "-----",
    "{}",
    "-----",
    "{}",
    "-----",
    "{}"
]

SEPARATOR = "!"

loading01 = [" _ ",
             "| |",
             "| '",
             "| .",
             "|_|"]

loading02 = [" _  _",
             "| |/ ",
             "| ' /",
             "| . \\",
             "|_|\\_"]

loading03 = [" _  __ ",
             "| |/ /_ ",
             "| ' /| '",
             "| . \\| |",
             "|_|\\_\\_|"]

loading04 = [" _  __    ",
             "| |/ /_ __",
             "| ' /| '_ ",
             "| . \\| | |",
             "|_|\\_\\_| |"]

loading05 = [" _  __     ",
             "| |/ /_ __  ",
             "| ' /| '_ \\",
             "| . \\| | | |",
             "|_|\\_\\_| |_|"]

loading06 = [" _  __      _ ",
             "| |/ /_ __ (_)",
             "| ' /| '_ \\| |",
             "| . \\| | | | |",
             "|_|\\_\\_| |_|_|"]

loading07 = [" _  __      _  _",
             "| |/ /_ __ (_)/ ",
             "| ' /| '_ \\| | |",
             "| . \\| | | | |  ",
             "|_|\\_\\_| |_|_|_|"]

loading08 = [" _  __      _  __",
             "| |/ /_ __ (_)/ _",
             "| ' /| '_ \\| | |_",
             "| . \\| | | | |  _",
             "|_|\\_\\_| |_|_|_| "]

loading09 = [" _  __      _  __  _",
             "| |/ /_ __ (_)/ _|/ ",
             "| ' /| '_ \\| | |_| |",
             "| . \\| | | | |  _|  ",
             "|_|\\_\\_| |_|_|_| |_|"]

loading10 = [" _  __      _  __  __ ",
             "| |/ /_ __ (_)/ _|/ _|",
             "| ' /| '_ \\| | |_| |_ ",
             "| . \\| | | | |  _|  _|",
             "|_|\\_\\_| |_|_|_| |_|  "]

loading11 = [" _  __      _  __  __   ",
             "| |/ /_ __ (_)/ _|/ _| _",
             "| ' /| '_ \\| | |_| |_ / ",
             "| . \\| | | | |  _|  _|  ",
             "|_|\\_\\_| |_|_|_| |_|  \\_"]

loading12 = [" _  __      _  __  __    ",
             "| |/ /_ __ (_)/ _|/ _| __",
             "| ' /| '_ \\| | |_| |_ / _",
             "| . \\| | | | |  _|  _|  _",
             "|_|\\_\\_| |_|_|_| |_|  \\__"]

loading13 = [" _  __      _  __  __     ",
             "| |/ /_ __ (_)/ _|/ _| ___",
             "| ' /| '_ \\| | |_| |_ / _ \\",
             "| . \\| | | | |  _|  _|  __/",
             "|_|\\_\\_| |_|_|_| |_|  \\___|"]

LOADING = [loading01, loading02,
           loading03, loading04,
           loading05, loading06,
           loading07, loading08,
           loading09, loading10,
           loading11, loading12,
           loading13]

# Curses color pairs
COLOR_PAIR_BLUE_BLACK = 1
COLOR_PAIR_BLACK_WHITE = 2
COLOR_PAIR_BLACK_CYAN = 3
COLOR_DICE_LOCKED = 1
SELECTED_OPTION = curses.A_REVERSE


def init_colors():
    """
    Init the commonly used colors
    @return:
    """
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_CYAN)
