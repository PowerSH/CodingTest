N = int(input())

result = 0

for idx1 in range(N):    
    text = input()
    temp = ''
    check = list()

    for idx2 in text:
        if idx2 != temp:
            check.append(idx2)
        temp = idx2
    
    if len(check) == len(set(check)):
        result += 1

print(result)