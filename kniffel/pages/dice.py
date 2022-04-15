import random
import curses
from curses import wrapper

DICE_FACES = [
    ["       ", "   ¤   ", "       "],
    [" ¤     ", "       ", "     ¤ "],
    [" ¤     ", "   ¤   ", "     ¤ "],
    [" ¤   ¤ ", "       ", " ¤   ¤ "],
    [" ¤   ¤ ", "   ¤   ", " ¤   ¤ "],
    [" ¤   ¤ ", " ¤   ¤ ", " ¤   ¤ "]
]

DICE_BORDER = ["┌───────┐", "│       │", "│       │", "│       │", "└───────┘"]
DICE_COUNT = 5
GAP_SIZE = 2


class Dice:
    def __init__(self):
        self.__value = random.randint(1, 6)
        self.selected = False
        self.locked = False

    @property
    def value(self):
        return self.__value

    def roll(self):
        self.__value = random.randint(1, 6)
        self.show()

    def show(self, std_scr):
        y, x = std_scr.getyx()
        max_y, max_x = std_scr.getmaxyx()
        if x + len(DICE_BORDER[0]) > max_x:
            print("Failed to draw dice X position to high")
            return
        if y + len(DICE_BORDER) > max_y:
            print("Failed to draw dice Y position to high")
            return
        if self.locked:
            self.draw_border(std_scr)
        std_scr.move(y + 1, x + 1)
        self.draw_face(std_scr)

    def draw_border(self, std_scr):
        y, x = std_scr.getyx()
        for i in range(len(DICE_BORDER)):
            if self.selected:
                std_scr.addstr(y + i, x, DICE_BORDER[i], curses.A_REVERSE)
            else:
                std_scr.addstr(y + i, x, DICE_BORDER[i])

    def draw_face(self, std_scr):
        y, x = std_scr.getyx()
        dice_face = DICE_FACES[self.__value - 1]
        for i in range(len(dice_face)):
            if self.selected:
                std_scr.addstr(y + i, x, dice_face[i], curses.A_REVERSE)
            else:
                std_scr.addstr(y + i, x, dice_face[i])


def render(std_scr, dice):
    std_scr.clear()
    max_y, max_x = std_scr.getmaxyx()
    off_left = (max_x - (DICE_COUNT * (len(DICE_BORDER[0]) + GAP_SIZE))) // 2
    dice_y = (max_y - len(DICE_BORDER)) // 2
    for i in range(DICE_COUNT):
        dice_x = off_left + i * (len(DICE_BORDER[0]) + GAP_SIZE)
        std_scr.move(dice_y, dice_x)
        dice[i].show(std_scr)
        std_scr.refresh()


def main(std_scr):
    curses.curs_set(0)  # hide cursor
    std_scr.keypad(True)  # to be able to compare input wit curses constants
    curses.cbreak()  # no input buffering
    curses.noecho()
    curses.mousemask(1)

    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)

    dice = []
    for i in range(DICE_COUNT):
        dice.append(Dice())

    selected = 0
    dice[selected].selected = True
    render(std_scr, dice)

    while True:
        ch = std_scr.getch()
        if ch == curses.KEY_MOUSE:
            _, mx, my, _, _ = curses.getmouse()
            y, x = std_scr.getyx()
            std_scr.addstr(y, x, std_scr.instr(my, mx, 5))
        if ch == curses.KEY_RIGHT:
            dice[selected].selected = False
            selected = (selected + 1) % len(dice)
            dice[selected].selected = True
        if ch == curses.KEY_LEFT:
            dice[selected].selected = False
            selected -= 1
            if selected < 0:
                selected = len(dice) - 1
            dice[selected].selected = True
        # 10/13 are added to catch enter from numeric keyboard
        if ch == curses.KEY_ENTER or ch == 10 or ch == 13:
            dice[selected].locked = dice[selected].locked ^ 1

        render(std_scr, dice)


if __name__ == "__main__":
    wrapper(main)
