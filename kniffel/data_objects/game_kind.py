"""
The game_kind module contains the data-objects for dealing
with what kind of game is played
"""
from enum import Enum


class EnumGameKind(Enum):
    """
    EnumGameKind-class contains enumerations for
    the different kind of games that can be played
    """
    GAME_AGAINST_HUMAN = 1
    GAME_AGAINST_BOT = 2
