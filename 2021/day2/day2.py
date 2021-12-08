with open('day2.txt') as f:
    input = f.read().split('\n')


correctInput = []
for i in range(len(input)):
    correctInput.append(input[i].strip().split(' '))

x = 0
y = 0
for i in correctInput:
    if i[0] == 'forward':
        x += int(i[1])
    if i[0] == 'down':
        y += int(i[1])
    if i[0] == 'up':
        y -= int(i[1])
print('day 2 part 1: ', x * y)

x = 0
y = 0
aim = 0

for i in correctInput:
    if i[0] == 'forward':
        x += int(i[1])
        y += aim * int(i[1])
    if i[0] == 'down':
        aim += int(i[1])
    if i[0] == 'up':
        aim -= int(i[1])
print('day 2 part 2: ', x * y)