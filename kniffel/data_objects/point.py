"""
The point module contains the needed classes for storing the
current state of a point
"""


class Point:
    """
    Class Point holds all relevant data of a point object
    """
    def __init__(self):
        self.selected = False
        self.completed = False
        self.value = None
