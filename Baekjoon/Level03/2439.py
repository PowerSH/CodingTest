N = int(input())

for idx1 in range(1, N+1):
    for idx2 in range(N-idx1):
        print(" ", end='')
    for idx3 in range(idx1):
        print("*", end='')        
    print("")