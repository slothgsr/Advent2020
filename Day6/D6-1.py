import os

os.chdir((os.path.dirname(os.path.realpath(__file__))))

file = ("input.txt")

with open(file) as f:
    wordlist =[]
    templist =[]
    for line in f.readlines():
        if line == "\n":
                wordlist.append(templist)
                templist = []
        for word in line.strip('\n'):
            templist.append(word)
    wordlist.append(templist)

setlist = []
for group in wordlist:
    setlist.append(set(group))

listlengths = []
for i in setlist:
    listlengths.append(len(i))

print(sum(listlengths))


