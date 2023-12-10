#!/usr/bin/env python3.12

import sys

lines = [l.strip() for l in sys.stdin.readlines()]

trans = {'zero': 0,
         'one': 1,
         'two': 2,
         'three': 3,
         'four': 4,
         'five': 5,
         'six': 6,
         'seven': 7,
         'eight': 8,
         'nine': 9}

digits = []
for l in lines:
    digits.append([])
    for i, c in enumerate(l):
        if c.isdigit():
            digits[-1].append(int(c))
        else:
            for word, value in trans.items():
                if l[i:].startswith(word):
                    digits[-1].append(value)
            


val = sum(int(f'{line[0]}{line[-1]}') for line in digits)
print(val)


