#!/usr/bin/env python
import os
os.chdir((os.path.dirname(os.path.realpath(__file__))))

file = ("input.txt")

with open(file) as f:
    bags = [line.rstrip('\n') for line in f]

print(bags)



