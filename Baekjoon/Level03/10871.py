N, X = map(int, input().split())
A = list(map(int, input().split()))

for idx in range(N):
    if A[idx] < X:
        print(A[idx], end=' ')