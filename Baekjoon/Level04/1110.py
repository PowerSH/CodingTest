origin = input()
N = origin
cnt = 0

while True:    
    if int(N) < 10:
        N = "0" + str(int(N))
    
    temp = int(N[0]) + int(N[1])
    
    N = N[1] + str(temp%10)

    cnt += 1
    if int(origin) == int(N):
        break

print(cnt)