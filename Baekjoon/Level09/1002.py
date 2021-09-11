T = int(input())

for idx in range(T):
    num = map(float, input().split())
    x1, y1, r1, x2, y2, r2 = num
    
    max_r = max(r1, r2)
    min_r = min(r1, r2)

    d = ((x1 - x2)**2 + (y1 - y2)**2)**(0.5)    
    
    if d == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)

    elif max_r + min_r < d or max_r - min_r > d:
        print(0)
    elif max_r + min_r == d or max_r - min_r == d:
        print(1)
    else:
        print(2)