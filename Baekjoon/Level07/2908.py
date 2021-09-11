A, B = input().split()
A = A[2] + A[1] + A[0]
B = B[2] + B[1] + B[0]

if int(A) > int(B):
    print(int(A))
else:
    print(int(B))