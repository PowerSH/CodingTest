def solution(answers):
    answer = []
    score = {'1':0, '2':0, '3':0}

    A = [1,2,3,4,5]
    B = [2,1,2,3,2,4,2,5]
    C = [3,3,1,1,2,2,4,4,5,5]

    while len(A) < len(answers):
        A += A
    while len(B) < len(answers):
        B += B
    while len(C) < len(answers):
        C += C

    A = A[:len(answers)]
    B = B[:len(answers)]
    C = C[:len(answers)]

    for a, b, c, ans in zip(A, B, C, answers):
        if ans == a:
            score['1'] += 1
        if ans == b:
            score['2'] += 1
        if ans == c:
            score['3'] += 1

    print(score)
    maximum = max(score.values())

    for idx in score:        
        if maximum == score[idx]:
            answer.append(int(idx))

    return answer

answer = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(solution(answer))