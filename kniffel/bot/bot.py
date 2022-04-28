"""A bot that fights against the human player and ALWAYS wins.
    It uses maths and simple logic to decide what to do.
    Inspired by:
    https://brefeld.homepage.t-online.de/kniffel.html
    """

from typing import Tuple

import numpy as np
from numpy import asarray as ar, number
from kniffel.data_objects.combinations import Combinations
from kniffel.game_logic.value_calculator import get_one_value, get_two_value, get_three_value, get_four_value,\
    get_five_value, get_six_value, get_three_of_kind_value, get_four_of_kind_value, get_full_house_value,\
    get_small_straight_value, get_large_straight_value, get_kniffel_value, get_chance_value

POSSIBLE = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "three_of_a_kind": 3,
    "four_of_a_kind": 4,
    "full_house": 25,
    "small_straight": 30,
    "large_straight": 40,
    "yahtzee": 50,
    "chance": 0}


def get_best_choice(dice_rolled: list[number], available_combinations) -> dict:
    """Return the best choice on a simple logic basis.

    Args:
        gewuerfelt (list): The numbers the dice rolled.
        available (list): A list of all still available options to choose from.

    Returns:
        dict: what dices should be rerolled or what option the bot chose.
    """
    generate = []
    if len(available_combinations) == 0:
        return {}
    for combination in available_combinations:
        # calculate the value of the throw
        match combination.value:
            case Combinations.ONES.value:
                generate.append(get_one_value(dice_rolled) / 1 * 5 + 1)
            case Combinations.TWOS.value:
                generate.append(get_two_value(dice_rolled) / 2 * 5 + 2)
            case Combinations.THREES.value:
                generate.append(get_three_value(dice_rolled) / 3 * 5 + 3)
            case Combinations.FOURS.value:
                generate.append(get_four_value(dice_rolled) / 4 * 5 + 4)
            case Combinations.FIVES.value:
                generate.append(get_five_value(dice_rolled) / 5 * 5 + 5)
            case Combinations.SIXES.value:
                generate.append(get_six_value(dice_rolled) / 6 * 5 + 6)
            case Combinations.THREE_OF_KIND.value:
                generate.append(get_three_of_kind_value(dice_rolled))
            case Combinations.FOUR_OF_KIND.value:
                generate.append(get_four_of_kind_value(dice_rolled))
            case Combinations.FULL_HOUSE.value:
                generate.append(get_full_house_value(dice_rolled))
            case Combinations.SMALL_STRAIGHT.value:
                generate.append(get_small_straight_value(dice_rolled))
            case Combinations.LARGE_STRAIGHT.value:
                generate.append(get_large_straight_value(dice_rolled))
            case Combinations.KNIFFEL.value:
                generate.append(get_kniffel_value(dice_rolled))
            case Combinations.CHANCE.value:
                # to make it less interesting
                generate.append(get_chance_value(dice_rolled) - 10)

    if len(generate) == len(available_combinations):
        possible = dict(zip(available_combinations, generate))
        # sort out all the impossible / useless combinations
        possible = {a: b for a, b in possible.items() if b != 0}
        # print(possible)
        # get the highest value
        return dict(sorted(possible.items(), key=lambda x: x[1], reverse=True))
    else:
        return {}


def reroll_controller(dice_rolled, available_combinations):
    """Choose the cubes to reroll.

    Args:
        dice_rolled (list): The numbers the dice rolled.
        available (list): A list of all still available options to choose from.

    Returns:
        list: The cubes to reroll.
    """
    # try out each possible dice combination
    dices = []
    for dice in range(6):
        dices.append(sorted([dice + 1] + dice_rolled[1:], reverse=True))
        dices.append(
            sorted(dice_rolled[:1] + [dice + 1] + dice_rolled[2:], reverse=True))
        dices.append(
            sorted(dice_rolled[:2] + [dice + 1] + dice_rolled[3:], reverse=True))
        dices.append(
            sorted(dice_rolled[:3] + [dice + 1] + dice_rolled[4:], reverse=True))
        dices.append(sorted(dice_rolled[:4] + [dice + 1], reverse=True))
    #print(f"orginal: {dice_rolled}\n")
    # print(dices)
    dices = list(set({tuple(i) for i in dices}))
    dices = sorted([list(i) for i in dices])
    output_points = []
    for dice in dices:
        output_points.append(get_best_choice(dice, available_combinations))
    output_points, dices = zip(*sorted(zip(output_points, dices),
                                       key=lambda x: x[0].get(next(iter(x[0])), 0), reverse=True))
    max_points = max([i.get(next(iter(i)), 0) for i in output_points])
    different = []
    for option, dice in zip(output_points, dices):
        if option.get(next(iter(option)), 0) == max_points:
            # print(f"{dice} | {next(iter(option))} is the best with {option.get(next(iter(option)))} points")
            different.append(dice)
    changed_dices = [False, False, False, False, False]
    for difference in different:
        changed_dices = ar(np.array(difference) != np.array(
            dice)) | ar(changed_dices)
    return changed_dices

    # get the elements with the highest value


def bot_controller(dice: list[int],
                   available_combinations,
                   rerolls_left=0) -> Tuple[bool,
                                            Combinations]:
    """The main bot controller

    Args:
        gewuerfelt (list[int]): The numbers the dice have rolled.
        available (list[str]): What options are still available to choose from.
        left_rerolls (int, optional): How many Rerolls are left 0 = none. Defaults to 0.

    Returns:
        str: The option the bot chose.
    """
    # sort the dices by value
    dice_sorted = sorted(dice, reverse=True)
    # print(dice_sorted)
    best_now = get_best_choice(dice_sorted, available_combinations)
    # print(best_now)
    if best_now.get(Combinations.KNIFFEL) == 50:
        #print("yahtzee is the best choice")
        return False, Combinations.KNIFFEL
    elif best_now.get(Combinations.LARGE_STRAIGHT) == 40:
        #print("large straight is the best choice")
        return False, Combinations.LARGE_STRAIGHT
    elif best_now.get(Combinations.SMALL_STRAIGHT) == 30:
        #print("small straight is the best choice")
        return False, Combinations.SMALL_STRAIGHT
    elif best_now.get(Combinations.FULL_HOUSE) == 25:
        #print("full house is the best choice")
        return False, Combinations.FULL_HOUSE
    elif best_now.get(Combinations.FOUR_OF_KIND) if best_now.get(Combinations.FOUR_OF_KIND) is not None else 0 > 5:
        #print("four of a kind is the best choice")
        return False, Combinations.FOUR_OF_KIND
    elif best_now.get(Combinations.THREE_OF_KIND) if best_now.get(Combinations.THREE_OF_KIND) is not None else 0 > 6:
        #print("three of a kind is the best choice")
        return False, Combinations.THREE_OF_KIND
    else:
        #print("There is no good special combination")
        if rerolls_left > 0:
            # print("reroll")
            # choose the cubes to reroll
            return True, reroll_controller(dice_sorted, available_combinations)
        else:
            #print("no rerolls left, choose the best left over")
            best = next(iter(best_now))
            #print(f"{best} is the best with {best_now.get(next(iter(best_now)))} points")
            return False, best


if __name__ == "__main__":
    # [1, 2, 5, 3, 5]
    # random cubes
    gewuerfelt = [1, 2, 5, 3, 5]
    available = [
        Combinations.ONES,
        Combinations.TWOS,
        Combinations.THREES,
        Combinations.FOURS,
        Combinations.FIVES,
        Combinations.SIXES,
        Combinations.THREE_OF_KIND,
        Combinations.FOUR_OF_KIND,
        Combinations.FULL_HOUSE,
        Combinations.SMALL_STRAIGHT,
        Combinations.LARGE_STRAIGHT,
        Combinations.KNIFFEL,
        Combinations.CHANCE

    ]
    left_rerolls = 1
    choice = bot_controller(gewuerfelt, available, left_rerolls)
    print(choice)
