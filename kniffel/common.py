import curses

GAME_TITLE = "Kniffel"

GAME_PAD = [
            " ┌─────────────┬───────┐┌─────┬─────┐ ",
            " │ Einser      │nur 1er││{}│{}│ ",
            " ├─────────────┼───────┤├─────┼─────┤ ",
            " │ Zweier      │nur 2er││{}│{}│ ",
            " ├─────────────┼───────┤├─────┼─────┤ ",
            " │ Dreier      │nur 3er││{}│{}│ ",
            " ├─────────────┼───────┤├─────┼─────┤ ",
            " │ Vieerer     │nur 4er││{}│{}│ ",
            " ├─────────────┼───────┤├─────┼─────┤ ",
            " │ Fünfer      │nur 5er││{}│{}│ ",
            " ├─────────────┼───────┤├─────┼─────┤ ",
            " │ Sechse      │nur 6er││{}│{}│ ",
            " └─────────────┴───────┘└─────┴─────┘ ",
            " ┌─────────────┬───────┐┌─────┬─────┐ ",
            " │ Dreierpasch │  alle ││{}│{}│ ",
            " ├─────────────┼───────┤├─────┼─────┤ ",
            " │ Viererpasch │  alle ││{}│{}│ ",
            " ├─────────────┼───────┤├─────┼─────┤ ",
            " │ Full-House  │  +25  ││{}│{}│ ",
            " ├─────────────┼───────┤├─────┼─────┤ ",
            " │ K.Straße    │  +30  ││{}│{}│ ",
            " ├─────────────┼───────┤├─────┼─────┤ ",
            " │ G.Straße    │  +40  ││{}│{}│ ",
            " ├─────────────┼───────┤├─────┼─────┤ ",
            " │ Kniffel     │  +50  ││{}│{}│ ",
            " ├─────────────┼───────┤├─────┼─────┤ ",
            " │ Chance      │  alle ││{}│{}│ ",
            " └─────────────┴───────┘└─────┴─────┘ "
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
