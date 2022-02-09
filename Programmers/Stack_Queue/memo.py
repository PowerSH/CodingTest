from collections import deque
def solution(priorities, location):
    priorities_dict={}
    start=deque([])
    for i in range(len(priorities)):
        priorities_dict[i] = priorities[i]
        start.append(i)
    sequence=[]
    while start:
        maxval=max(priorities)
        if priorities_dict[start[0]]<maxval:
            start.append(start.popleft())
        else:
            sequence.append(start[0])
            priorities.remove(priorities_dict[start.popleft()])
    return sequence.index(location)+1