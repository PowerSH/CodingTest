N = int(input())
A = list(map(int, input().split()))

min, max = 1000000, -1000000

for idx in range(N):
    if A[idx] > max:
        max = A[idx]
    
    if A[idx] < min:
        min = A[idx]

print(min, max)