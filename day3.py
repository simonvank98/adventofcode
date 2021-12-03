with open('day3.txt') as f:
    input = f.read().split('\n')
print(input)

i = 0
gamma = ''
epsilon = ''

while i < 12:
    high = 0
    low = 0
    for j in input:
        if j[i] == '1':
            high += 1
        if j[i] == '0':
            low += 1
    if high > low:
        gamma += '1'
        epsilon += '0'
    if low > high:
        gamma += '0'
        epsilon += '1'

    i += 1
print('day 3 part 1: ', int(gamma, 2) * int(epsilon, 2))

i = 0
while i < 12:
    highList = []
    lowList = []
    for j in input:
        if j[i] == '1':
            highList.append(j)
        if j[i] == '0':
            lowList.append(j)
    if len(highList) >= len(lowList):
        input = highList
    if len(highList) < len(lowList):
        input = lowList
    i += 1
oxygen = input[0]

i = 0
with open('day3.txt') as f:
    input = f.read().split('\n')
while i < 12:
    highList = []
    lowList = []
    if len(input) == 1:
        break
    for j in input:
        # print(input)
        if j[i] == '1':
            highList.append(j)
        if j[i] == '0':
            lowList.append(j)
    # print(len(highList), len(lowList))
    if len(highList) < len(lowList):
        input = highList
    if len(highList) >= len(lowList):
        input = lowList
    i += 1
co2 = input[0]

print('day 3 part 2: ', int(oxygen, 2) * int(co2, 2))
