"""
Here are Functions which take in a Kniffel-Turn-Value aka a List of Five Numbers.
Depending on the function that is called the according value of the corresponding
Field will be returned.
"""

from typing import Dict, List

FULL_HOUSE_VALUE = 25
SMALL_STRAIGHT_VALUE = 30
LARGE_STRAIGHT_VALUE = 40
KNIFFEL_VALUE = 50


class InvalidThrow(Exception):
    """
    Is thrown when a Throw is not plausible meaning a Player tries to cheat
    or something went wrong
    """


def validate_throw(throw: List[int]):
    """
    validate throw will check if the passed throw fits the requirements if not
    a InvalidThrow Exception will be raised
    @raise InvalidThrow if the throw does not fit requirements
    """
    if len(throw) != 5:
        raise InvalidThrow(
            f"A throw has to consist of 5 Dice not: {len(throw)}")
    for dice in throw:
        if dice < 1 or dice > 6:
            raise InvalidThrow(
                "In the passed throw is at "
                f"least one number not between 1 and 6 got {throw}")


def contains_n_dice(count: int, throw: List[int]) -> bool:
    """
    this function counts how often any dice value occurs in a throw and returns true if any count
    is greater or equal to the passed count
    @param count: the number of dices that have to be the same for this function to return true
    @param throw: a List of dice values
    @return: True if the throw contains passed number of same kind, False if not
    """
    counts = get_count_dict(throw)
    for _, value in counts.items():
        if value >= count:
            return True
    return False


def get_count_dict(throw: List[int]) -> Dict[int, int]:
    """
    Counts the number of occurrences of any dice value in a throw
    @param throw: a List of dice values
    @return: a Dict that maps dice values to their occurrences in th throw
    """
    counts = {}
    for dice in throw:
        if dice in counts:
            counts[dice] += 1
        else:
            counts[dice] = 1
    return counts


def get_one_value(throw: List[int]) -> int:
    """
    Sums up all the one's in a throw
    @param throw: a List of dice values
    @return: the Sum of all one's
    @raise InvalidThrow if the throw does not fit requirements
    """
    return get_number_value(1, throw)


def get_two_value(throw: List[int]) -> int:
    """
    Sums up all the two's in a throw
    @param throw: a List of dice values
    @return: the Sum of all two's
    @raise InvalidThrow if the throw does not fit requirements
    """
    return get_number_value(2, throw)


def get_three_value(throw: List[int]) -> int:
    """
    Sums up all the three's in a throw
    @param throw: a List of dice values
    @return: the Sum of all three's
    @raise InvalidThrow if the throw does not fit requirements
    """
    return get_number_value(3, throw)


def get_four_value(throw: List[int]) -> int:
    """
    Sums up all the four's in a throw
    @param throw: a List of dice values
    @return: the Sum of all four's
    @raise InvalidThrow if the throw does not fit requirements
    """
    return get_number_value(4, throw)


def get_five_value(throw: List[int]) -> int:
    """
    Sums up all the five's in a throw
    @param throw: a List of dice values
    @return: the Sum of all five's
    @raise InvalidThrow if the throw does not fit requirements
    """
    return get_number_value(5, throw)


def get_six_value(throw: List[int]) -> int:
    """
    Sums up all the six's in a throw
    @param throw: a List of dice values
    @return: the Sum of all six's
    @raise InvalidThrow if the throw does not fit requirements
    """
    return get_number_value(6, throw)


def get_number_value(dice_value: int, throw: List[int]) -> int:
    """
    Sums up all the dices with the same value as the passed number
    @param dice_value: value of the dices that should be counted
    @param throw: a List of dice values
    @return: the Sum of all dices with the same value as the passed dice_value
    @raise InvalidThrow if the throw does not fit requirements
    """
    validate_throw(throw)
    result = 0
    for dice in throw:
        if dice_value == dice:
            result += dice
    return result


def get_three_of_kind_value(throw: List[int]) -> int:
    """
    Sums up all dice values if there are three dices of the same kind.
    If there are not three of the same kind 0 will be returned
    @param throw: a List of dice values
    @return: Either Sum of all dices or 0
    @raise InvalidThrow if the throw does not fit requirements
    """
    validate_throw(throw)
    result = 0
    for dice in throw:
        result += dice
    if contains_n_dice(3, throw):
        return result
    return 0


def get_four_of_kind_value(throw: List[int]) -> int:
    """
    Sums up all dice values if there are four dices of the same kind.
    If there are not four of the same kind 0 will be returned
    @param throw: a List of dice values
    @return: Either Sum of all dices or 0
    @raise InvalidThrow if the throw does not fit requirements
    """
    validate_throw(throw)
    result = 0
    for dice in throw:
        result += dice
    if contains_n_dice(4, throw):
        return result
    return 0


def get_full_house_value(throw: List[int]) -> int:
    """
    Checks if there are three of one kind and two of another kind.
    If those requirements are fulfilled, the FULL_HOUSE_VALUE is returned otherwise 0
    @param throw: a list of dice values
    @return: FULL_HOUSE_VALUE or 0
    @raise InvalidThrow if the throw does not fit requirements
    """
    validate_throw(throw)
    counts = get_count_dict(throw)
    three, two = False, False
    for _, count in counts.items():
        if count == 2:
            two = True
        if count == 3:
            three = True
    if two and three:
        return FULL_HOUSE_VALUE
    return 0


def count_run(throw: List[int]) -> int:
    """
    Counts the longest sequenz of subsequent numbers in a throw
    @param throw: a list of dice values
    @return: the count of the longest sequenz of numbers in the passed throw (at least one)
    """
    longest_run = 0
    run = 0
    for i in range(1, 7):
        if i in throw:
            run += 1
        else:
            if run > longest_run:
                longest_run = run
                run = 0
    if run > longest_run:
        longest_run = run
    return longest_run


def get_small_straight_value(throw: List[int]) -> int:
    """
    Checks if there are is a sequenz of at least three subsequent numbers if so the value of
    SMALL_STRAIGHT_VALUE is returned otherwise 0
    @param throw: a List of dice values
    @return: SMALL_STRAIGHT_VALUE or 0
    @raise InvalidThrow if the throw does not fit requirements
    """
    validate_throw(throw)
    if count_run(throw) >= 4:
        return SMALL_STRAIGHT_VALUE
    return 0


def get_large_straight_value(throw: List[int]) -> int:
    """
    Checks if there are is a sequenz of at least four subsequent numbers if so the value of
    LARGE_STRAIGHT_VALUE is returned otherwise 0
    @param throw: a List of dice values
    @return: LARGE_STRAIGHT_VALUE or 0
    @raise InvalidThrow if the throw does not fit requirements
    """
    validate_throw(throw)
    if count_run(throw) >= 5:
        return LARGE_STRAIGHT_VALUE
    return 0


def get_kniffel_value(throw: List[int]) -> int:
    """
    Checks if there are 5 dice values of the same kind if so, KNIFFEL_VALUE is returned otherwise 0
    @param throw: a List of dice values
    @return: KNIFFEL_VALUE or 0
    @raise InvalidThrow if the throw does not fit requirements
    """
    validate_throw(throw)
    value = throw[0]
    for dice in throw:
        if dice != value:
            return 0
    return KNIFFEL_VALUE


def get_chance_value(throw: List[int]) -> int:
    """
    Sums up all dice values of a throw
    @param throw: a List of dice values
    @return: Sum of all dice values
    @raise InvalidThrow if the throw does not fit requirements
    """
    validate_throw(throw)
    result = 0
    for dice in throw:
        result += dice
    return result
