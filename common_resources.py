one = ["┌───────┐",
       "│       │",
       "│   ¤   │",
       "│       │",
       "└───────┘"]
two = ["┌───────┐",
       "│ ¤     │",
       "│       │",
       "│     ¤ │",
       "└───────┘"]
three = ["┌───────┐",
         "│ ¤     │",
         "│   ¤   │",
         "│     ¤ │",
         "└───────┘"]
four = ["┌───────┐",
        "│ ¤   ¤ │",
        "│       │",
        "│ ¤   ¤ │",
        "└───────┘"]
five = ["┌───────┐",
        "│ ¤   ¤ │",
        "│   ¤   │",
        "│ ¤   ¤ │",
        "└───────┘"]
six = ["┌───────┐",
       "│ ¤   ¤ │",
       "│ ¤   ¤ │",
       "│ ¤   ¤ │",
       "└───────┘"]

DICE_STR_LEN = len(one[0])
DICE_ARRAY_LEN = len(one)

title = [" _  __      _  __  __      _  ",
         "| |/ /_ __ (_)/ _|/ _| ___| | ",
         "| ' /| '_ \| | |_| |_ / _ \ | ",
         "| . \| | | | |  _|  _|  __/ | ",
         "|_|\_\_| |_|_|_| |_|  \___|_| "]

TITLE_STR_LEN = len(title[0])
TITLE_ARRAY_LEN = len(title)

start_menu = [" 1 Player start (F1) ", " 2 Player start (F2) ", " Exit (Esc) "]

STATUS_BAR_STR = " Press 'F1' to 1 Player start | Press 'F2' to 2 Player start | Press 'Esc' to exit | Press '←' to back to Menu |"

PLAYER_CARD = ["                                                           ",
               "                           Player 1                        ",
               "                                                           ",
               "┌─────────────┬───────┬┬───────┬────────┬────────┬────────┐",
               "│ Einser      │nur 1er││       │        │        │        │",
               "├─────────────┼───────┤├───────┼────────┼────────┼────────┤",
               "│ Zweier      │nur 2er││       │        │        │        │",
               "├─────────────┼───────┤├───────┼────────┼────────┼────────┤",
               "│ Dreier      │nur 3er││       │        │        │        │",
               "├─────────────┼───────┤├───────┼────────┼────────┼────────┤",
               "│ Vieerer     │nur 4er││       │        │        │        │",
               "├─────────────┼───────┤├───────┼────────┼────────┼────────┤",
               "│ Fünfer      │nur 5er││       │        │        │        │",
               "├─────────────┼───────┤├───────┼────────┼────────┼────────┤",
               "│ Sechser     │nur 6er││       │        │        │        │",
               "├─────────────┴───────┘└───────┴────────┴────────┴────────┤",
               "├─────────────┬───────┐┌───────┬────────┬────────┬────────┤",
               "│ Gesamt      │   →   ││   0   │        │        │        │",
               "├─────────────┼───────┤├───────┼────────┼────────┼────────┤",
               "│ bei >=63    │  +35  ││   0   │        │        │        │",
               "├─────────────┼───────┤├───────┼────────┼────────┼────────┤",
               "│Gesamt o.Teil│   →   ││   0   │        │        │        │",
               "├─────────────┴───────┘└───────┴────────┴────────┴────────┤",
               "├─────────────┬───────┐┌───────┬────────┬────────┬────────┤",
               "│ Dreierpasch │  alle ││       │        │        │        │",
               "├─────────────┼───────┤├───────┼────────┼────────┼────────┤",
               "│ Viererpasch │  alle ││       │        │        │        │",
               "├─────────────┼───────┤├───────┼────────┼────────┼────────┤",
               "│ Full-House  │  +25  ││       │        │        │        │",
               "├─────────────┼───────┤├───────┼────────┼────────┼────────┤",
               "│ K.Straße    │  +30  ││       │        │        │        │",
               "├─────────────┼───────┤├───────┼────────┼────────┼────────┤",
               "│ G.Straße    │  +40  ││       │        │        │        │",
               "├─────────────┼───────┤├───────┼────────┼────────┼────────┤",
               "│ Kniffel     │  +50  ││       │        │        │        │",
               "├─────────────┼───────┤├───────┼────────┼────────┼────────┤",
               "│ Chance      │  alle ││       │        │        │        │",
               "├─────────────┴───────┘└───────┴────────┴────────┴────────┤",
               "├─────────────┬───────┐┌───────┬────────┬────────┬────────┤",
               "│Gesamt u.Teil│   →   ││   0   │        │        │        │",
               "├─────────────┼───────┤├───────┼────────┼────────┼────────┤",
               "│Gesamt o.Teil│   →   ││   0   │        │        │        │",
               "├─────────────┼───────┤├───────┼────────┼────────┼────────┤",
               "│Extra-Kniffel│   →   ││   0   │        │        │        │",
               "├─────────────┼───────┤├───────┼────────┼────────┼────────┤",
               "│ Endsumme    │   →   ││   0   │        │        │        │",
               "└─────────────┴───────┴┴───────┴────────┴────────┴────────┘"]
PLAYER_CARD_STR_LEN = len(PLAYER_CARD[0])
PLAYER_CARD_ARRAY_LEN = len(PLAYER_CARD)
