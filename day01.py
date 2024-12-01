from typing import Tuple, List
from collections import Counter

INPUTFILE = "inputs/day01.txt"
# INPUTFILE = "inputs/day01_test.txt"

def get_left_and_right_from_file(filename: str) -> Tuple[List[int],List[int]]:
    left: List[int] = []
    right: List[int] = []
    with open(filename, mode='r') as f_in:
       for line in f_in:
           items = [int(x) for x in line.rstrip().split('   ')]
           left.append(items[0])
           right.append(items[1])
    return left, right


def part01(debug: bool = True) -> int:
    dist_total = 0
    if debug:
        filename = INPUTFILE.replace(".txt", "_test.txt")
    else:
        filename = INPUTFILE
    left, right = get_left_and_right_from_file(filename)
    # TODO
    left.sort()
    right.sort()
    for idx in range(len(left)):
        dist_total = sum([abs(x-y) for x, y in zip(left, right)])
    return dist_total

def part02(debug: bool = False) -> int:
    if debug:
        filename = INPUTFILE.replace(".txt", "_test.txt")
    else:
        filename = INPUTFILE
    left, right = get_left_and_right_from_file(filename)
    cnt = Counter(right)
    dist = sum([l_item*cnt[l_item] for l_item in left])
    return dist
