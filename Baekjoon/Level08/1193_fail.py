X = int(input())

# 1 2 3 4 5 6 7 8 

counter = 1
flag = 1
temp = X

while True:
    # print(counter)
    temp -= counter

    if temp <= 0:        
        # print("temp:", temp, "X:", X, "counter:", counter)    
        break
    
    counter += 1
    flag *= -1

if flag == 1:
    # print("Up")
    for idx in range(counter):        
        if temp + counter == idx+1:
            print(counter-idx,"/",idx+1)
            break
        
else:
    # print("Down")
    for idx in range(counter):
        if temp + counter == idx+1:
            print(idx+1,"/",counter-idx)
            break