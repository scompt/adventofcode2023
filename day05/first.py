#!/usr/bin/env python3.12
import sys
from collections import defaultdict
lines = [l.strip() for l in sys.stdin.readlines()]

seeds = [int(s) for s in lines[0][7:].split(' ')]

maps = defaultdict(lambda: defaultdict(lambda: []))
currentmap = None
for l in lines[2:]:
    if l.endswith(' map:'):
        fromm = l.split('-')[0]
        tom = l.split(' ')[0].split('-')[2]
        currentmap = (fromm, tom)
    elif len(l) > 1:
        maps[currentmap[0]][currentmap[1]].append(tuple(int(n) for n in l.split(' ')))
    else:
        currentmap = None

memo = defaultdict(lambda: {})
locations = []
for froms, length in zip(seeds[0::2], seeds[1::2]):
    for seed in range(froms, froms+length):
        position = seed
        mapp = 'seed'
        memo_locs = []
        while mapp != 'location':
            memo_loc = (mapp, position)
            if memo_loc in memo:
                print('memo')
                position = memo[memo_loc]
                break
            memo_locs.append(memo_loc)
            destmap  = list(maps[mapp].keys()).pop(0)
            amap = maps[mapp][destmap]
            for deststart, sourcestart, length in amap:
                if position >= sourcestart and position < sourcestart+length:
                    position = deststart + (position-sourcestart)
                    break
            mapp = destmap
        print(memo_locs)
        for memo_loc in memo_locs:
            memo[memo_loc] = position
        locations.append(position)
print(min(locations))
