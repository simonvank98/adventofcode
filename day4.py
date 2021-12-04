def makeBoards(board):
    newBoard = []
    for y in range(len(board)):
        row = board[y].strip().replace(r'  ', ' ').split(' ')
        newRow = []
        for x in range(len(row)):
            newRow.append(int(row[x]))
        newBoard.append(newRow)
    return newBoard


def checkBoards(board):
    for x in range(len(board)):
        if board[x][0] + board[x][1] + board[x][2] + board[x][3] + board[x][4] == -5:
            return True
        y = [y[x] for y in board]
        if y[0] + y[1] + y[2] + y[3] + y[4] == -5:
            return True


def playBingo(boards):
    winningBoards = []
    for number in numbers:
        for i in range(len(boards)):
            for y in range(len(boards[i])):
                for x in range(len(boards[i][y])):
                    if number == boards[i][y][x]:
                        boards[i][y][x] = -1
                        if checkBoards(boards[i]):
                            print(boards[i])
                            print(number)
                            winningBoards.append(boards[i])
                            print(len(winningBoards))
                            if len(winningBoards) == len(boards):
                                return winningBoards[-1], number  # part 2
                            # return boards[i], number  # part 1


def calculateNumber(board, number):
    totalNumber = 0
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] != -1:
                totalNumber += board[x][y]
    return totalNumber * number


input = open("day4.txt").read().split('\n\n')
numbers = [int(i) for i in input[0].split(',')]
boards = [board.split('\n') for board in input[1:]]
newBoards = [makeBoards(board) for board in boards]
result = playBingo(newBoards)
# print('day 4 part 1: ', calculateNumber(result[0], result[1]))
print(result)
print('day 4 part 2: ', calculateNumber(result[0], result[1]))
