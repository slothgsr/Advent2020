#!/usr/bin/env python
import os
from itertools import combinations

os.chdir((os.path.dirname(os.path.realpath(__file__))))

file = ("input.txt")

with open(file) as f:
    numbers = [int(line.rstrip('\n')) for line in f]


def combocheck(start,numbers):
    chunk = numbers[start - 25:start]
    combos = combinations(chunk,2)
    good = False
    for combo in combos:
        if numbers[start] == sum(combo):
            good = True
    return good


start = 26
for i in numbers[26:]:
    if combocheck(start,numbers) == True:
        start +=1
    else:
        print("no good",i)
        start +=1