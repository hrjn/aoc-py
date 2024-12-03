import re
from pathlib import Path
from typing import List

INPUTFILE = "inputs/day03.txt"


def add_mul_ops(mem_str: str) -> int:
    output = 0
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, mem_str)
    for m in matches:
        x, y = map(int, m)
        output += x * y
    return output


def add_mul_ops_v2(mem_str: str) -> int:
    output = 0
    is_mul_enabled = True
    patterns = {
        "mul": r"mul\((\d{1,3}),(\d{1,3})\)",
        "do": r"do\(\)",
        "dont": r"don\'t\(\)",
    }
    # Use re.finditer() to collect additional match info
    matches = {k: re.finditer(patterns[k], mem_str) for k in patterns.keys()}

    # Collect relevant matches
    sorted_matches = []
    for k, v in matches.items():
        sorted_matches += list(v)
    sorted_matches = sorted(sorted_matches, key=(lambda m: m.start()))

    # Process matches
    for m in sorted_matches:
        if m.group() == "do()":
            # print("ENABLED")
            is_mul_enabled = True
        elif m.group() == "don't()":
            # print("DISABLED")
            is_mul_enabled = False
        elif is_mul_enabled:
            x, y = map(int, m.groups())
            output += x * y

    return output


def part01(debug: bool = False) -> int:
    if debug:
        filename = INPUTFILE.replace(".txt", "_part01_test.txt")
    else:
        filename = INPUTFILE
    with Path(filename).open(mode="r") as f_in:
        mem = f_in.read()
    return add_mul_ops(mem)


def part02(debug: bool = False) -> int:
    if debug:
        filename = INPUTFILE.replace(".txt", "_part02_test.txt")
    else:
        filename = INPUTFILE
    with Path(filename).open(mode="r") as f_in:
        mem = f_in.read()
    return add_mul_ops_v2(mem)


print(part01(debug=False))
print(part02(debug=False))
