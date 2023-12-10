#!/usr/bin/env python3.12
import sys
lines = [l.strip() for l in sys.stdin.readlines()]

games = []

threshold = {'red': 12, 'green': 13, 'blue': 14}
colors = threshold.keys()

for l in lines:
    games.append([])
    sets = l.split(': ')[1].split('; ')
    for aset in sets:
        games[-1].append({})
        cubes = aset.split(', ')
        for cube in cubes:
            num, color = cube.split(' ', 1)
            games[-1][-1][color] = int(num)

powers = []
for i, game in enumerate(games):
    mins = {color: 0 for color in colors}
    for aset in game:
        for color in colors:
            mins[color] = max(mins[color], aset.get(color, 0))
    power = 1
    for color in colors:
        power *= mins[color]
    powers.append(power)
print(sum(powers))
