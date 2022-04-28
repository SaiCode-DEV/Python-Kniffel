# https://brefeld.homepage.t-online.de/kniffel.html
import random
import sys
from numpy import diff

from kniffel.data_objects.combinations import Combinations
from kniffel.game_logic.value_calculator import *
import numpy as np
from numpy import asarray as ar


def get_best_choice(dice: List[int], available_combinations: List[Combinations]) -> dict:
    generate = []
    if len(available_combinations) == 0:
        return {}
    for combination in available_combinations:
        # calculate the value of the throw
        match combination.value:
            case Combinations.ONES.value:
                generate.append(get_one_value(dice) / 1 * 5 + 1)
            case Combinations.TWOS.value:
                generate.append(get_two_value(dice) / 2 * 5 + 2)
            case Combinations.THREES.value:
                generate.append(get_three_value(dice) / 3 * 5 + 3)
            case Combinations.FOURS.value:
                generate.append(get_four_value(dice) / 4 * 5 + 4)
            case Combinations.FIVES.value:
                generate.append(get_five_value(dice) / 5 * 5 + 5)
            case Combinations.SIXES.value:
                generate.append(get_six_value(dice) / 6 * 5 + 6)
            case Combinations.THREE_OF_KIND.value:
                generate.append(get_three_of_kind_value(dice))
            case Combinations.FOUR_OF_KIND.value:
                generate.append(get_four_of_kind_value(dice))
            case Combinations.FULL_HOUSE.value:
                generate.append(get_full_house_value(dice))
            case Combinations.SMALL_STRAIGHT.value:
                generate.append(get_small_straight_value(dice))
            case Combinations.LARGE_STRAIGHT.value:
                generate.append(get_large_straight_value(dice))
            case Combinations.KNIFFEL.value:
                generate.append(get_kniffel_value(dice))
            case Combinations.CHANCE.value:
                # to make it less interesting
                generate.append(get_chance_value(dice) - 10)

    if len(generate) == len(available_combinations):
        possible = dict(zip(available_combinations, generate))
        # sort out all the impossible / useless combinations
        possible = {a: b for a, b in possible.items() if b != 0}
        # print(possible)
        # get the highest value
        return dict(sorted(possible.items(), key=lambda x: x[1], reverse=True))
    else:
        return {}


def calculate_expected_value(gewuerfelt, available):

    return 0


def reroll_controller(dice_rolled, available_combinations):
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
    print(f"orginal: {dice_rolled}\n")
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


def bot_controller(dice: list[int], available_combinations, rerolls_left=0) -> Combinations:
    # sort the dices by value
    dice_sorted = sorted(dice, reverse=True)
    print(dice_sorted)
    best_now = get_best_choice(dice_sorted, available_combinations)
    print(best_now)
    if best_now.get(Combinations.KNIFFEL) == 50:
        print("yahtzee is the best choice")
        return Combinations.KNIFFEL
    elif best_now.get(Combinations.LARGE_STRAIGHT) == 40:
        print("large straight is the best choice")
        return Combinations.LARGE_STRAIGHT
    elif best_now.get(Combinations.SMALL_STRAIGHT) == 30:
        print("small straight is the best choice")
        return Combinations.SMALL_STRAIGHT
    elif best_now.get(Combinations.FULL_HOUSE) == 25:
        print("full house is the best choice")
        return Combinations.FULL_HOUSE
    elif best_now.get(Combinations.FOUR_OF_KIND) if best_now.get(Combinations.FOUR_OF_KIND) is not None else 0 > 5:
        print("four of a kind is the best choice")
        return Combinations.FOUR_OF_KIND
    elif best_now.get(Combinations.THREE_OF_KIND) if best_now.get(Combinations.THREE_OF_KIND) is not None else 0 > 6:
        print("three of a kind is the best choice")
        return Combinations.THREE_OF_KIND
    else:
        print("There is no good special combination")
        if rerolls_left > 0:
            print("reroll")
            # choose the cubes to reroll
            return reroll_controller(dice_sorted, available_combinations)
        else:
            print("no rerolls left, choose the best left over")
            best = next(iter(best_now))
            print(
                f"{best} is the best with {best_now.get(next(iter(best_now)))} points")
            return best


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


def test(available_combinations):
    # try out each possible dice combination
    dices = []
    for dice1 in range(6):
        for dice2 in range(6):
            for dice3 in range(6):
                for dice4 in range(6):
                    for dice5 in range(6):
                        # create a new list with the new dice values
                        dices.append(
                            sorted([dice1 + 1, dice2 + 1, dice3 + 1, dice4 + 1, dice5 + 1]))
    dices = list(set({tuple(i) for i in dices}))
    dices = sorted([list(i) for i in dices])
    print(len(dices))
    for dice in dices:
        new_value = get_best_choice(dice, available_combinations)
        # subdivide 10 from chance
        print(f"{dice} | {next(iter(new_value))} is the best with {new_value.get(next(iter(new_value)))} points")
