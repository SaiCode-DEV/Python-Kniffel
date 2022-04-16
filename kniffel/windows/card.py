import curses
from kniffel import common


class Card:
    def __init__(self, points: int = 0):
        self.__points = points

    @staticmethod
    def get_required_size():
        return [len(common.GAME_PAD), len(common.GAME_PAD[0])]

    def get_created_points_str(self):
        points_to_add = self.__points

        if points_to_add == 0:
            points_to_add = " "

        attachment = " " * ((5 - len(str(points_to_add))) // 2)
        ending = " " * (5 - len(str(points_to_add)) - len(attachment))

        return attachment + str(points_to_add) + ending

    def show(self, window: curses.window):
        curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)
        card_width = len(common.GAME_PAD[0])

        attachment = " " * (card_width // 2 - len(common.GAME_TITLE) // 2)
        ending = " " * (card_width - len(common.GAME_TITLE) - len(attachment))
        name_str = attachment + common.GAME_TITLE + ending

        line_count = 0
        for line in common.GAME_PAD:
            str_to_add = line.format(self.get_created_points_str(), self.get_created_points_str())
            window.addstr(line_count, 0, str_to_add, curses.color_pair(4))
            line_count += 1

        window.addstr(1, 0, name_str, curses.color_pair(4))
        window.refresh()
