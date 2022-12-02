input = open("day9.txt").read().split('\n')

lowPoints = []

for row in range(len(input)):
    for i in range(10):
        if row != 0 and row != 4 and i != 0 and i != 9:
            if input[row][i] < input[row][i - 1] and input[row][i] < input[row][i + 1] and input[row][i] < input[row - 1][i] and input[row][i] < input[row + 1][i]:
                lowPoints.append(int(input[row][i]) + 1)
        else:
            if 
print(lowPoints)
