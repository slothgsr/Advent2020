import os

os.chdir((os.path.dirname(os.path.realpath(__file__))))

file = ("sample.txt")

with open(file) as f:
    operations = [(line.rstrip('\n')) for line in f]

label = 1
labeledlist = []
for i in operations:
    labeledlist.append(f"{label} {i}, ")
    label += 1

print(labeledlist)

checking = True
used = []
start = 0
currentline = 0
nextline = 0
acc = 0




    
while checking:
    if labeledlist[currentline] in used:
        print(acc)
        checking = False
    used.append(labeledlist[currentline])
    splitlines = labeledlist[currentline].split(" ")
    print(splitlines)
    if splitlines[1] == "nop":
        currentline += 1
    if splitlines[1] == "acc":
        if splitlines[1[0]] == "+":
            acc += int(splitlines[2])
        else:
            acc -= int(splitlines[2])
        currentline += 1 
    if splitlines[1] == "jmp":
        if splitlines[1[0]] == "+":
            currentline += int(splitlines[2])
        else:
            currentline -= int(splitlines[2])

    

