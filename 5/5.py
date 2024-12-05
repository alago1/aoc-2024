from collections import defaultdict, deque, Counter
from itertools import combinations, cycle
from itertools import product as cartesian_product, count as count_from
from functools import lru_cache, reduce, cmp_to_key
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
        lines = [x.strip() for x in file.readlines()]

    empty_line = lines.index('')
    pairs = [list(map(int, x.split('|'))) for x in lines[:empty_line]]
    pages = [list(map(int, x.split(','))) for x in lines[empty_line + 1:]]
    return pairs, pages

def part1(pairs, pages):
    middles = []
    for page in pages:
        for a, b in combinations(page, 2):
            if [b, a] in pairs:
                break
        else:
            middles.append(page[len(page) // 2])
    return sum(middles)

def comp_page_nums(less_set, page1, page2):
    pair = (page1, page2)
    if pair in less_set:
        return -1
    if reversed(pair) in less_set:
        return 1
    return 0

def part2(pairs, pages):
    disordered = []
    for page in pages:
        for a, b in combinations(page, 2):
            if [b, a] in pairs:
                disordered.append(page)
                break
    
    less_set = set(map(tuple, pairs))
    cmp = cmp_to_key(lambda x0, x1: comp_page_nums(less_set, x0, x1))
    ordered = [sorted(y, key=cmp) for y in disordered]
    return sum([x[len(x) // 2] for x in ordered])

if __name__ == '__main__':
    pairs, pages = parse('input.txt')
    print(f"Part 1: {part1(pairs, pages)}")
    print(f"Part 2: {part2(pairs, pages)}")
