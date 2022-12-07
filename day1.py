elf = []
biggest = 0
middle = 0
smallest = 0
total = 0
sum = []
def read_file():
    with open('calories.txt', 'r') as f:
        lines = f.readlines()
    return lines

lines = read_file()


for line in lines:
    line = line.strip()
    if(line != ''):
        total += int(line)     
    else:
        elf.append(total)
        total = 0

elf.sort(reverse=True)

for i in range(3):
    print(elf[i])

x = 68923 + 67023 + 64098
print(x)