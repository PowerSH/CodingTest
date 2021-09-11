T = int(input())

for idx1 in range(T):
    Q = input()
    sum = 0
    count = 0
    for idx2 in range(len(Q)):        
        if Q[idx2] == 'O':
            count = 1 + count
            sum += count
        else:
            count = 0

    print(sum)