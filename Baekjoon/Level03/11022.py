T = int(input())

for idx in range(T):
    A, B = map(int, input().split())
    print("Case #" + str(idx+1) + ":", A, "+" ,B , "=", A + B)