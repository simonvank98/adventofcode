input = open("day6.txt").read().split('\n\n')
fishArr = [int(i) for i in input[0].split(',')]

fishAges = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0
}
for age in fishArr:
    fishAges[age] += 1

# part 1
# for i in range(80):

# part 2
for i in range(256):
    newFish = fishAges[6]
    fishAges[6] = fishAges[7] + fishAges[0]
    fishAges[7] = fishAges[8]
    fishAges[8] = fishAges[0]
    fishAges[0] = fishAges[1]
    fishAges[1] = fishAges[2]
    fishAges[2] = fishAges[3]
    fishAges[3] = fishAges[4]
    fishAges[4] = fishAges[5]
    fishAges[5] = newFish

# part 1
print('day 6 part 1: ', sum(fishAges.values()))

# part 2
print('day 6 part 2: ', sum(fishAges.values()))
