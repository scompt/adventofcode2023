#!/usr/bin/env python3.12
import sys
lines = [l.strip() for l in sys.stdin.readlines()]

games = []

threshold = {'red': 12, 'green': 13, 'blue': 14}

for l in lines:
    games.append([])
    sets = l.split(': ')[1].split('; ')
    for aset in sets:
        games[-1].append({})
        cubes = aset.split(', ')
        for cube in cubes:
            num, color = cube.split(' ', 1)
            games[-1][-1][color] = int(num)

possible_ids = []
for i, game in enumerate(games):
    possible = True
    for aset in game:
        for color, thres in threshold.items():
            if aset.get(color, 0) > thres:
                possible = False
    if possible:
        possible_ids.append(i+1)
print(sum(possible_ids))
