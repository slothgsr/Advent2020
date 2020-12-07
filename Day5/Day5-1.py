#!/usr/bin/env python
import os

os.chdir((os.path.dirname(os.path.realpath(__file__))))

file = ("input.txt")

with open(file) as f:
    tickets = [line.rstrip('\n') for line in f]

seats = []
for ticket in tickets:
    rowsmin = 0
    rowsmax = 127
    columnsmax = 7
    columnsmin = 0
    for letter in ticket[0:7]:
        if letter == "F":
            rowsmax = rowsmax - (rowsmax - rowsmin + 1) /2
        if letter == "B":
            rowsmin = rowsmin + (rowsmax - rowsmin + 1) /2

    row = int(rowsmin)

    for letter in ticket[7:]:
        if letter == "L":
            columnsmax = columnsmax - (columnsmax - columnsmin + 1) /2
        if letter == "R":
            columnsmin = columnsmin + (columnsmax - columnsmin + 1) /2

    column = int(columnsmin)

    seats.append(row * 8  + column)

print("Max seat ID:", sorted(seats)[-1])

start = 71
for i in sorted(seats):
    if int(i)  != start:
        print("Missing Seat ID:", i-1)
        start += 1
    start += 1


