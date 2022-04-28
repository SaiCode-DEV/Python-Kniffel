# https://brefeld.homepage.t-online.de/kniffel.html
import random
from game_logic.value_calculator import *
import sys
import numpy as np
from numpy import asarray as ar, number
sys.path.append('../')
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


def get_best_choice(gewuerfelt:list(number), available) -> dict:
    """Return the best choice on a simple logic basis.

    Args:
        gewuerfelt (list): The numbers the dice rolled.
        available (list): A list of all still available options to choose from.

    Returns:
        dict: what dices should be rerolled or what option the bot chose.
    """
    generate = []
    if(len(available) == 0):
        return {}
    for i in enumerate(available):
        # calculate the value of the throw
        match available[i]:
            case "one":
                generate.append(get_one_value(gewuerfelt) / 1 * 5 + 1)
            case "two":
                generate.append(get_two_value(gewuerfelt) / 2 * 5 + 2)
            case "three":
                generate.append(get_three_value(gewuerfelt) / 3 * 5 + 3)
            case "four":
                generate.append(get_four_value(gewuerfelt) / 4 * 5 + 4)
            case "five":
                generate.append(get_five_value(gewuerfelt) / 5 * 5 + 5)
            case "six":
                generate.append(get_six_value(gewuerfelt) / 6 * 5 + 6)
            case "three_of_a_kind":
                generate.append(get_three_of_kind_value(gewuerfelt))
            case "four_of_a_kind":
                generate.append(get_four_of_kind_value(gewuerfelt))
            case "full_house":
                generate.append(get_full_house_value(gewuerfelt))
            case "small_straight":
                generate.append(get_small_straight_value(gewuerfelt))
            case "large_straight":
                generate.append(get_large_straight_value(gewuerfelt))
            case "yahtzee":
                generate.append(get_kniffel_value(gewuerfelt))
            case "chance":
                # to make it less interesting
                generate.append(get_chance_value(gewuerfelt) - 10)

    if(len(generate) == len(available)):
        possible = dict(zip(available, generate))
        # sort out all the impossible / useless combinations
        possible = {a: b for a, b in possible.items() if b != 0}
        # print(possible)
        # get the highest value
        return dict(sorted(possible.items(), key=lambda x: x[1], reverse=True))
    else:
        return {}



def reroll_controller(gewuerfelt, available):
    """Choose the cubes to reroll.

    Args:
        gewuerfelt (list): The numbers the dice rolled.
        available (list): A list of all still available options to choose from.

    Returns:
        list: The cubes to reroll. 
    """
    # try out each possible dice combination
    dices = []
    for dice in range(6):
        dices.append(sorted([dice + 1] + gewuerfelt[1:], reverse=True))
        dices.append(
            sorted(gewuerfelt[:1] + [dice + 1] + gewuerfelt[2:], reverse=True))
        dices.append(
            sorted(gewuerfelt[:2] + [dice + 1] + gewuerfelt[3:], reverse=True))
        dices.append(
            sorted(gewuerfelt[:3] + [dice + 1] + gewuerfelt[4:], reverse=True))
        dices.append(sorted(gewuerfelt[:4] + [dice + 1], reverse=True))
    print(f"orginal: {gewuerfelt}\n")
    # print(dices)
    dices = list(set({tuple(i) for i in dices}))
    dices = sorted([list(i) for i in dices])
    output_points = []
    for dice in dices:
        output_points.append(get_best_choice(dice, available))
    output_points, dices = zip(*sorted(zip(output_points, dices),
                               key=lambda x: x[0].get(next(iter(x[0])), 0), reverse=True))
    max_points = max([i.get(next(iter(i)), 0) for i in output_points])
    different = []
    for option, dice in zip(output_points, dices):
        if(option.get(next(iter(option)), 0) == max_points):
            #print(f"{dice} | {next(iter(option))} is the best with {option.get(next(iter(option)))} points")
            different.append(dice)
    changed_dices = [False, False, False, False, False]
    for difference in different:
        changed_dices = ar(np.array(difference) != np.array(
            gewuerfelt)) | ar(changed_dices)
    return changed_dices

    # get the elements with the highest value


def bot_controller(gewuerfelt: list[int], available, left_rerolls=0):
    """The main bot controller

    Args:
        gewuerfelt (list[int]): The numbers the dice have rolled.
        available (list[str]): What options are still available to choose from.
        left_rerolls (int, optional): How many Rerolls are left 0 = none. Defaults to 0.

    Returns:
        str: The option the bot chose.
    """
    # sort the dices by value
    gewuerfelt = sorted(gewuerfelt, reverse=True)
    print(gewuerfelt)
    best_now = get_best_choice(gewuerfelt, available)
    print(best_now)
    if (available == []):
        return "nothing to choose"
    if (best_now.get("yahtzee") == 50):
        print("yahtzee is the best choice")
        return "yahtzee"
    elif(best_now.get("large_straight") == 40):
        print("large straight is the best choice")
        return "large_straight"
    elif(best_now.get("small_straight") == 30):
        print("small straight is the best choice")
        return "small_straight"
    elif(best_now.get("full_house") == 25):
        print("full house is the best choice")
        return "full_house"
    elif(best_now.get("four_of_a_kind") if best_now.get("four_of_a_kind") is not None else 0 > 5):
        print("four of a kind is the best choice")
        return "four_of_a_kind"
    elif(best_now.get("three_of_a_kind") if best_now.get("three_of_a_kind") is not None else 0 > 6):
        print("three of a kind is the best choice")
        return "three_of_a_kind"
    else:
        print("There is no good special combination")
        if(left_rerolls > 0):
            print("reroll")
            # choose the cubes to reroll
            return reroll_controller(gewuerfelt, available)
        else:
            print("no rerolls left, choose the best left over")
            best = next(iter(best_now))
            print(
                f"{best} is the best with {best_now.get(next(iter(best_now)))} points")
            return best


if __name__ == "__main__":
    #[1, 2, 5, 3, 5]
    # ranom cubes
    gewuerfelt = [random.randint(1, 6) for i in range(5)]
    available = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "four_of_a_kind",
        "full_house",
        "small_straight",
        "large_straight",
        "yahtzee",
        "chance"]
    left_rerolls = 1
    choice = bot_controller(gewuerfelt, available, left_rerolls)
    print(choice)


def test(available):
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
        new_value = get_best_choice(dice, available)
        # subdivide 10 from chance
        print(f"{dice} | {next(iter(new_value))} is the best with {new_value.get(next(iter(new_value)))} points")
