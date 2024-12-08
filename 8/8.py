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
        return [list(x.strip()) for x in file.readlines()]

def is_valid(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def part1(grid):
    unique_nodes = dict()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != '.':
                if grid[r][c] not in unique_nodes:
                    unique_nodes[grid[r][c]] = []
                unique_nodes[grid[r][c]].append((r, c))
    
    antinodes = set()
    for v in unique_nodes.values():
        for n1, n2 in combinations(v, 2):
            offset = (n1[0] - n2[0], n1[1] - n2[1])

            anti1 = (n1[0] + offset[0], n1[1] + offset[1])
            anti2 = (n2[0] - offset[0], n2[1] - offset[1])
            if is_valid(grid, *anti1):
                antinodes.add(anti1)
            if is_valid(grid, *anti2):
                antinodes.add(anti2)
    
    return len(antinodes)

def part2(grid):
    unique_nodes = dict()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != '.':
                if grid[r][c] not in unique_nodes:
                    unique_nodes[grid[r][c]] = []
                unique_nodes[grid[r][c]].append((r, c))
    
    antinodes = set()
    for v in unique_nodes.values():
        for n1, n2 in combinations(v, 2):
            offset = (n1[0] - n2[0], n1[1] - n2[1])
            offset = (offset[0] // gcd(*offset), offset[1] // gcd(*offset))

            anti = deepcopy(n1)
            while is_valid(grid, *anti):
                antinodes.add(anti)
                anti = (anti[0] + offset[0], anti[1] + offset[1])
            anti = (n1[0]-offset[0], n1[1]-offset[1])
            while is_valid(grid, *anti):
                antinodes.add(anti)
                anti = (anti[0] - offset[0], anti[1] - offset[1])
    
    return len(antinodes)

if __name__ == '__main__':
    x = parse('input.txt')
    print(f"Part 1: {part1(x)}")
    print(f"Part 2: {part2(x)}")
