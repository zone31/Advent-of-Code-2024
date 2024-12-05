#!/usr/bin/env python3
import itertools
import os
import sys
from typing import Optional

####################### Helping functions###########################


def data_parser(filepath) -> list[list[str]]:
    """Parse the data by returning it as a list of lists of str."""
    ret = []
    with open(filepath, "r") as file:
        data = file.read()
        for element in data.split("\n"):
            ret.append(list(element))

    return ret


def coord_to_letter(x: int, y: int, data: list[list[str]]) -> Optional[str]:
    if x < len(data) and x >= 0:
        if y < len(data[x]) and y >= 0:
            return data[x][y]
    return None


######################### Main functions############################


def solver_1star(data: list[list[str]]):
    """
    Iterate over the board, and look in all directions, finding the
    target string
    """
    ret = 0
    # generate the search offset patterns
    # delete (0,0)
    pat = list(itertools.product([0, 1, -1], [0, 1, -1]))
    del pat[0]

    # define the search string, and try to find it
    s = "XMAS"
    for x in range(len(data)):
        for y in range(len(data[0])):
            # Check all dirrections
            for x_d, y_d in pat:
                x_range = [x + x_d * a for a in range(len(s))]
                y_range = [y + y_d * a for a in range(len(s))]

                value = []
                for x_p, y_p in zip(x_range, y_range):
                    if char := coord_to_letter(x_p, y_p, data):
                        value.append(char)
                found = "".join(value)
                if found == s:
                    ret += 1

    return ret


def solver_2star(data: list[list[str]]):
    """
    Detine the search pattern, and iterate over the board, looking for it
    """
    patterns = [
        [
            ["M", None, "M"],
            [None, "A", None],
            ["S", None, "S"],
        ],
        [
            ["M", None, "S"],
            [None, "A", None],
            ["M", None, "S"],
        ],
        [
            ["S", None, "S"],
            [None, "A", None],
            ["M", None, "M"],
        ],
        [
            ["S", None, "M"],
            [None, "A", None],
            ["S", None, "M"],
        ],
    ]
    ret = 0
    # do not iterate over the edges, since we have
    # a pattern that is >1 in height an width
    for x in range(1, len(data) - 1):
        for y in range(1, len(data[0]) - 1):
            seen = []
            for b in range(y - 1, y + 2):
                seen.append([coord_to_letter(a, b, data) for a in range(x - 1, x + 2)])

            for pattern in patterns:
                match = True
                for x_i, pattern_x in enumerate(pattern):
                    for y_i, value in enumerate(pattern_x):
                        if value is not None and seen[x_i][y_i] != value:
                            match = False
                            pass
                if match:
                    ret += 1

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
