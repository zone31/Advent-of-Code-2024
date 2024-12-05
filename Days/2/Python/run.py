#!/usr/bin/env python3
import os
import sys

####################### Helping functions###########################


def data_parser(filepath) -> list[list[int]]:
    """Parse the data by splitting each line into a list of ints."""

    ret = []
    with open(filepath, "r") as file:
        data = file.read()
        for element in data.split("\n"):
            ret.append([int(x) for x in element.split(" ")])

    return ret


def is_valid_list(input: list[int]):
    diffs = [x - y for x, y in zip(input[1:], input)]
    max_change = 3
    going_up = all([x > 0 and x <= max_change for x in diffs])
    going_down = all([x < 0 and x >= -max_change for x in diffs])

    return going_up or going_down


######################### Main functions############################


def solver_1star(data: list[list[int]]):
    """
    Iterate over each element, and create a diff list, with the up/down
    difference. test this list if we are going up or down correctly
    """
    ret = 0
    for element in data:
        if is_valid_list(element):
            ret += 1
    return ret


def solver_2star(data: list[list[int]]):
    """
    Same as star 1, but also check sublists, where a element is removed.
    """
    ret = 0
    for element in data:
        if is_valid_list(element):
            ret += 1
            continue
        for index in range(len(element)):
            sublist = list(element)
            del sublist[index]
            if is_valid_list(sublist):
                ret += 1
                break

    return ret


############################## MAIN#################################


def main(solve=0):
    """Run the program by itself, return a tuple of star1 and star2.

    solve: set what stars we want, 0 returns both
    """
    dirname = os.path.dirname(__file__)
    input_source = os.path.join(dirname, "..", "input1.txt")
    # Make list, since the generator has to be used multiple times
    data = data_parser(input_source)
    match solve:
        case 0:
            return (solver_1star(data), solver_2star(data))
        case 1:
            return (solver_1star(data), None)
        case 2:
            return (None, solver_2star(data))
        case _:
            raise Exception(f"solve set wrong! ({solve})")


def day_name():
    """Get the date name from the folder."""
    file_path = os.path.dirname(__file__)
    day_path = os.path.normpath(os.path.join(file_path, ".."))
    return os.path.basename(day_path)


if __name__ == "__main__":
    solve = 0
    if len(sys.argv) == 2:
        solve = int(sys.argv[1])
    star1, star2 = main(solve)

    match solve:
        case 0:
            day = day_name()
            print(f"Day {day} first star:")
            print(star1)
            print(f"Day {day} second star:")
            print(star2)
        case 1:
            print(star1)
        case 2:
            print(star2)
        case _:
            raise Exception(f"solve set wrong! ({solve})")
