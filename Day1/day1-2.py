from itertools import combinations

file = (r'C:\Users\SlothGSR\Desktop\python_stuff\MyPythonScripts\Advent2020\Day1\numbers.txt')

with open(file) as f:
    lines = [int(line.rstrip('\n')) for line in f]

combos = combinations(lines, 3)

for i in combos:
    if sum(i) == 2020:
        print(i[0] * i[1] * i[2])
