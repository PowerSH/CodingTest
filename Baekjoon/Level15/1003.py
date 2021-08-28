T = int(input())

memory = [[0, 0]] * 41

def fibonacci(n):    
    if n == 0:
        return [1, 0]

    elif n == 1:        
        return [0, 1]

    if memory[n] != [0, 0]:        
        return memory[n]
    
    memory[n] = [x + y for x,y in zip(fibonacci(n-1), fibonacci(n-2))]    

    return memory[n]

for idx in range(T):
    num = int(input())
    fibo = fibonacci(num)

    print(fibo[0], fibo[1])