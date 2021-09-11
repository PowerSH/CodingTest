T = int(input())

for idx in range(T):
    A, B = map(int, input().split())
    print("Case #" + str(idx+1) + ":", A + B)

# str 형변환을 해줘야 자동 띄어쓰기를 방지함.