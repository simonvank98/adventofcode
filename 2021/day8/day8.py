input = open("day8.txt").read().split('\n')
screenOutputs = []
for i in input:
    screenOutputs.append(i.split(' | ', 1)[1])

digits = []
for j in screenOutputs:
    digits.append(j.split(' '))

digits = [item for sublist in digits for item in sublist]

dict = {
    2: 0,
    3: 0,
    4: 0,
    7: 0
}

lengths = [2, 3, 4, 7]
for d in digits:
    if len(d) in lengths:
        dict[len(d)] += 1

print('day 7 part 1: ', sum(dict.values()))
