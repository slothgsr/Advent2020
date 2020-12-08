import os

os.chdir((os.path.dirname(os.path.realpath(__file__))))

file = ("input.txt")

with open(file) as f:
    operations = [(line.rstrip('\n')) for line in f]


label = 1

labeledlist = []

for i in operations:
    labeledlist.append(f"{i} ,line:{label}: ")
    label += 1

print(labeledlist)

# acc = 0
# nextline = 0
# used = []
# for i in range(len(operations)):

#     if operations[i][0:3] == "nop":
#         nextline = i+1
#         used.append(i)
    
        

print(len(operations))

#TODO number each line
#TODO iterate operations
#TODO Log what line is being called.
#TODO if repeat.  return acc number

