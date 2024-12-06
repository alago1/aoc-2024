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
        grid = [list(x.strip()) for x in file.readlines()]
    return grid

def print_grid(grid, visited):
    g = deepcopy(grid)
    for (r, c), _ in visited:
        g[r][c] = 'O'
    for row in g:
        print(''.join(row))

def is_in_range(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[r])

def is_looping(grid, start_pos):
    # right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    pos = start_pos
    dir_index = 3

    visited = set()
    while (pos, dir_index) not in visited:
        visited.add((pos, dir_index))
        
        p = (pos[0] + directions[dir_index][0], pos[1] + directions[dir_index][1])
        if not is_in_range(grid, p[0], p[1]):
            return False
        if grid[p[0]][p[1]] == '#':
            dir_index = (dir_index + 1) % 4
            continue
        pos = p
    
    return True

def part1(grid):
    # right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '^':
                pos = (r, c)
    dir_index = 3

    visited = set()
    while (pos, dir_index) not in visited:
        visited.add((pos, dir_index))
        
        p = (pos[0] + directions[dir_index][0], pos[1] + directions[dir_index][1])
        if not is_in_range(grid, p[0], p[1]):
            break
        if grid[p[0]][p[1]] == '#':
            dir_index = (dir_index + 1) % 4
            continue
        pos = p
    
    return len({p for p, _ in visited})

def part2(grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '^':
                start_pos = (r, c)
    
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '.':
                grid[r][c] = '#'
                count += is_looping(grid, start_pos)
                grid[r][c] = '.'
    
    return count

if __name__ == '__main__':
    x = parse('input.txt')
    print(f"Part 1: {part1(x)}")
    print(f"Part 2: {part2(x)}")
