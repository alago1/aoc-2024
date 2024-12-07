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
        lines = [x.strip().split(': ') for x in file.readlines()]
    return [
        (int(x), list(map(int, y.split())))
        for x, y in lines
    ]

def test_config(ins, config, num_ops):
    qi = deque(ins)
    while len(qi) > 1:
        i1 = qi.popleft()
        i2 = qi.popleft()
        config, op = divmod(config, num_ops)
        if op == 0: # op == '+'
            qi.appendleft(i1 + i2)
        elif op == 1: # op == '*'
            qi.appendleft(i1 * i2)
        else: # op == '||'
            qi.appendleft(int(str(i1) + str(i2)))
    return qi.popleft()

def part1(x):
    num_ops = 2
    s = 0
    for target, ins in x:
        # represent configuration as number in base num_ops
        for config in range(num_ops ** (len(ins) - 1)):
            if test_config(ins, config, num_ops) == target:
                s += target
                break
    return s

def part2(x):
    num_ops =3
    s = 0
    for target, ins in x:
        # represent configuration as number in base num_ops
        for config in range(num_ops ** (len(ins) - 1)):
            if test_config(ins, config, num_ops) == target:
                s += target
                break
    return s

if __name__ == '__main__':
    x = parse('input.txt')
    print(f"Part 1: {part1(x)}")
    print(f"Part 2: {part2(x)}")
