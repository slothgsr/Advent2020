#!/usr/bin/env python
import os
import bisect 

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
    print(ticket[0])

    for letter in ticket[0:7]:
        print(letter)
        if letter == "F":
            rowsmax = rowsmax - (rowsmax - rowsmin) /2
            # print("max:",rowsmax)
            # print("min:",rowsmin)
        if letter == "B":
            rowsmin = rowsmin + (rowsmax - rowsmin) /2
            # print("max:",rowsmax)
            # print("min:",rowsmin)
    rowsmax -= 1

    print(rowsmin, rowsmax)

