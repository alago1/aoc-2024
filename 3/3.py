from collections import defaultdict, deque, Counter
from itertools import combinations, cycle
from itertools import product as cartesian_product, count as count_from
from functools import lru_cache, reduce
from math import gcd, prod
from copy import deepcopy
import heapq
import re

try:
    from math import lcm
except ImportError:
    def lcm(*args):
        return reduce(lambda x, y: abs(x * y) // gcd(x, y), args)


def parse(filename):
    with open(filename) as file:
        return file.read().strip()

def part1(line):
    matches = re.findall('mul\\([0-9]+,[0-9]+\\)', line)
    vals = [
        prod(map(int, mul[4:-1].split(',') ))
        for mul in matches
    ]
    return sum(vals)


def part2(line):
    matches = re.findall('(mul\\([0-9]+,[0-9]+\\))|(do\\(\\))|(don\'t\\(\\))', line)
    vals = [
        prod(map(int, op[0][4:-1].split(',') )) if op[0] else op[1] + op[2]
        for op in matches
    ]
    s = 0
    skip = False
    for val in vals:
        if val == 'don\'t()':
            skip = True
        elif val == 'do()':
            skip = False
        else:
            s += val * (1 - skip)
    return s
    
if __name__ == '__main__':
    x = parse('input.txt')
    print(f"Part 1: {part1(x)}")
    print(f"Part 2: {part2(x)}")
