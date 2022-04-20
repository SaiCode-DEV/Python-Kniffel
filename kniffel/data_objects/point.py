from kniffel.data_objects.combinations import Combinations

points = {
    Combinations.ONES: "",
    Combinations.TWOS: "",
    Combinations.THREES: "",
    Combinations.FOURS: "",
    Combinations.FIVES: "",
    Combinations.SIXES: "",

    Combinations.THREE_OF_KIND: "",
    Combinations.FOUR_OF_KIND: "",
    Combinations.FULL_HOUSE: "",
    Combinations.SMALL_STRAIGHT: "",
    Combinations.LARGE_STRAIGHT: "",
    Combinations.KNIFFEL: "",
    Combinations.CHANCE: ""
}


class Point:
    def __init__(self):
        self.selected = False
        self.completed = False
        self.value = 0
        self.position = 0

        self.__points = []

    def save_value(self, value: int, position: int):
        self.__points[position] = value

    @property
    def points(self):
        return self.__points

    def add_points(self, value: str, art: Combinations):
        self.__points[art] = value
