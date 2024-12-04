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

def is_valid(y, x, grid):
    return 0 <= y < len(grid) and 0 <= x < len(grid[y])

def get_subarray(y0, x0, dy, dx, grid):
    out = []
    for delta_y in range(dy+1):
        for delta_x in range(dx+1):
            if not is_valid(y0 + delta_y, x0 + delta_x, grid):
                return None
            out.append(grid[y0 + delta_y][x0 + delta_x])
    return "".join(out)

def get_diag_subarray(y0, x0, d, dir_y, grid):
    out = []
    for delta in range(d+1):
        if not is_valid(y0 + delta*dir_y, x0 + delta, grid):
            return None
        out.append(grid[y0 + delta*dir_y][x0 + delta])
    return "".join(out)

def print_grid(grid):
    for row in grid:
        print(row)

def part1(grid):
    valid_xmas = {"XMAS", "SAMX"}
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # horizontal
            if get_subarray(i, j, 0, 3, grid) in valid_xmas:
                count += 1
            # vertical
            if get_subarray(i, j, 3, 0, grid) in valid_xmas:
                count += 1
            # diagonal top left to bottom right
            if get_diag_subarray(i, j, 3, 1, grid) in valid_xmas:
                count += 1
            # diagonal top left to bottom right
            if get_diag_subarray(i, j, 3, -1, grid) in valid_xmas:
                count += 1
    return count


def part2(grid):
    valid_mas = {"MAS", "SAM"}
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            diag_top_left_bottom_right = get_diag_subarray(i, j, 2, 1, grid)
            diag_bottom_left_top_right = get_diag_subarray(i+2, j, 2, -1, grid)
            if diag_top_left_bottom_right in valid_mas and diag_bottom_left_top_right in valid_mas:
                count += 1
    return count

if __name__ == '__main__':
    x = parse('input.txt')
    print(f"Part 1: {part1(x)}")
    print(f"Part 2: {part2(x)}")
