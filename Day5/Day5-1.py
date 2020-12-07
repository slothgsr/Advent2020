import os

os.chdir((os.path.dirname(os.path.realpath(__file__))))

file = ("test.txt")

with open(file) as f:
    tickets = [line.rstrip('\n') for line in f]



rowsmin = 0
rowsmax = 127
columnsmax = 8
columnsmin = 0


for ticket in tickets:
    rowsmin = 0
    rowsmax = 128
    columnsmax = 8
    columnsmin = 0
    print("ticket")
    if ticket[0] == "F" :
            rowsmax = (rowsmax - rowsmin) /2
            print("max:",rowsmax)
            print("min:",rowsmin)
    if ticket[0] == "B" :
            rowsmin = (rowsmax - rowsmin) /2
            print("max:",rowsmax)
            print("min:",rowsmin)
    for letter in ticket[1:7]:
        if letter == "F" and letter == ticket[0]:
            rowsmax = rowsmax - (rowsmax - rowsmin) /2
            print("max:",rowsmax)
            print("min:",rowsmin)
        if letter == "B" and letter == ticket[0]:
            rowsmin = rowsmin + (rowsmax - rowsmin) /2
            print("max:",rowsmax)
            print("min:",rowsmin)
            
    print(rowsmax,rowsmin)


