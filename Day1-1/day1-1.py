from itertools import combinations

with open("numbers.txt") as f:
    lines = [int(line.rstrip('\n')) for line in f]

combos = combinations(lines, 3)

for i in combos:
    if sum(i) == 2020:
        print(i[0] * i[1] * i[2])

                

