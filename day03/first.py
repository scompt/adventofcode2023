#!/usr/bin/env python3.12
import sys
lines = [l.strip() for l in sys.stdin.readlines()]

from collections import defaultdict
grid = defaultdict(lambda: [])
nums = []

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        grid[y].append(char)

for y in range(len(grid)):
    start = None
    length = 1
    for x in range(len(grid[y])):
        if grid[y][x].isdigit():
            if not start:
                start = (y, x)
            else:
                length += 1
        elif start:
            nums.append((start, length))
            start = None
            length = 1
    if start:
        nums.append((start, length))
        start = None
        length = 1


real = []
for start, length in nums:
    adj = False
    for y in range(start[0]-1, start[0]+2):
        for x in range(start[1]-1, start[1]+1+length):
            try:
                char = grid.get(y, {})[x]
            except:
                char = '.'
            adj = adj or (not char.isdigit() and char != '.')
    if adj:
        real.append(int(''.join(grid[start[0]][start[1]:start[1]+length])))

print(sum(real))
