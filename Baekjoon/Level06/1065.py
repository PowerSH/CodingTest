N = int(input())
count = 0

def count_han(N):
    if N < 100:
        return 0
    else:
        h = N//100
        t = (N%100)//10
        o = N%10
        
        if h-t == t-o:            
            return 0

    return 1

for idx in range(1, N+1):    
    if count_han(idx) == 0:
        count += 1

print(count)