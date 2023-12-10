#!/usr/bin/env python3.12
import sys
from collections import defaultdict
lines = [l.strip() for l in sys.stdin.readlines()]

cards = []
for l in lines:
    _, card = l.split(': ')
    winningstr, minestr = card.split(' | ')
    winning = set(int(n) for n in winningstr.split(' ') if n)
    mine = set(int(n) for n in minestr.split(' ') if n)
    cards.append((winning, mine))

scored = {}
for i, (winning, mine) in enumerate(cards):
    winners = winning.intersection(mine)
    scored[i] = winners

memo = [1]*len(cards)
for i in range(len(cards)-1, -1, -1):
    if len(scored[i])>0:
        for j in range(i+1, i+1+len(scored[i])):
            memo[i] += memo[j]
print(sum(memo))
