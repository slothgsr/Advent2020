import os

os.chdir((os.path.dirname(os.path.realpath(__file__))))

file = ("input.txt")

with open(file) as f:
    wordlist =[]
    templist =[]
    people_count = 0
    for line in f.readlines():
        people_count += 1
        if line == "\n":
                people_count -=1
                templist.append(people_count)
                wordlist.append(templist)
                templist = []
                people_count = 0
        for letter in line.strip('\n'):
            templist.append(letter)
    templist.append(people_count)
    wordlist.append(templist)

sumlist = []
for item in wordlist:
    poped = item.pop()
    if poped == 1:
        sumlist.append(len(item))
    else:
        setitem = set(item)
        counter = 0
        for i in setitem:
            if item.count(i) == int(poped):
                counter += 1
        sumlist.append(counter)
        
print(sum(sumlist))

