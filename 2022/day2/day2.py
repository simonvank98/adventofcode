with open ('day2.txt') as f:
    input = f.read().split('\n')
    scores = {
        'B X': 1, 'C Y': 2, 'A Z': 3, 'A X': 4, 'B Y': 5, 'C Z': 6, 'C X': 7, 'A Y': 8, 'B Z': 9
    }
    total_score = 0
    for i in input:
        total_score += scores[i]
    print('day2 part 1: ', total_score)

    new_scores = {
        'A X': 3, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7
    }
    total_score = 0
    for i in input:
        total_score += new_scores[i]
    print('day2 part 2: ', total_score)

