def convert(line):
    global correct
    Dashpos = line.find('-')
    letterpos = line.find(':') - 1
    letter = line[letterpos]
    if Dashpos == 1:
        num1= int(line[0])
        if line[3] == ' ':
            num2 = int(line[2])
        else:
            num2 = int(line[2:4])
    if Dashpos == 2:
        num1 = int(line[0:2])
        num2 = int(line[3:5])
    lettercount = line.count(letter) -1
    if lettercount >= num1 and lettercount <= num2:
        correct += 1

file = (r'C:\Users\SlothGSR\Desktop\python_stuff\MyPythonScripts\Advent2020\Day2\pws.txt')

with open(file) as f:
    lines = [line.rstrip('\n') for line in f]

correct = 0
for combo in lines:
    convert(combo)

print(correct)