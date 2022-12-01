with open('day1.txt') as f:
    input = f.read().split('\n\n')
    calories = []
    for i in input:
        j = i.split('\n')
        calories += [[int(k) for k in j]]

    highest = 0
    total_list = []

    for i in calories:
        total = int(sum(i))
        total_list.append(total)
        if total > highest:
            highest = total

    print('day 1 part 1: ', highest)
    total_list.sort(reverse=True)
    highest_three = total_list[0] + total_list[1] + total_list[2]
    print('day 1 part 2: ', highest_three)


