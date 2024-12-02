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
        return [x.strip().split() for x in file.readlines()]

def is_safe(level):
    diff = list([x - y for x, y in zip(level, level[1:])])
    monotonic = all([v > 0 for v in diff]) or all([v < 0 for v in diff])
    in_range = all([1 <= abs(x) <= 3 for x in diff])
    return monotonic and in_range

def part1(lines):
    levels = [[int(x) for x in line] for line in lines]
    return sum([is_safe(level) for level in levels])

def part2(lines):
    levels = [[int(x) for x in line] for line in lines]
    count = 0
    for level in levels:
        if is_safe(level):
            count += 1
            continue
        for j in range(len(level)):
            if is_safe(level[:j] + level[j+1:]):
                count += 1
                break
    
    return count

if __name__ == '__main__':
    x = parse('input.txt')
    print(f"Part 1: {part1(x)}")
    print(f"Part 2: {part2(x)}")
