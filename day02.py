from pathlib import Path
from typing import List

INPUTFILE = "inputs/day02.txt"

def load_reports(filename: str) -> List[List[int]]:
    with Path(filename).open(mode='r') as f_in:
        data = f_in.read()
        reports = [list(map(int, line.split())) for line in data.rstrip().split('\n')]
    return reports


def check_safety(report: List[int]) -> bool:
    increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    # Unsafe if not increasing or decreasing
    if not (increasing or decreasing):
        return False
    # Unsafe if incr/decr value is not in [-1,3]
    for i in range(len(report) - 1):
        if not (1 <= abs(report[i]-report[i + 1]) <= 3):
            return False
    return True

def check_safety_with_dampening(report: str) -> bool:
    for i in range(len(report)):
        mod_report = report[:i] + report[i+1:]
        if check_safety(mod_report):
            return True
    return False

def part01(debug: bool = True) -> int:
    if debug:
        filename = INPUTFILE.replace(".txt", "_test.txt")
    else:
        filename = INPUTFILE
    num_safe_reports = 0
    for report in load_reports(filename):
        if check_safety(report):
            num_safe_reports += 1
    return num_safe_reports

def part02(debug: bool = True) -> int:
    if debug:
        filename = INPUTFILE.replace(".txt", "_test.txt")
    else:
        filename = INPUTFILE
    num_safe_reports = 0
    for report in load_reports(filename):
        if check_safety(report) or check_safety_with_dampening(report):
            num_safe_reports += 1
    return num_safe_reports

print(part01(debug=False))
print(part02(debug=False))

