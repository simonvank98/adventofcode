input = open("day7.txt").read()
crabs = [int(i) for i in input.split(',')]

# part 1
fuelCosts = []
for i in range(min(crabs), max(crabs)):
    fuel = 0
    for crab in crabs:
        # part 1
        # fuel += abs(i - crab)

        # part 2
        # n * (n+1) // 2 aka triangle numbers
        fuel += abs(i - crab) * (abs(i - crab) + 1) / 2

    fuelCosts.append(int(fuel))

# print('day 7 part 1: ', min(fuelCosts))
print('day 7 part 2: ', min(fuelCosts))
