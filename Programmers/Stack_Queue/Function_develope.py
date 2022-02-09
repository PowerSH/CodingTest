def solution(progresses, speeds):
    answer = []    

    while(True):
        counter = 0

        if len(progresses) == 0:
            break

        for idx in range(len(progresses)):
            progresses[idx] += speeds[idx]

        # check part
        if progresses[0] >= 100:
            for idx in range(len(progresses)):
                if progresses[0] >= 100:
                    progresses.pop(0)
                    speeds.pop(0)
                    counter += 1
            answer.append(counter)        
            # print(progresses, counter)

    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

print(solution(progresses, speeds))