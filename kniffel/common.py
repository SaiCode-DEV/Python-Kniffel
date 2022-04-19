"""
The common module is supposed to contain all commonly used attributes and
all strings which get displayed to the user
"""

import curses

GAME_TITLE = "Kniffel"

LABEL_MANU_PLAY = "(P) Spiel starten"
LABEL_MENU_PLAY_BOT = "(C) Play against computer"
LABEL_MENU_ESCAPE = "(Q) Quit the game"

LABEL_CONTROL_DESCRIPTION_GAME_WINDOW = " | (Q) Spiel Beenden"
LABEL_CONTROL_DESCRIPTION_DICE_SET = " | (TAB) Enter Result | (Space) Roll " \
                                     "| (Arrow) Navigate Dice | (Enter) Lock/Unlock Dice |"
LABEL_CONTROL_DESCRIPTION_GAME_CARD = " | (TAB) Roll Dice | (Arrow) Navigate Combinations |" \
                                      " (Enter) Lock Result |"
LABEL_CONTROL_DESCRIPTION_RESULT_CARD = " | (TAB) Enter Result | (Space) Roll |" \
                                        " (Arrow) Navigate Dice | (Enter) lock/unlock Dice |"

ERROR_COMBINATION_ALREADY_DONE = "In dieses Feld können Sie nichts mehr eintragen"
ERROR_NO_MORE_ROLLS = "Leider dürfen Sie in diesem Zug keine weiteren Würfe mehr tätigen"

DICE_COUNT = 5
PLAYER_COUNT = 2
MAX_ROLL_COUNT = 2  # Number of rolls a player can roll in one turn
ANIMATION_DELAY = 0.175

LOGO = [" _  __      _  __  __      _  ",
        "| |/ /_ __ (_)/ _|/ _| ___| | ",
        "| ' /| '_ \\| | |_| |_ / _ \\ | ",
        "| . \\| | | | |  _|  _|  __/ | ",
        "|_|\\_\\_| |_|_|_| |_|  \\___|_| "]

GAME_PAD = [
    "                                     ",
    "                                     ",
    "                                     ",
    " ----------------------------------- ",
    " ! Einser      !nur 1er!{}!{}! ",
    " !-------------!-------!-----!-----! ",
    " ! Zweier      !nur 2er!{}!{}! ",
    " !-------------!-------!-----!-----! ",
    " ! Dreier      !nur 3er!{}!{}! ",
    " !-------------!-------!-----!-----! ",
    " ! Vierer      !nur 4er!{}!{}! ",
    " !-------------!-------!-----!-----! ",
    " ! Fünfer      !nur 5er!{}!{}! ",
    " !-------------!-------!-----!-----! ",
    " ! Sechser     !nur 6er!{}!{}! ",
    " ----------------------------------- ",
    " ----------------------------------- ",
    " ! Dreierpasch !  alle !{}!{}! ",
    " !-------------!-------!-----!-----! ",
    " ! Viererpasch !  alle !{}!{}! ",
    " !-------------!-------!-----!-----! ",
    " ! Full-House  !  +25  !{}!{}! ",
    " !-------------!-------!-----!-----! ",
    " ! K.Straße    !  +30  !{}!{}! ",
    " !-------------!-------!-----!-----! ",
    " ! G.Straße    !  +40  !{}!{}! ",
    " !-------------!-------!-----!-----! ",
    " ! Kniffel     !  +50  !{}!{}! ",
    " !-------------!-------!-----!-----! ",
    " ! Chance      !  alle !{}!{}! ",
    " ----------------------------------- "
]

RESULT_PAD = [
    " ------------------------------------------ ",
    " ! Oberer Teil  !   →   !{}!{}! ",
    " !--------------!-------!-----!-----!-----! ",
    " ! bei >=63     !  +35  !{}!{}! ",
    " !--------------!-------!-----!-----!-----! ",
    " ! Gesamt o.Teil!   →   !{}!{}! ",
    " !--------------!-------!-----!-----!-----! ",
    " ! Endsumme     !   →   !{}!{}! ",
    " ------------------------------------------ ",
]

loading01 = [" _ ",
             "| |",
             "| '",
             "| .",
             "|_|"]

loading02 = [" _  _",
             "| |/ ",
             "| ' /",
             "| . \\",
             "|_|\_"]

loading03 = [" _  __ ",
             "| |/ /_ ",
             "| ' /| '",
             "| . \| |",
             "|_|\_\_|"]

loading04 = [" _  __    ",
             "| |/ /_ __",
             "| ' /| '_ ",
             "| . \| | |",
             "|_|\_\_| |"]

loading05 = [" _  __     ",
             "| |/ /_ __  ",
             "| ' /| '_ \\",
             "| . \| | | |",
             "|_|\_\_| |_|"]

loading06 = [" _  __      _ ",
             "| |/ /_ __ (_)",
             "| ' /| '_ \| |",
             "| . \| | | | |",
             "|_|\_\_| |_|_|"]

loading07 = [" _  __      _  _",
             "| |/ /_ __ (_)/ ",
             "| ' /| '_ \| | |",
             "| . \| | | | |  ",
             "|_|\_\_| |_|_|_|"]

loading08 = [" _  __      _  __",
             "| |/ /_ __ (_)/ _",
             "| ' /| '_ \| | |_",
             "| . \| | | | |  _",
             "|_|\_\_| |_|_|_| "]

loading09 = [" _  __      _  __  _",
             "| |/ /_ __ (_)/ _|/ ",
             "| ' /| '_ \| | |_| |",
             "| . \| | | | |  _|  ",
             "|_|\_\_| |_|_|_| |_|"]

loading10 = [" _  __      _  __  __ ",
             "| |/ /_ __ (_)/ _|/ _|",
             "| ' /| '_ \| | |_| |_ ",
             "| . \| | | | |  _|  _|",
             "|_|\_\_| |_|_|_| |_|  "]

loading11 = [" _  __      _  __  __   ",
             "| |/ /_ __ (_)/ _|/ _| _",
             "| ' /| '_ \| | |_| |_ / ",
             "| . \| | | | |  _|  _|  ",
             "|_|\_\_| |_|_|_| |_|  \_"]

loading12 = [" _  __      _  __  __    ",
             "| |/ /_ __ (_)/ _|/ _| __",
             "| ' /| '_ \| | |_| |_ / _",
             "| . \| | | | |  _|  _|  _",
             "|_|\_\_| |_|_|_| |_|  \__"]

loading13 = [" _  __      _  __  __     ",
             "| |/ /_ __ (_)/ _|/ _| ___",
             "| ' /| '_ \| | |_| |_ / _ \\",
             "| . \| | | | |  _|  _|  __/",
             "|_|\_\_| |_|_|_| |_|  \___|"]

LOADING = [loading01, loading02, loading03, loading04, loading05, loading06, loading07, loading08, loading09, loading10, loading11, loading12, loading13]

# Curses color pairs
COLOR_PAIR_BLUE_BLACK = None

# Settings
COLOR_DICE_LOCKED = None
SELECTED_OPTION = curses.A_REVERSE


def init_colors():
    """
    Init the commonly used colors
    Has to be done in an extra function because curses.initscr has to be
    called before colors get initialized
    @return:
    """
    global COLOR_PAIR_BLUE_BLACK
    global COLOR_DICE_LOCKED
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)

    COLOR_PAIR_BLUE_BLACK = curses.color_pair(1)
    COLOR_DICE_LOCKED = COLOR_PAIR_BLUE_BLACK
