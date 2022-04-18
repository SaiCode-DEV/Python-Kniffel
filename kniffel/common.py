import curses

GAME_TITLE = "Kniffel"

LABEL_MANU_PLAY = "(P) Spiel starten"
LABEL_MENU_PLAY_BOT = "(C) Play against computer"
LABEL_MENU_ESCAPE = "(Q) Quit the game"

LABEL_CONTROL_DESCRIPTION_GAME_WINDOW = " | (Q) Spiel Beenden"
LABEL_CONTROL_DESCRIPTION_DICE_SET = " | (TAB) Enter Result | (Space) Roll | (Arrow) Navigate Dice | (Enter) Lock/Unlock Dice |"
LABEL_CONTROL_DESCRIPTION_GAME_CARD = " | (TAB) Roll Dice | (Arrow) Navigate Combinations | (Enter) Lock Result |"
LABEL_CONTROL_DESCRIPTION_RESULT_CARD = " | (TAB) Enter Result | (Space) Roll | (Arrow) Navigate Dice | (Enter) lock/unlock Dice |"

LOGO = [" _  __      _  __  __      _  ",
        "| |/ /_ __ (_)/ _|/ _| ___| | ",
        "| ' /| '_ \| | |_| |_ / _ \ | ",
        "| . \| | | | |  _|  _|  __/ | ",
        "|_|\_\_| |_|_|_| |_|  \___|_| "]

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
    " ! Vieerer     !nur 4er!{}!{}! ",
    " !-------------!-------!-----!-----! ",
    " ! Fünfer      !nur 5er!{}!{}! ",
    " !-------------!-------!-----!-----! ",
    " ! Sechse      !nur 6er!{}!{}! ",
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

# Curses color pairs
COLOR_PAIR_BLUE_BLACK = None

# Settings
COLOR_DICE_LOCKED = None
SELECTED_OPTION = curses.A_REVERSE


def init_colors():
    global COLOR_PAIR_BLUE_BLACK
    global COLOR_DICE_LOCKED
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)

    COLOR_PAIR_BLUE_BLACK = curses.color_pair(1)
    COLOR_DICE_LOCKED = COLOR_PAIR_BLUE_BLACK
