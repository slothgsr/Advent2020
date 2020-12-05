import os
import itertools

file = (r'C:\Users\Dustin\Desktop\MyPythonScripts\advent2020\Advent2020\Day4\input.txt')

with open(file) as f:
    space = 1
    wordlist =[]
    templist =[]
    for line in f.readlines():
        if line == "\n":
                wordlist.append(templist)
                templist = []
        for word in line.split():
            templist.append(word)
    wordlist.append(templist)

musthave=['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:']
positive = 0
for group in wordlist:
    hit = 0
    for subgroup in group:
        if subgroup[0:4] in musthave:
            hit += 1
    if hit >= 7:
         positive += 1
        
print(positive)