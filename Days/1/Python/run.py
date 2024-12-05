#!/usr/bin/env python3
from collections import defaultdict
import os
import sys
from typing import Tuple

####################### Helping functions###########################


def data_parser(filepath) -> Tuple[list[int], list[int]]:
    """Parse the data by splitting each line into two number."""

    ret_a = []
    ret_b = []
    with open(filepath, "r") as file:
        data = file.read()
        ret = data.split("\n")
        for element in ret:
            a, b = element.split("   ")
            ret_a.append(int(a))
            ret_b.append(int(b))

    return ret_a, ret_b


######################### Main functions############################


def solver_1star(data: Tuple[list[int], list[int]]):
    """
    Sort each list of elements, and compare the distance one at
    a time, and add to a return value
    """
    a_unsorted, b_unsorted = data
    ret = 0
    for a, b in zip(sorted(a_unsorted), sorted(b_unsorted)):
        ret += abs(a - b)

    return ret


def solver_2star(data: Tuple[list[int], list[int]]):
    """
    Count all the occurances in list b, and iterate over list a.
    for each found, multiply it with the value, and add it to the return.
    """
    a, b = data
    b_seen = defaultdict(int)
    ret = 0
    for element in b:
        b_seen[element] += 1

    for element in a:
        ret += b_seen[element] * element

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
