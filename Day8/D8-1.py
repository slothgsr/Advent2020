import os

os.chdir((os.path.dirname(os.path.realpath(__file__))))

file = ("input.txt")

with open(file) as f:
    operations = [(line.rstrip('\n')) for line in f]

label = 1
labeledlist = []
for i in operations:
    labeledlist.append(f"{label} {i} ")
    label += 1

used = []
start = 0
currentline = 0
nextline = 0
acc = 0
previousline = 0

    
while True:
    if labeledlist[currentline] == labeledlist[-1]:
        print(f"reached end of program aac = {aac}")
    if labeledlist[currentline] in used:
        print('Found in list already, Breaking loop')
        print(f'Current line :{labeledlist[currentline]}')
        print(f'Previous line : {labeledlist[previousline]}')
        print(f"acc = {acc}")
        break
    used.append(labeledlist[currentline])
    splitlines = labeledlist[currentline].split(" ")
    previousline = currentline
    if splitlines[1] == "nop":
        currentline += 1
    if splitlines[1] == "acc":
        if splitlines[2][0] == "+":
            acc += int(splitlines[2][1:])
        else:
            acc -= int(splitlines[2][1:])
        currentline += 1 
    if splitlines[1] == "jmp":
        if splitlines[2][0] == "+":
            currentline += int(splitlines[2][1:])
        else:
            currentline -= int(splitlines[2][1:])

    

