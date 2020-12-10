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


looped = 0 
def checklist(listcheck):
    global looped , error 
    used = []
    start = 0
    currentline = 0
    nextline = 0
    acc = 0
    previousline = 0
    while True:
        if listcheck[currentline] == listcheck[-1]:
            print(f"reached end of program acc = {acc}")
            break
        if listcheck[currentline] in used:
            error =[]
            if looped == 0:
                for i in used:
                    hmm = i.split(" ")
                    if hmm[1] == "jmp" or hmm[1] == "nop":
                        error.append(i)
                looped = 1
                print('Found in list already, Breaking loop')
                print(f'Current line :{listcheck[currentline]}')
                print(f'Previous line : {listcheck[previousline]}')
                print(f"acc = {acc}")
                break
            else:
                break
        used.append(listcheck[currentline])
        splitlines = listcheck[currentline].split(" ")
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

checklist(labeledlist)


for i in error:
    replacement = (i.split(" "))
    if replacement[1] == 'jmp':
        replacement[1] = 'nop'
    else:
        replacement[1] = 'jmp'

    copylist = labeledlist.copy()
    copylist[int(replacement[0])-1] = f'{replacement[0]} {replacement[1]} {replacement[2]}'
    checklist(copylist)
    