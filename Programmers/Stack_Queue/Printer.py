def solution(priorities, location):
    answer = 0
    hash = {}
    start = []
    seq = []

    for cnt, idx in enumerate(priorities):        
        hash[cnt] = idx
        start.append(cnt)

    while start:
        maxval = max(priorities)
        if hash[start[0]] < maxval:
            start.append(start.pop(0))
        else:
            seq.append(start[0])
            priorities.remove(hash[start.pop(0)])

        # print(start, seq, priorities)
    
    answer = seq.index(location)+1
    return answer

# priorities = [2, 1, 3, 2]
# location = 2

# priorities = [1, 1, 9, 1, 1, 1]
# location = 0

# priorities = [1, 1, 7, 5, 3, 11, 15]
# location = 3

priorities = [1, 2, 8, 3, 4]
location = 4

print("Final Answer : ", solution(priorities, location))