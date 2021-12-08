with open('day1.txt') as f:
    input = f.read().split('\n')
    input = [int(i) for i in input]

output1 = 0
for i in range(1, len(input)):
    if input[i] > input[i -1]:
        output1 += 1
print('day 1 part 1: ', output1)

output2 = 0
for i in range(1, len(input)):
    curr = input[i - 1] + input[i - 2] + input[i - 3]
    prev = input[i] + input[i - 1] + input[i - 2]
    if prev > curr:
        output2 += 1
print('day 2 part 2: ', output2)
