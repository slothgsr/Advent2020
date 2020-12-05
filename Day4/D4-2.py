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


for group in wordlist:
    for subgroup in group:
        if subgroup[0:4] == "byr:": 
            if len(subgroup) == 8:
                if 1920 <= int(subgroup[4:9]) <= 2002:
                    continue
                else:
                    group.remove(subgroup)
            else:
                group.remove(subgroup)
            
        if subgroup[0:4] == "iyr:": 
            if len(subgroup) == 8:
                if 2010 <= int(subgroup[4:9]) <= 2020:
                    continue
                else:
                    group.remove(subgroup)
            else:
                group.remove(subgroup)

        if subgroup[0:4] == "eyr:": 
            if 2020 <= int(subgroup[4:9]) <= 2030:
                continue
            else:
                group.remove(subgroup)
        
        if subgroup[0:4] == "hgt:": 
            if (subgroup[-2:]) == "in" or (subgroup[-2:]) == "cm":
                if (subgroup[-2:]) == "in":
                    try:
                        if 59 <= int(subgroup[4:6]) <= 76:
                            continue
                        else:
                            group.remove(subgroup)
                    except:
                        group.remove(subgroup)

                if (subgroup[-2:]) == "cm":
                    try:
                        if 150 <= int(subgroup[4:7]) <= 193:
                            continue
                        else:
                            group.remove(subgroup)
                    except:
                        group.remove(subgroup)
            else:
                group.remove(subgroup)

        allowed =["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
        if subgroup[0:4] == "hcl:":
            if len(subgroup) == 11:
                if subgroup[4] == "#":
                    for i in subgroup[5:]:
                        if i not in allowed:
                            group.remove(subgroup)
            else:
                group.remove(subgroup)
        eyes = ['amb','blu','brn','gry','grn','hzl','oth']

        if subgroup[0:4] == "ecl:":
            if subgroup[-3:] not in eyes:
                group.remove(subgroup)

        if subgroup[0:4] == "pid:":
            if len(subgroup) == 13:
                for i in subgroup[-9:]:
                    if i not in allowed[0:10]:
                        group.remove(subgroup)
            else:
                group.remove(subgroup)
    
positive = 0
for group in wordlist:
    hit = 0
    for subgroup in group:
        if subgroup[0:4] in musthave:
            hit += 1
    if hit >= 7:
         positive += 1
        
print(positive)


