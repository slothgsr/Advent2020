def loop(line):
    global x
    x += 1
    if x > len(line):
        x = x - len(line)
        if debug == True:
            print("shift x start posistion by:", x)          
    if line[x-1] == "#":
        trees = 1
        if debug == True:
            print("tree posistion",x)
        return trees

file = (r'C:\Users\SlothGSR\Desktop\python_stuff\MyPythonScripts\Advent2020\Day3\input.txt')

with open(file) as f:
    lines = [line.rstrip('\n') for line in f]


debug = False

trees = 0
x = 1
test =0
for line in lines[2::2]:
    if debug == True:
        print(line)
    test += 1
    if loop(line) == 1:
        trees += 1
        
        if debug == True:
            print(f' {line} hit tree on line # {test + 1}')
            print()
    

print("Total of trees hit:",trees)
