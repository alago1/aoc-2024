from collections import Counter

def parse(filename):
    with open(filename) as f:
        return [s.strip().split('   ') for s in f.readlines()]

def part1(inputs):
    pairs = [[int(x[0]), int(x[1])] for x in inputs]

    left = sorted([x[0] for x in pairs])
    right = sorted([x[1] for x in pairs])

    diff = [abs(x-y) for x, y in zip(left, right)]
    return sum(diff)

def part2(inputs):
    pairs = [[int(x[0]), int(x[1])] for x in inputs]

    left = sorted([x[0] for x in pairs])
    right = sorted([x[1] for x in pairs])

    counter = Counter(right)
    return sum([l*counter.get(l, 0) for l in left])

if __name__ == '__main__':
    inputs = parse('input.txt')
    print(f"Part 1: {part1(inputs)}")
    print(f"Part 2: {part2(inputs)}")
