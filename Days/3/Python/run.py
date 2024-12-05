#!/usr/bin/env python3
import os
import re
import sys

####################### Helping functions###########################


def data_parser(filepath) -> str:
    """Parse the data by returning it as a string."""

    with open(filepath, "r") as file:
        return file.read()


######################### Main functions############################


def solver_1star(data: str):
    """
    Use a regex to find all orruncances of "mul(xxx,yyy)",
    then summarize xxx*yyy on all occurances
    """
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

    ret = 0
    for match in re.finditer(pattern, data):
        ret += int(match.group(1)) * int(match.group(2))

    return ret


def solver_2star(data: str):
    """
    Same as star1, but extend regex to catch dont and do, and add
    some logic when iterating over the mathces, to turn off the mul
    """
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|don\'t\(\)|do\(\)")

    ret = 0
    enabled = True
    for match in re.finditer(pattern, data):
        if match.group(0) == "do()":
            enabled = True
        elif match.group(0) == "don't()":
            enabled = False
        elif enabled:
            ret += int(match.group(1)) * int(match.group(2))

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
