"""
KeyCodes for KeyEvents to simplify code comprehension
"""

# (Behind the # is the Symbol and in the () are all hotkeys to accomplish this integer value too)
VK_NULL_CHAR = 0                    # NUL (Almost every hotkey which is not listed here)
VK_START_OF_HEADING = 1             # SOH (Ctrl+A)
VK_START_OF_TEXT = 2                # STX (Ctrl+B)
VK_END_OF_TEXT = 3                  # ETX (Ctrl+C)
VK_END_OF_TRANSMISSION = 4          # EOT (Ctrl+D)
VK_ENQUIRY = 5                      # ENQ (Ctrl+E)
VK_ACKNOWLEDGMENT = 6               # ACK (Ctrl+F)
VK_BELL = 7                         # BEL (Ctrl+G)
VK_BACKSPACE = 8                    # BS  (Backspace, Ctrl+H)
VK_HORIZONTAL_TAB = 9               # HT  (Tabulator, Ctrl+I)
VK_LINE_FEED = 10                   # LF  (Enter, Ctrl+J, Ctrl+M)
VK_VERTICAL_TAB = 11                # VT  (Ctrl+K)
VK_FORM_FEED = 12                   # FF  (Ctrl+L)
VK_CARRIAGE_RETURN = 13             # CR
VK_SHIFT_OUT = 14                   # SO  (Ctrl+N)
VK_SHIFT_IN = 15                    # SI  (Ctrl+O)
VK_DATA_LINE_ESCAPE = 16            # DLE (Ctrl+P)
VK_DEVICE_CONTROL_1 = 17            # DC1 (Ctrl+Q)
VK_DEVICE_CONTROL_2 = 18            # DC2 (Ctrl+R)
VK_DEVICE_CONTROL_3 = 19            # DC3 (Ctrl+S)
VK_DEVICE_CONTROL_4 = 20            # DC4 (Ctrl+T)
VK_NEGATIVE_ACKNOWLEDGMENT = 21     # NAK (Ctrl+U)
VK_SYNCHRONOUS_IDLE = 22            # SYN (Ctrl+V)
VK_END_OF_TRANSMIT_BLOCK = 23       # ETB (Ctrl+W)
VK_CANCEL = 24                      # CAN (Ctrl+X)
VK_END_OF_MEDIUM = 25               # EM  (Ctrl+Y)
VK_SUBSTITUTE = 26                  # SUB (Ctrl+Z)
VK_ESCAPE = 27                      # ESC (Escape, Ctrl+ß, Ctrl+Ü)
VK_FILE_SEPERATOR = 28              # FS  (Ctrl+#)
VK_GROUP_SEPERATOR = 29             # GS  (Ctrl++)
VK_RECORD_SEPERATOR = 30            # RS  (Ctrl+Shift+6)
VK_UNIT_SEPERATOR = 31              # US  (Ctrl+Shift+-)

VK_SPACE = 32                       # Space
VK_EXCLAMATION_MARK = 33            # ! (Ctrl+Shift+1)
VK_QUOTATION_MARK = 34              # "
VK_NUMBER_SIGN = 35                 # # (Ctrl+Shift+3)
VK_DOLLAR_SIGN = 36                 # $ (Ctrl+Shift+4)
VK_PERCENT_SIGN = 37                # % (Ctrl+Shift+5)
VK_AMPERSAND = 38                   # & (Ctrl+Shift+7)
VK_APOSTROPHE = 39                  # ' (Ctrl+Ä)
VK_BRACKET_OPEN = 40                # ( (Ctrl+Shift+8)
VK_BRACKET_CLOSE = 41               # ) (Ctrl+Shift+V)
VK_ASTERISK = 42                    # * (Ctrl+Shift+9)
VK_PLUS = 43                        # +
VK_COMMA = 44                       # ,
VK_HYPHEN = 45                      # -
VK_PERIOD = 46                      # .
VK_SLASH = 47                       # /

VK_0 = 48                           # 0
VK_1 = 49                           # 1
VK_2 = 50                           # 2
VK_3 = 51                           # 3
VK_4 = 52                           # 4
VK_5 = 53                           # 5
VK_6 = 54                           # 6
VK_7 = 55                           # 7
VK_8 = 56                           # 8
VK_9 = 57                           # 9

VK_COLON = 58                       # :
VK_SEMICOLON = 59                   # ;
VK_LESS_THAN = 60                   # <
VK_EQUALS = 61                      # =
VK_GREATER_THAN = 62                # >
VK_QUESTION_MARK = 63               # ?
VK_AT_SYMBOL = 64                   # @ (Ctrl+Shift+2)

VK_UC_A = 65                        # A
VK_UC_B = 66                        # B
VK_UC_C = 67                        # C
VK_UC_D = 68                        # D
VK_UC_E = 69                        # E
VK_UC_F = 70                        # F
VK_UC_G = 71                        # G
VK_UC_H = 72                        # H
VK_UC_I = 73                        # I
VK_UC_J = 74                        # J
VK_UC_K = 75                        # K
VK_UC_L = 76                        # L
VK_UC_M = 77                        # M
VK_UC_N = 78                        # N
VK_UC_O = 79                        # O
VK_UC_P = 80                        # P
VK_UC_Q = 81                        # Q
VK_UC_R = 82                        # R
VK_UC_S = 83                        # S
VK_UC_T = 84                        # T
VK_UC_U = 85                        # U
VK_UC_V = 86                        # V
VK_UC_W = 87                        # W
VK_UC_X = 88                        # X
VK_UC_Y = 89                        # Y
VK_UC_Z = 90                        # Z

VK_SQUARE_BRACKET_OPEN = 91         # [
VK_BACKSLASH = 92                   # \
VK_SQUARE_BRACKET_CLOSE = 93        # ]
VK_CARET = 94                       # ^
VK_UNDERSCORE = 95                  # _
VK_GRAVE_ACCENT = 96                # `

VK_LC_A = 97                        # a
VK_LC_B = 98                        # b
VK_LC_C = 99                        # c
VK_LC_D = 100                       # d
VK_LC_E = 101                       # e
VK_LC_F = 102                       # f
VK_LC_G = 103                       # g
VK_LC_H = 104                       # h
VK_LC_I = 105                       # i
VK_LC_J = 106                       # j
VK_LC_K = 107                       # k
VK_LC_L = 108                       # l
VK_LC_M = 109                       # m
VK_LC_N = 110                       # n
VK_LC_O = 111                       # o
VK_LC_P = 112                       # p
VK_LC_Q = 113                       # q
VK_LC_R = 114                       # r
VK_LC_S = 115                       # s
VK_LC_T = 116                       # t
VK_LC_U = 117                       # u
VK_LC_V = 118                       # v
VK_LC_W = 119                       # w
VK_LC_X = 120                       # x
VK_LC_Y = 121                       # y
VK_LC_Z = 122                       # z

VK_CURLY_BRACKET_OPEN = 123         # { (Ctrl+Shift+ß)
VK_VERTICAL_BAR = 124               # |
VK_CURLY_BRACKET_CLOSE = 125        # }
VK_TILDE = 126                      # ~

VK_DELETE = 127                     # (Ctrl+Backspace)

VK_SECTION_SIGN = 167               # §

VK_DEGREE = 176                     # °

VK_ACUTE_ACCENT = 180               # ´

VK_LC_MU = 181                      # µ

VK_UC_A_DIAERESIS = 196             # Ä

VK_UC_O_DIAERESIS = 214             # Ö

VK_UC_U_DIAERESIS = 220             # Ü

VK_ESZETT = 223                     # ß

VK_LC_A_DIAERESIS = 228             # ä

VK_LC_O_DIAERESIS = 246             # ö

VK_LC_E_DIAERESIS = 252             # ü

VK_DOWN = 258
VK_UP = 259
VK_LEFT = 260
VK_RIGHT = 261

VK_POS1 = 262

VK_F1 = 265
VK_F2 = 266
VK_F3 = 267
VK_F4 = 268
VK_F5 = 269
VK_F6 = 270
VK_F7 = 271
VK_F8 = 272
VK_F9 = 273
VK_F10 = 274
VK_F11 = 275
VK_F12 = 276

VK_DEL = 330
VK_INS = 331

VK_END = 358

VK_NUMPAD_POS1 = 449
VK_NUMPAD_UP = 450
VK_NUMPAD_SITE_UP = 451
VK_NUMPAD_LEFT = 452
VK_NUMPAD_NOTHING = 453
VK_NUMPAD_RIGHT = 454
VK_NUMPAD_END = 455
VK_NUMPAD_DOWN = 456
VK_NUMPAD_SITE_DOWN = 457

VK_NUMPAD_DIVISOR_SIGN = 458

VK_NUMPAD_ENTER = 459

VK_NUMPAD_DEL = 462

VK_NUMPAD_MULTIPLICATOR_SIGN = 463
VK_NUMPAD_SUBTRACTION_SIGN = 464
VK_NUMPAD_ADDITION_SIGN = 465

VK_NUMPAD_INS = 506

VK_EURO_SIGN = 8364                 # €
