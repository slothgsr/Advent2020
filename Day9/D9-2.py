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
        nogood = i
        start +=1

print(nogood)

for i in range(len(numbers)):
    templist=[]
    adder = i
    start = numbers[i]
    templist.append(start)
    while sum(templist) < nogood:
        adder += 1
        templist.append(numbers[adder])

        if sum(templist) == nogood:
            print(sorted(templist)[0] + sorted(templist)[-1])
            break

        









