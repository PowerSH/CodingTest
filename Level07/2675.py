T = int(input())

for idx1 in range(T):
    R, S = input().split()
    
    for idx2 in range(len(S)):
        print(S[idx2]*int(R), end='')
    print("")