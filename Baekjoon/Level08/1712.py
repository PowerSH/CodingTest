A, B, C = map(int, input().split())

if B >= C:
    print(-1)
elif A/(C-B) >= A//(C-B):
    print(int(A/(C-B) + 1))
else:
    print(A//(C-B))