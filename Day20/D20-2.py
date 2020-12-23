import os

os.chdir((os.path.dirname(os.path.realpath(__file__))))

file = ("input.txt")

with open(file) as f:
    tilelist =[]
    templist =[]
    for line in f.readlines():
        if line == "\n":
            tilelist.append(templist)
            templist = []
            continue
        templist.append(line.strip('\n'))
        

for i in tilelist[:1]:
    print(i)


for tile in tilelist[:1]:
    topside = tile[1]
    bottom = tile[10]
    left = ''.join([x[0] for x in tile[1:]])
    right = ''.join([x[9] for x in tile[1:]])
    # print(topside)
    # print(bottom)
    # print(left)
    # print(right)
    
