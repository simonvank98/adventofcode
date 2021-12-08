grid = {}

def calculateOverlappingPoints(list, part2=False):
    for line in list:
        x1, y1 = map(int, line[0].split(","))
        x2, y2 = map(int, line[1].split(","))

        minX = min(x1, x2)
        maxX = max(x1, x2)
        minY = min(y1, y2)
        maxY = max(y1, y2)

        # part 2
        if (part2 and (x1 != x2 and y1 != y2)):
            diffX = x1 - x2
            diffY = y1 - y2

            startX = x1
            startY = y1

            for i in range(0, abs(diffX) + 1):
                x = startX - i if diffX > 0 else startX + i
                y = startY - i if diffY > 0 else startY + i

                increment_grid_position((x, y))

        if (x1 != x2 and y1 != y2):
            continue

        if (minX < maxX):
            for x in range(minX, maxX + 1):
                increment_grid_position((x, y1))

        if (minY < maxY):
            for y in range(minY, maxY + 1):
                increment_grid_position((x1, y))

    points = 0
    for key in grid:
        if grid[key] > 1:
            points += 1

    print_grid()
    return points


def increment_grid_position(key):
    if (key) in grid:
        grid[key] += 1
    else:
        grid[key] = 1


def print_grid():
    for y in range(100):
        for x in range(100):
            if (x, y) in grid:
                print(grid[(x, y)], end="")
            else:
                print('.', end="")
        print()


def read_file():
    file = open("day5.txt").read()
    lines = file.split("\n")
    cords = []
    for line in lines:
        cords.append(line.split(" -> "))
    return cords


if __name__ == '__main__':
    list = read_file()
    # print('day5 part 1: ', calculateOverlappingPoints(list))
    print('day5 part 2: ', calculateOverlappingPoints(list, True))
