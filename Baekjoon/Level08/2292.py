N = int(input())

head = 1
tail = 1
count = 1

while True:    
    if N <= tail:
        # print("got ya", head, tail, count)
        print(count)
        break

    head = tail + 1
    tail += 6*count
    count += 1