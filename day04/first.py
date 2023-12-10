#!/usr/bin/env python3.12
import sys
lines = [l.strip() for l in sys.stdin.readlines()]

cards = []
for l in lines:
    _, card = l.split(': ')
    winningstr, minestr = card.split(' | ')
    winning = set(int(n) for n in winningstr.split(' ') if n)
    mine = set(int(n) for n in minestr.split(' ') if n)
    cards.append((winning, mine))

score = 0
for winning, mine in cards:
    winners = winning.intersection(mine)
    if winners:
        score += 2**(len(winners)-1)
print(score)
